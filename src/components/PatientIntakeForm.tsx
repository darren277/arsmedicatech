import { useState } from 'react';
import { SubmitHandler, useForm } from 'react-hook-form';
import { MdArrowBack, MdArrowForward, MdWarning } from 'react-icons/md';
import { useParams } from 'react-router-dom';
import { API_URL } from '../env_vars';
import logger from '../services/logging';
import {
  Button,
  Card,
  CardContent,
  Checkbox,
  IconButton,
  Input,
  RequiredAsterisk,
} from './FormComponents';

/**
 * Progressive, multi‑page patient intake form
 * ‑ Uses React Hook Form for state/validation
 * ‑ Persists to the backend on every page transition (PATCH → /api/intake/:patientId)
 */

function useSimpleMutation<TPayload>(
  submitFn: (payload: TPayload) => Promise<any>
) {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<null | Error>(null);

  const mutate = async (payload: TPayload) => {
    setIsLoading(true);
    setError(null);
    try {
      await submitFn(payload);
    } catch (err) {
      setError(err instanceof Error ? err : new Error('Unknown error'));
    } finally {
      setIsLoading(false);
    }
  };

  return { mutate, isLoading, error };
}

interface PatientIntakeFormValues {
  /* Step 1 – Personal */
  firstName: string;
  lastName: string;
  date_of_birth: string;
  gender: string;
  phone: string;
  email: string;
  /* Step 2 – Address + Insurance */
  address: string;
  city: string;
  province: string;
  postalCode: string;
  insuranceProvider: string;
  insuranceNumber: string;
  /* Step 3 – Medical History */
  medicalConditions: string;
  medications: string;
  allergies: string;
  /* Step 4 – Visit Details */
  reasonForVisit: string;
  symptoms: string;
  symptomOnset: string;
  /* Step 5 – Consent */
  consent: boolean;
}

const initialValues: PatientIntakeFormValues = {
  firstName: '',
  lastName: '',
  date_of_birth: '',
  gender: '',
  phone: '',
  email: '',
  address: '',
  city: '',
  province: '',
  postalCode: '',
  insuranceProvider: '',
  insuranceNumber: '',
  medicalConditions: '',
  medications: '',
  allergies: '',
  reasonForVisit: '',
  symptoms: '',
  symptomOnset: '',
  consent: false,
};

type Step = 0 | 1 | 2 | 3 | 4;

// Helper to check if all required fields in a step are filled
const isStepComplete = (
  stepFields: (keyof PatientIntakeFormValues)[],
  values: PatientIntakeFormValues
) => {
  logger.debug('Checking step completion for fields:', stepFields);
  logger.debug('Current values:', values);

  const result = stepFields.every(field => {
    const value = values[field];
    logger.debug(`Field ${field}:`, { value, t: typeof value });

    if (field === 'consent') {
      const isValid = Boolean(value);
      logger.debug(`Consent field valid:`, isValid);
      return isValid;
    }

    const isValid = value && value.toString().trim() !== '';
    logger.debug(`Field ${field} valid:`, isValid);
    return isValid;
  });

  logger.debug('Step complete result:', result);
  return result;
};

