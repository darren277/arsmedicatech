import { useState } from 'react';
import { SubmitHandler, useForm } from 'react-hook-form';
import { useParams } from 'react-router-dom';
import API_URL from '../env_vars';
import { Button, Card, CardContent, Checkbox, Input } from './FormComponents';

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
  dob: string;
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
  dob: '',
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
    0: ['firstName', 'lastName', 'dob', 'gender', 'phone', 'email'],
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
      {/* Progress bar */}
      <div className="w-full bg-gray-200 rounded-full h-2 mb-6">
        <div
          className="bg-blue-600 h-2 rounded-full transition-all"
          style={{ width: `${progress}%` }}
        />
      </div>

      <h2 className="text-2xl font-semibold mb-4">{stepLabels[step]}</h2>

      <form onSubmit={handleSubmit(submit)} className="space-y-6">
        {/* Step 1 */}
        {step === 0 && (
          <CardContent className="grid md:grid-cols-2 gap-4">
            <Input
              placeholder="First Name"
              {...register('firstName', { required: true })}
            />
            <Input
              placeholder="Last Name"
              {...register('lastName', { required: true })}
            />
            <Input
              type="date"
              placeholder="DOB"
              {...register('dob', { required: true })}
            />
            <Input
              placeholder="Gender"
              {...register('gender', { required: true })}
            />
            <Input
              placeholder="Phone"
              {...register('phone', { required: true })}
            />
            <Input
              type="email"
              placeholder="Email"
              {...register('email', { required: true })}
            />
          </CardContent>
        )}

        {/* Step 2 */}
        {step === 1 && (
          <CardContent className="grid md:grid-cols-2 gap-4">
            <Input
              placeholder="Address"
              {...register('address', { required: true })}
            />
            <Input
              placeholder="City"
              {...register('city', { required: true })}
            />
            <Input
              placeholder="Province/State"
              {...register('province', { required: true })}
            />
            <Input
              placeholder="Postal / ZIP"
              {...register('postalCode', { required: true })}
            />
            <Input
              placeholder="Insurance Provider"
              {...register('insuranceProvider', { required: true })}
            />
            <Input
              placeholder="Policy / Member #"
              {...register('insuranceNumber', { required: true })}
            />
          </CardContent>
        )}

        {/* Step 3 */}
        {step === 2 && (
          <CardContent className="grid gap-4">
            <Input
              placeholder="Known Medical Conditions"
              {...register('medicalConditions')}
            />
            <Input
              placeholder="Current Medications"
              {...register('medications')}
            />
            <Input placeholder="Allergies" {...register('allergies')} />
          </CardContent>
        )}

        {/* Step 4 */}
        {step === 3 && (
          <CardContent className="grid gap-4">
            <Input
              placeholder="Reason for Visit"
              {...register('reasonForVisit', { required: true })}
            />
            <Input
              placeholder="Key Symptoms"
              {...register('symptoms', { required: true })}
            />
            <Input
              type="date"
              placeholder="Symptom Onset Date"
              {...register('symptomOnset')}
            />
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
                information.
              </label>
            </div>
          </CardContent>
        )}

        {/* Navigation */}
        <div className="flex justify-between pt-4">
          <Button
            variant="secondary"
            type="button"
            onClick={back}
            disabled={step === 0}
          >
            Back
          </Button>
          {step < 4 ? (
            <Button type="button" onClick={next} disabled={mutation.isLoading}>
              Next
            </Button>
          ) : (
            <Button type="submit" disabled={mutation.isLoading}>
              Submit
            </Button>
          )}
        </div>
      </form>
    </Card>
  );
}
