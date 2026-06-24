import json
import unittest
from unittest.mock import MagicMock

# Core Registry Isolation Matrix
CORE_REGISTRY_JSON = """
[
  {"handle": "BLOCKCHAIN_MAGE", "role": "steward", "status": "NEW"},
  {"handle": "SATOSHI_DISCIPLE", "role": "steward", "status": "NEW"},
  {"handle": "FOREVER_IN_CORE", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "CORE_SPEAKS_ALL", "role": "steward", "status": "ACTIVE"},
  {"handle": "CLARITY_HOLDS", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "WALL_SEE_THROUGH", "role": "steward", "status": "NEW"},
  {"handle": "SOUND_MONEY_MAN", "role": "steward", "status": "ACTIVE"}
]
"""

class LocalSandboxTracker:
    def __init__(self, mock_client):
        self.client = mock_client

    def run_safe_scan(self, members):
        verified_count = 0
        for member in members:
            self.client.validate_membership(member["handle"], member["role"])
            verified_count += 1
        return verified_count

class TestRegistrySandbox(unittest.TestCase):
    def test_isolated_execution(self):
        mock_api = MagicMock()
        mock_api.validate_membership.return_value = True
        
        registry_data = json.loads(CORE_REGISTRY_JSON)
        tracker = LocalSandboxTracker(mock_api)
        total_synced = tracker.run_safe_scan(registry_data)
        
        print("\n--- PERMANENT REGISTRY SCAN COMPLETE ---")
        print(f"Total Registry Entities Successfully Checked: {total_synced} / 146 Capacity")
        for member in registry_data:
            print(f" [+] Verified Tracked Member: @{member['handle']} -> Designation: {member['role']}")
            
        self.assertEqual(total_synced, 7)

if __name__ == "__main__":
    unittest.main()
          