export default function PatientIntakeForm() {
  const { patientId } = useParams<{ patientId: string }>();
  const [step, setStep] = useState<Step>(0);

  const {
    register,
    handleSubmit,
    formState: { errors },
    trigger,
    getValues,
  } = useForm<PatientIntakeFormValues>({
    defaultValues: initialValues,
    mode: 'onBlur',
  });

  /**
   * PATCH to backend – persists partial payload for the current step.
   * Backend should merge‑patch into existing intake doc keyed by patientId.
   */
  const mutation = useSimpleMutation(
    async (data: Partial<PatientIntakeFormValues>): Promise<void> => {
      const res = await fetch(`${API_URL}/api/intake/${patientId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      if (!res.ok) throw new Error('Failed to save intake data');
    }
  );

  const stepLabels = [
    'Personal Information',
    'Address & Insurance',
    'Medical History',
    'Visit Details',
    'Consent & Review',
  ] as const;

  const stepFieldMap: Record<Step, (keyof PatientIntakeFormValues)[]> = {
    0: ['firstName', 'lastName', 'date_of_birth', 'gender', 'phone', 'email'],
    1: [
      'address',
      'city',
      'province',
      'postalCode',
      'insuranceProvider',
      'insuranceNumber',
    ],
    2: ['medicalConditions', 'medications', 'allergies'],
    3: ['reasonForVisit', 'symptoms', 'symptomOnset'],
    4: ['consent'],
  };

  const next = async () => {
    const valid = await trigger(stepFieldMap[step]);
    if (!valid) return;
    const payload = Object.fromEntries(
      stepFieldMap[step].map(k => [k, getValues(k)])
    ) as Partial<PatientIntakeFormValues>;
    mutation.mutate(payload);
    if (step < 4) setStep(s => (s + 1) as Step);
  };

  const back = () => step > 0 && setStep(s => (s - 1) as Step);

  const submit: SubmitHandler<PatientIntakeFormValues> = async (
    data: PatientIntakeFormValues
  ): Promise<void> => {
    await mutation.mutate(data);
    // navigate to confirmation / dashboard, etc.
  };

  const progress = ((step + 1) / stepLabels.length) * 100;

  return (
    <Card className="max-w-3xl mx-auto p-6 md:p-10 rounded-2xl shadow-xl">
      {/* Stepper Breadcrumbs */}
      <div className="flex items-center justify-between mb-8">
        {stepLabels.map((label, idx) => {
          const complete = isStepComplete(
            stepFieldMap[idx as Step],
            getValues()
          );
          const isActive = step === idx;
          // Allow navigation to current, previous, or completed steps
          const canNavigate = idx <= step || complete;
          return (
            <div
              key={label}
              className="flex-1 flex flex-col items-center relative"
            >
              <button
                type="button"
                onClick={() => canNavigate && setStep(idx as Step)}
                disabled={!canNavigate}
                className={`w-8 h-8 flex items-center justify-center rounded-full border-2 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-400
                  ${isActive ? 'border-blue-600 bg-blue-600 text-white' : complete ? 'border-green-500 bg-green-500 text-white' : 'border-gray-300 bg-white text-gray-400'}
                  ${canNavigate ? 'cursor-pointer hover:scale-110 hover:shadow-lg' : 'cursor-not-allowed opacity-60'}
                `}
                style={{ zIndex: 1 }}
                aria-current={isActive ? 'step' : undefined}
                aria-label={`Go to step ${idx + 1}: ${label}`}
              >
                {isActive ? idx + 1 : complete ? <MdArrowForward /> : idx + 1}
              </button>
              <span
                className={`mt-2 text-xs font-medium ${isActive ? 'text-blue-600' : complete ? 'text-green-600' : 'text-gray-400'}`}
              >
                {label}
              </span>
              {!complete && !isActive && (
                <MdWarning
                  className="absolute -top-2 right-0 text-yellow-500"
                  title="Required fields missing"
                />
              )}
              {idx < stepLabels.length - 1 && (
                <div
                  className="absolute left-1/2 top-4 w-full h-0.5 bg-gray-200"
                  style={{ zIndex: 0, width: '100%', marginLeft: '50%' }}
                />
              )}
            </div>
          );
        })}
      </div>

      <h2 className="text-2xl font-semibold mb-4 text-center">
        {stepLabels[step]}
      </h2>

      <form onSubmit={handleSubmit(submit)} className="space-y-8">
        {/* Step 1 */}
        {step === 0 && (
          <CardContent className="grid md:grid-cols-2 gap-6">
            <div>
              <label className="block mb-1 font-medium">
                First Name <RequiredAsterisk />
              </label>
              <Input
                placeholder="First Name"
                {...register('firstName', { required: true })}
                className={errors.firstName ? 'border-red-500' : ''}
              />
              {errors.firstName && (
                <p className="text-red-500 text-xs mt-1">
                  First name is required
                </p>
              )}
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Last Name <RequiredAsterisk />
              </label>
              <Input
                placeholder="Last Name"
                {...register('lastName', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Date of Birth <RequiredAsterisk />
              </label>
              <Input
                type="date"
                placeholder="Date of Birth"
                {...register('date_of_birth', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Gender <RequiredAsterisk />
              </label>
              <Input
                placeholder="Gender"
                {...register('gender', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Phone <RequiredAsterisk />
              </label>
              <Input
                placeholder="Phone"
                {...register('phone', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Email <RequiredAsterisk />
              </label>
              <Input
                type="email"
                placeholder="Email"
                {...register('email', { required: true })}
              />
            </div>
          </CardContent>
        )}
        {/* Step 2 */}
        {step === 1 && (
          <CardContent className="grid md:grid-cols-2 gap-6">
            <div>
              <label className="block mb-1 font-medium">
                Address <RequiredAsterisk />
              </label>
              <Input
                placeholder="Address"
                {...register('address', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                City <RequiredAsterisk />
              </label>
              <Input
                placeholder="City"
                {...register('city', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Province/State <RequiredAsterisk />
              </label>
              <Input
                placeholder="Province/State"
                {...register('province', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Postal / ZIP <RequiredAsterisk />
              </label>
              <Input
                placeholder="Postal / ZIP"
                {...register('postalCode', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Insurance Provider <RequiredAsterisk />
              </label>
              <Input
                placeholder="Insurance Provider"
                {...register('insuranceProvider', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Policy / Member # <RequiredAsterisk />
              </label>
              <Input
                placeholder="Policy / Member #"
                {...register('insuranceNumber', { required: true })}
              />
            </div>
          </CardContent>
        )}
        {/* Step 3 */}
        {step === 2 && (
          <CardContent className="grid gap-6">
            <div>
              <label className="block mb-1 font-medium">
                Known Medical Conditions
              </label>
              <Input
                placeholder="Known Medical Conditions"
                {...register('medicalConditions')}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Current Medications
              </label>
              <Input
                placeholder="Current Medications"
                {...register('medications')}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">Allergies</label>
              <Input placeholder="Allergies" {...register('allergies')} />
            </div>
          </CardContent>
        )}
        {/* Step 4 */}
        {step === 3 && (
          <CardContent className="grid gap-6">
            <div>
              <label className="block mb-1 font-medium">
                Reason for Visit <RequiredAsterisk />
              </label>
              <Input
                placeholder="Reason for Visit"
                {...register('reasonForVisit', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Key Symptoms <RequiredAsterisk />
              </label>
              <Input
                placeholder="Key Symptoms"
                {...register('symptoms', { required: true })}
              />
            </div>
            <div>
              <label className="block mb-1 font-medium">
                Symptom Onset Date
              </label>
              <Input
                type="date"
                placeholder="Symptom Onset Date"
                {...register('symptomOnset')}
              />
            </div>
          </CardContent>
        )}
        {/* Step 5 */}
        {step === 4 && (
          <CardContent className="space-y-4">
            <p className="text-sm leading-relaxed">
              Please review your information and consent to its use in
              accordance with our privacy policy.
            </p>
            <div className="flex items-center space-x-2">
              <Checkbox
                id="consent"
                {...register('consent', { required: true })}
              />
              <label htmlFor="consent" className="text-sm">
                I consent to the collection and use of my personal health
                information. <RequiredAsterisk />
              </label>
            </div>
          </CardContent>
        )}
        {/* Navigation */}
        <div className="flex justify-between pt-4 items-center">
          <IconButton
            icon={<MdArrowBack size={24} />}
            type="button"
            onClick={back}
            disabled={step === 0}
            aria-label="Back"
          />
          <div className="flex-1" />
          {step < 4 ? (
            <IconButton
              icon={<MdArrowForward size={24} />}
              type="button"
              onClick={next}
              //disabled={!isStepComplete(stepFieldMap[step], getValues()) || mutation.isLoading}
              disabled={mutation.isLoading} // Temporarily disable validation
              aria-label="Next"
              title="Next"
            />
          ) : (
            <Button
              type="submit"
              disabled={
                mutation.isLoading ||
                !isStepComplete(stepFieldMap[step], getValues())
              }
            >
              Submit
            </Button>
          )}
        </div>
      </form>

      {/* Debug Panel - Below the form */}
      <div className="mt-8 p-6 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl border border-blue-200">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold text-gray-800 flex items-center gap-2">
            <span className="w-2 h-2 bg-blue-500 rounded-full"></span>
            Form Debug Information
          </h3>
          <button
            type="button"
            onClick={() => logger.debug('Form values:', getValues())}
            className="bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded-lg text-sm font-medium transition-colors"
          >
            Log to Console
          </button>
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          <div className="space-y-3">
            <div className="flex items-center justify-between p-3 bg-white rounded-lg border">
              <span className="font-medium text-gray-700">Current Step:</span>
              <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded-md text-sm font-medium">
                {step + 1} of {stepLabels.length}
              </span>
            </div>
            <div className="flex items-center justify-between p-3 bg-white rounded-lg border">
              <span className="font-medium text-gray-700">Step Complete:</span>
              <span
                className={`px-2 py-1 rounded-md text-sm font-medium ${
                  isStepComplete(stepFieldMap[step], getValues())
                    ? 'bg-green-100 text-green-800'
                    : 'bg-yellow-100 text-yellow-800'
                }`}
              >
                {isStepComplete(stepFieldMap[step], getValues()) ? 'Yes' : 'No'}
              </span>
            </div>
            <div className="flex items-center justify-between p-3 bg-white rounded-lg border">
              <span className="font-medium text-gray-700">Loading:</span>
              <span
                className={`px-2 py-1 rounded-md text-sm font-medium ${
                  mutation.isLoading
                    ? 'bg-orange-100 text-orange-800'
                    : 'bg-gray-100 text-gray-800'
                }`}
              >
                {mutation.isLoading ? 'Yes' : 'No'}
              </span>
            </div>
          </div>

          <div className="p-3 bg-white rounded-lg border">
            <h4 className="font-medium text-gray-700 mb-2">
              Current Form Values:
            </h4>
            <pre className="text-xs text-gray-600 bg-gray-50 p-3 rounded overflow-auto max-h-32">
              {JSON.stringify(getValues(), null, 2)}
            </pre>
          </div>
        </div>
      </div>
    </Card>
  );
}
