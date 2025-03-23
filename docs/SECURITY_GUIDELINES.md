### 3. `SECURITY_GUIDELINES.md`
# Security Best Practices

## RBAC Implementation
| Role            | Permissions                          |
|-----------------|--------------------------------------|
| Admin           | Full system access                   |
| Data Scientist  | Submit jobs, read results            |
| Viewer          | Read-only monitoring                 |

```python
# Example FastAPI RBAC
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials

async def get_admin_user(
    creds: HTTPAuthorizationCredentials = Security(security)
) -> User:
    if "admin" not in creds.claims["roles"]:
        raise HTTPException(status_code=403)
    return user
```

## Secrets Management
1. **Never Commit Secrets**
   ```bash
   # .gitignore
   config/secrets.yaml
   ```
2. **Use Environment Variables**
   ```dockerfile
   ENV DB_PASSWORD=$SECRET_DB_PASSWORD
   ```
3. **Encrypt Sensitive Data**
   ```python
   from cryptography.fernet import Fernet
   cipher = Fernnet(os.getenv("ENCRYPTION_KEY"))
   ```
4. **Rotation Policy**
   - API Tokens: 90 days
   - Database Creds: 180 days

## Infrastructure Security
- **Kubernetes**: 
  ```yaml
  # pod-security-policy.yaml
  allowPrivilegeEscalation: false
  runAsNonRoot: true
  ```
- **Network Policies**:
  ```yaml
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
  ```

## Audit Tools
- [Vault](https://www.vaultproject.io/) for secret management
- [Falco](https://falco.org/) for runtime security
- [OPA](https://www.openpolicyagent.org/) for policy enforcement
```