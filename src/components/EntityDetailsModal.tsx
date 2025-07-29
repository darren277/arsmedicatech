import { EntityType } from '../types';

interface EntityDetailsModalProps {
  entity: EntityType | null;
  isOpen: boolean;
  onClose: () => void;
}

export function EntityDetailsModal({
  entity,
  isOpen,
  onClose,
}: EntityDetailsModalProps) {
  if (!isOpen || !entity) {
    return null;
  }

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-xl max-w-md w-full mx-4">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-gray-200">
          <h3 className="text-lg font-semibold text-gray-900">
            Entity Details
          </h3>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 transition-colors"
          >
            <svg
              className="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>

        {/* Content */}
        <div className="p-6">
          <div className="space-y-4">
            {/* Entity Text */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Entity Text
              </label>
              <div className="bg-blue-50 border border-blue-200 rounded-md p-3">
                <span className="text-blue-900 font-medium">{entity.text}</span>
              </div>
            </div>

            {/* Entity Type */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Entity Type
              </label>
              <div className="bg-gray-50 border border-gray-200 rounded-md p-3">
                <span className="text-gray-900">{entity.label}</span>
              </div>
            </div>

            {/* CUI (Concept Unique Identifier) */}
            {entity.cui && (
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  UMLS CUI
                </label>
                <div className="bg-gray-50 border border-gray-200 rounded-md p-3">
                  <span className="text-gray-900 font-mono text-sm">
                    {entity.cui}
                  </span>
                </div>
              </div>
            )}

            {/* ICD-10-CM Code */}
            {entity.icd10cm && (
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  ICD-10-CM Code
                </label>
                <div className="bg-green-50 border border-green-200 rounded-md p-3">
                  <span className="text-green-900 font-mono font-medium">
                    {entity.icd10cm}
                  </span>
                </div>
              </div>
            )}

            {/* ICD-10-CM Name */}
            {entity.icd10cm_name && (
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  ICD-10-CM Description
                </label>
                <div className="bg-green-50 border border-green-200 rounded-md p-3">
                  <span className="text-green-900">{entity.icd10cm_name}</span>
                </div>
              </div>
            )}

            {/* Position Information */}
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Start Position
                </label>
                <div className="bg-gray-50 border border-gray-200 rounded-md p-3">
                  <span className="text-gray-900">{entity.start_char}</span>
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  End Position
                </label>
                <div className="bg-gray-50 border border-gray-200 rounded-md p-3">
                  <span className="text-gray-900">{entity.end_char}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="flex justify-end p-6 border-t border-gray-200">
          <button
            onClick={onClose}
            className="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600 transition-colors"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
