import React, { useCallback, useEffect, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { useNavigate } from 'react-router-dom';
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
}

const statusColors: Record<string, string> = {
  pending: '#fbbf24', // amber
  processing: '#60a5fa', // blue
  completed: '#22c55e', // green
  failed: '#ef4444', // red
  cancelled: '#a1a1aa', // gray
};

const FileUpload: React.FC = () => {
  const [uploads, setUploads] = useState<Upload[]>([]);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const navigate = useNavigate();

  // Fetch uploads list
  const fetchUploads = useCallback(async () => {
    try {
      const res = await fileUploadAPI.getAll();
      setUploads(res);
    } catch (err) {
      setError('Failed to fetch uploads.');
    }
  }, []);

  useEffect(() => {
    fetchUploads();
    const interval = setInterval(fetchUploads, 4000); // auto-refresh every 4s
    return () => clearInterval(interval);
  }, [fetchUploads]);

  // Handle file drop
  const onDrop = useCallback(
    async (acceptedFiles: File[]) => {
      setError(null);
      setSuccess(null);
      if (!acceptedFiles.length) return;
      setUploading(true);
      const file = acceptedFiles[0];
      const formData = new FormData();
      formData.append('file', file);
      try {
        const res = await fileUploadAPI.create(formData);
        logger.debug('File uploaded successfully:', res);
        setSuccess('File uploaded!');
        fetchUploads();
      } catch (err: any) {
        setError(err?.response?.data?.error || 'Upload failed.');
      } finally {
        setUploading(false);
      }
    },
    [fetchUploads]
  );

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    multiple: false,
  });

  const handleUploadClick = (upload: Upload) => {
    if (upload.status === 'completed') {
      navigate(`/uploads/${upload.id}`);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: '40px auto', padding: 24 }}>
      <h2 style={{ fontSize: 28, fontWeight: 700, marginBottom: 24 }}>
        File Upload
      </h2>
      <div
        {...getRootProps()}
        style={{
          border: '2px dashed #888',
          borderRadius: 12,
          padding: 40,
          textAlign: 'center',
          background: isDragActive ? '#f0f9ff' : '#fafafa',
          color: '#333',
          cursor: 'pointer',
          marginBottom: 24,
          transition: 'background 0.2s',
        }}
      >
        <input {...getInputProps()} />
        {isDragActive ? (
          <p>Drop the file here ...</p>
        ) : (
          <p>Drag & drop a file here, or click to select</p>
        )}
        {uploading && (
          <p style={{ color: '#60a5fa', marginTop: 8 }}>Uploading...</p>
        )}
      </div>
      {error && (
        <div style={{ color: '#ef4444', marginBottom: 12 }}>{error}</div>
      )}
      {success && (
        <div style={{ color: '#22c55e', marginBottom: 12 }}>{success}</div>
      )}
      <h3 style={{ fontSize: 20, fontWeight: 600, margin: '24px 0 12px' }}>
        Your Uploads
      </h3>
      <div
        style={{
          border: '1px solid #e5e7eb',
          borderRadius: 8,
          background: '#fff',
        }}
      >
        {uploads.length === 0 ? (
          <div style={{ padding: 24, color: '#888' }}>No uploads yet.</div>
        ) : (
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead>
              <tr style={{ background: '#f3f4f6' }}>
                <th style={{ padding: 10, textAlign: 'left', fontWeight: 500 }}>
                  File
                </th>
                <th style={{ padding: 10, textAlign: 'left', fontWeight: 500 }}>
                  Type
                </th>
                <th style={{ padding: 10, textAlign: 'left', fontWeight: 500 }}>
                  Uploaded
                </th>
                <th style={{ padding: 10, textAlign: 'left', fontWeight: 500 }}>
                  Status
                </th>
              </tr>
            </thead>
            <tbody>
              {uploads.map(u => (
                <tr
                  key={u.id}
                  style={{
                    borderBottom: '1px solid #f1f5f9',
                    cursor: u.status === 'completed' ? 'pointer' : 'default',
                    backgroundColor:
                      u.status === 'completed' ? '#f8fafc' : 'transparent',
                    transition: 'background-color 0.2s',
                  }}
                  onClick={() => handleUploadClick(u)}
                  onMouseEnter={e => {
                    if (u.status === 'completed') {
                      e.currentTarget.style.backgroundColor = '#e2e8f0';
                    }
                  }}
                  onMouseLeave={e => {
                    if (u.status === 'completed') {
                      e.currentTarget.style.backgroundColor = '#f8fafc';
                    }
                  }}
                >
                  <td style={{ padding: 10 }}>{u.file_name}</td>
                  <td style={{ padding: 10 }}>{u.file_type}</td>
                  <td style={{ padding: 10 }}>
                    {new Date(u.date_uploaded).toLocaleString()}
                  </td>
                  <td style={{ padding: 10 }}>
                    <span
                      style={{
                        background: statusColors[u.status] || '#e5e7eb',
                        color: '#222',
                        borderRadius: 6,
                        padding: '2px 10px',
                        fontWeight: 500,
                        fontSize: 14,
                      }}
                    >
                      {u.status.charAt(0).toUpperCase() + u.status.slice(1)}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};

export default FileUpload;
