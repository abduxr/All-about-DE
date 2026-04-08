# Configure Azure Storage with Service Principal for Spark

## Step 1: Create Service Principal
- In **Microsoft Entra ID**, register a new application (service principal).
- Generate a **client secret** and save it securely.
- Note down:
  - Application (Client) ID
  - Directory (Tenant) ID
  - Client Secret

---

## Step 2: Assign Role in Azure Storage Account
- Go to your **Azure Storage Account**.
- Open **Access Control (IAM)**.
- Add a role assignment:
  - Role: **Storage Blob Data Contributor** (or required role).
  - Member: Select the **Service Principal account** created above.

---

## Step 3: Configure Spark with OAuth
Paste the following configuration into your Spark environment, replacing placeholders with actual values:

```python
spark.conf.set("fs.azure.account.auth.type.<storage-account>.dfs.core.chinacloudapi.cn", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.<storage-account>.dfs.core.chinacloudapi.cn", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.<storage-account>.dfs.core.chinacloudapi.cn", "<application-id>")
spark.conf.set("fs.azure.account.oauth2.client.secret.<storage-account>.dfs.core.chinacloudapi.cn", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.<storage-account>.dfs.core.chinacloudapi.cn", "https://login.chinacloudapi.cn/<directory-id>/oauth2/token")
