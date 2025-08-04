import vertexai
from google.cloud import aiplatform
import google.auth
import os

# --- EDIT THESE TWO LINES ---
# Replace with your project ID (e.g., 'my-gcp-project')
PROJECT_ID = "arched-curve-464100-c9"

# Replace with your project region (e.g., 'us-central1')
REGION = 'us-central1'
# ---------------------------

def test_vertex_ai_auth():
    """Tests Vertex AI authentication by initializing the client and listing endpoints."""
    
    if PROJECT_ID == 'your-project-id':
        print("Please edit the 'PROJECT_ID' variable in the script with your actual project ID.")
        return

    try:
        # A simple test to check authentication
        credentials, _ = google.auth.default()
        
        # Initialize Vertex AI with your project ID and region
        vertexai.init(project=PROJECT_ID, location=REGION)
        
        # A stable test: use a core method to list endpoints
        # This confirms that both authentication and API permissions are working
        endpoints = aiplatform.Endpoint.list()
        
        print(f"\n✅ Success! Vertex AI client initialized for project: {PROJECT_ID}")
        print(f"   Found {len(endpoints)} endpoints in your project.")
        
    except Exception as e:
        print("\n❌ Initialization or Authentication FAILED")
        print(f"   Error: {e}")
        print("\nPossible solutions:")
        print("1. **Authentication Error:** Have you run `gcloud auth application-default login`?")
        print("2. **API Not Enabled:** Is the Vertex AI API enabled for your project?")
        print("3. **Incorrect Project/Region:** Are the `PROJECT_ID` and `REGION` in the script correct?")
        
# Run the test
if __name__ == "__main__":
    test_vertex_ai_auth()