# OSCAR EMR Kubernetes Deployment

This Helm chart deploys the OSCAR EMR (Electronic Medical Records) system on Kubernetes.

## Prerequisites

- Kubernetes cluster 1.19+
- Helm 3.0+
- cert-manager (for SSL/TLS certificates)
- nginx-ingress-controller
- Storage class for persistent volumes

## Components

- **MariaDB Database**: StatefulSet with persistent storage
- **OSCAR Web Application**: Deployment with horizontal pod autoscaling
- **Ingress**: SSL/TLS enabled ingress with Let's Encrypt certificates
- **Network Policies**: Security policies for pod-to-pod communication
- **Persistent Volumes**: For documents and logs storage

## Installation

1. **Add the Helm repository** (if using a repository):
   ```bash
   helm repo add oscar-emr https://your-repo-url
   helm repo update
   ```

2. **Install the chart**:
   ```bash
   # Create namespace if it doesn't exist
   kubectl create namespace oscar-emr
   
   # Basic installation
   helm install oscar-emr ./emr/k8s --namespace oscar-emr

   # With custom values
   helm install oscar-emr ./emr/k8s -f custom-values.yaml

   # With specific namespace
   helm install oscar-emr ./emr/k8s --namespace oscar-emr --create-namespace
   ```

3. **Verify the installation**:
   ```bash
   helm status oscar-emr
   kubectl get all -n oscar-emr
   ```

If you need to delete the PVCs:
```bash
kubectl delete pvc oscar-documents-pvc -n oscar-emr
kubectl delete pvc oscar-logs-pvc -n oscar-emr
```

## Configuration

### Values.yaml

The main configuration file contains:

- **Database settings**: MariaDB image, credentials, storage
- **OSCAR application**: Image, replicas, resources, environment variables
- **Ingress configuration**: Host, SSL/TLS, annotations
- **Persistence**: Storage class and size for documents and logs
- **Security**: User/group IDs for containers

### Custom Values

Create a `custom-values.yaml` file to override defaults:

```yaml
namespace: my-oscar-namespace
certManagerEmail: admin@example.com

database:
  credentials:
    rootPassword: my-secure-password
    password: my-oscar-password

oscar:
  image:
    repository: my-registry/oscar-emr
    tag: v1.0.0
  replicas: 3

ingress:
  hosts:
    - host: emr.mycompany.com
      paths:
        - path: /
          pathType: Prefix
```

## Accessing the Application

### Via Ingress (Default)
If ingress is enabled, access the application at:
- `https://emr.arsmedicatech.com` (or your configured host)

### Via Port Forward
```bash
kubectl port-forward -n oscar-emr svc/oscar-web 8080:80
# Then visit http://localhost:8080
```

## Database Access

### Direct Database Connection
```bash
kubectl exec -it -n oscar-emr deployment/oscar-web -- mysql -h oscar-db -u oscar -p
```

### Database Credentials
- Host: `oscar-db.oscar-emr.svc.cluster.local`
- Port: `3306`
- Database: `oscar`
- User: `oscar`
- Password: Stored in `oscar-db-secret`

## Monitoring and Logs

### View Application Logs
```bash
kubectl logs -n oscar-emr -l app=oscar-web
```

### Check Pod Status
```bash
kubectl get pods -n oscar-emr
kubectl describe pod -n oscar-emr <pod-name>
```

### Monitor Resources
```bash
kubectl top pods -n oscar-emr
kubectl get hpa -n oscar-emr
```

## Scaling

The application includes a HorizontalPodAutoscaler that scales based on:
- CPU utilization (target: 70%)
- Memory utilization (target: 80%)

Manual scaling:
```bash
kubectl scale deployment oscar-web -n oscar-emr --replicas=5
```

## Backup and Restore

### Database Backup
```bash
kubectl exec -it -n oscar-emr deployment/oscar-web -- mysqldump -h oscar-db -u oscar -p oscar > backup.sql
```

### Documents Backup
```bash
kubectl cp oscar-emr/oscar-web-pod:/var/lib/OscarDocument ./backup-documents
```

## Troubleshooting

### Common Issues

1. **Database Connection Issues**
   - Check if the database pod is running: `kubectl get pods -n oscar-emr -l app=oscar-db`
   - Verify database credentials in the secret: `kubectl get secret oscar-db-secret -n oscar-emr -o yaml`

2. **Ingress Issues**
   - Check ingress status: `kubectl get ingress -n oscar-emr`
   - Verify cert-manager is working: `kubectl get certificaterequests -n oscar-emr`

3. **Storage Issues**
   - Check PVC status: `kubectl get pvc -n oscar-emr`
   - Verify storage class exists: `kubectl get storageclass`

### Debug Commands

```bash
# Check all resources
kubectl get all -n oscar-emr

# Check events
kubectl get events -n oscar-emr --sort-by='.lastTimestamp'

# Check pod logs
kubectl logs -n oscar-emr -l app=oscar-web --tail=100

# Check database logs
kubectl logs -n oscar-emr -l app=oscar-db --tail=100
```

## Security Considerations

- Database credentials are stored in Kubernetes secrets
- Network policies restrict pod-to-pod communication
- SSL/TLS is enabled for ingress traffic
- Containers run with non-root users
- Persistent volumes are used for data storage

## Upgrading

```bash
# Upgrade to a new version
helm upgrade oscar-emr ./emr/k8s

# Upgrade with custom values
helm upgrade oscar-emr ./emr/k8s -f custom-values.yaml
```

## Uninstalling

```bash
# Remove the deployment
helm uninstall oscar-emr

# Remove persistent volumes (optional)
kubectl delete pvc -n oscar-emr --all
```

## Support

For issues and questions:
- Check the troubleshooting section above
- Review the Helm chart logs: `helm status oscar-emr`
- Check Kubernetes events: `kubectl get events -n oscar-emr` 