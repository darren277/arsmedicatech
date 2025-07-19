import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { fileUploadAPI } from '../services/api';
import logger from '../services/logging';

interface Upload {
  id: string;
  file_name: string;
  file_type: string;
  date_uploaded: string;
  status: string;
  file_size: number;
  processed_text?: string;
  uploader?: string;
  file_path?: string;
  bucket_name?: string;
  s3_key?: string;
  task_id?: string;
}

const statusColors: Record<string, string> = {
  pending: '#fbbf24', // amber
  processing: '#60a5fa', // blue
  completed: '#22c55e', // green
  failed: '#ef4444', // red
  cancelled: '#a1a1aa', // gray
};

const UploadDetails: React.FC = () => {
  const { uploadId } = useParams<{ uploadId: string }>();
  const navigate = useNavigate();
  const [upload, setUpload] = useState<Upload | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (uploadId) {
      loadUploadDetails();
    }
  }, [uploadId]);

  const loadUploadDetails = async () => {
    if (!uploadId) return;

    setLoading(true);
    setError(null);
    try {
      const uploadData = await fileUploadAPI.getById(uploadId);
      setUpload(uploadData);
      logger.debug('Upload details loaded:', uploadData);
    } catch (err: any) {
      setError(err?.response?.data?.error || 'Failed to load upload details.');
      logger.error('Error loading upload details:', err);
    } finally {
      setLoading(false);
    }
  };

  const formatFileSize = (bytes: number): string => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  if (loading) {
    return (
      <div style={{ maxWidth: 800, margin: '40px auto', padding: 24 }}>
        <div style={{ textAlign: 'center', padding: '40px 0' }}>
          Loading upload details...
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ maxWidth: 800, margin: '40px auto', padding: 24 }}>
        <div style={{ color: '#ef4444', marginBottom: 12 }}>{error}</div>
        <button
          onClick={() => navigate('/uploads')}
          style={{
            background: '#3b82f6',
            color: 'white',
            border: 'none',
            padding: '8px 16px',
            borderRadius: 6,
            cursor: 'pointer',
          }}
        >
          Back to Uploads
        </button>
      </div>
    );
  }

  if (!upload) {
    return (
      <div style={{ maxWidth: 800, margin: '40px auto', padding: 24 }}>
        <div style={{ color: '#ef4444', marginBottom: 12 }}>
          Upload not found.
        </div>
        <button
          onClick={() => navigate('/uploads')}
          style={{
            background: '#3b82f6',
            color: 'white',
            border: 'none',
            padding: '8px 16px',
            borderRadius: 6,
            cursor: 'pointer',
          }}
        >
          Back to Uploads
        </button>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: 800, margin: '40px auto', padding: 24 }}>
      <div style={{ marginBottom: 24 }}>
        <button
          onClick={() => navigate('/uploads')}
          style={{
            background: 'none',
            border: '1px solid #d1d5db',
            padding: '8px 16px',
            borderRadius: 6,
            cursor: 'pointer',
            marginBottom: 16,
            display: 'flex',
            alignItems: 'center',
            gap: 8,
          }}
        >
          ← Back to Uploads
        </button>
        <h1 style={{ fontSize: 32, fontWeight: 700, marginBottom: 8 }}>
          {upload.file_name}
        </h1>
        <div
          style={{
            display: 'flex',
            gap: 16,
            alignItems: 'center',
            marginBottom: 24,
          }}
        >
          <span
            style={{
              background: statusColors[upload.status] || '#e5e7eb',
              color: '#222',
              borderRadius: 6,
              padding: '4px 12px',
              fontWeight: 500,
              fontSize: 14,
            }}
          >
            {upload.status.charAt(0).toUpperCase() + upload.status.slice(1)}
          </span>
          <span style={{ color: '#6b7280' }}>
            Uploaded {new Date(upload.date_uploaded).toLocaleString()}
          </span>
        </div>
      </div>

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: 24,
          marginBottom: 32,
        }}
      >
        <div style={{ background: '#f9fafb', padding: 20, borderRadius: 8 }}>
          <h3 style={{ fontSize: 18, fontWeight: 600, marginBottom: 12 }}>
            File Information
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            <div>
              <strong>File Type:</strong> {upload.file_type.toUpperCase()}
            </div>
            <div>
              <strong>File Size:</strong> {formatFileSize(upload.file_size)}
            </div>
            {upload.file_path && (
              <div>
                <strong>File Path:</strong> {upload.file_path}
              </div>
            )}
            {upload.bucket_name && (
              <div>
                <strong>Bucket:</strong> {upload.bucket_name}
              </div>
            )}
          </div>
        </div>

        <div style={{ background: '#f9fafb', padding: 20, borderRadius: 8 }}>
          <h3 style={{ fontSize: 18, fontWeight: 600, marginBottom: 12 }}>
            Processing Details
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            <div>
              <strong>Status:</strong>{' '}
              {upload.status.charAt(0).toUpperCase() + upload.status.slice(1)}
            </div>
            {upload.task_id && (
              <div>
                <strong>Task ID:</strong> {upload.task_id}
              </div>
            )}
            {upload.uploader && (
              <div>
                <strong>Uploader:</strong> {upload.uploader}
              </div>
            )}
          </div>
        </div>
      </div>

      {upload.status === 'completed' && upload.processed_text && (
        <div
          style={{
            background: '#fff',
            border: '1px solid #e5e7eb',
            borderRadius: 8,
            padding: 24,
          }}
        >
          <h3 style={{ fontSize: 20, fontWeight: 600, marginBottom: 16 }}>
            Extracted Text Content
          </h3>
          <div
            style={{
              background: '#f8fafc',
              border: '1px solid #e2e8f0',
              borderRadius: 6,
              padding: 16,
              whiteSpace: 'pre-wrap',
              fontFamily: 'monospace',
              fontSize: 14,
              lineHeight: 1.5,
              maxHeight: '500px',
              overflowY: 'auto',
            }}
          >
            {upload.processed_text}
          </div>
        </div>
      )}

      {upload.status === 'completed' && !upload.processed_text && (
        <div
          style={{
            background: '#fef3c7',
            border: '1px solid #f59e0b',
            borderRadius: 8,
            padding: 16,
          }}
        >
          <p style={{ color: '#92400e', margin: 0 }}>
            This file has been processed but no text content was extracted. This
            may be normal for certain file types or if the file didn't contain
            extractable text.
          </p>
        </div>
      )}

      {upload.status === 'failed' && (
        <div
          style={{
            background: '#fef2f2',
            border: '1px solid #f87171',
            borderRadius: 8,
            padding: 16,
          }}
        >
          <p style={{ color: '#991b1b', margin: 0 }}>
            This file failed to process. Please try uploading again or contact
            support if the issue persists.
          </p>
        </div>
      )}

      {upload.status === 'processing' && (
        <div
          style={{
            background: '#eff6ff',
            border: '1px solid #60a5fa',
            borderRadius: 8,
            padding: 16,
          }}
        >
          <p style={{ color: '#1e40af', margin: 0 }}>
            This file is currently being processed. Please check back in a few
            moments.
          </p>
        </div>
      )}
    </div>
  );
};

export default UploadDetails;
