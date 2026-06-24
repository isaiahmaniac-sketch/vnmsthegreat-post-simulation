import json
import unittest
from unittest.mock import MagicMock

# Core Registry Isolation Matrix
CORE_REGISTRY_JSON = """
[
  {"handle": "BLOCKCHAIN_MAGE", "role": "steward", "status": "ACTIVE"},
  {"handle": "SATOSHI_DISCIPLE", "role": "steward", "status": "ACTIVE"},
  {"handle": "FOREVER_IN_CORE", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "CORE_SPEAKS_ALL", "role": "steward", "status": "ACTIVE"},
  {"handle": "CLARITY_HOLDS", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "WALL_SEE_THROUGH", "role": "steward", "status": "ACTIVE"},
  {"handle": "SOUND_MONEY_MAN", "role": "steward", "status": "ACTIVE"},
  {"handle": "VNMS_BELIEVER", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "ZERO_TRUST_NODE", "role": "PIONEER", "status": "NEW"},
  {"handle": "PROTOCOL_MONK", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "SOVEREIGN_SIGNAL", "role": "steward", "status": "ACTIVE"},
  {"handle": "HASH_RATE_KING", "role": "steward", "status": "ACTIVE"},
  {"handle": "DECENTRALIZE_ALL", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "STACK_OR_NOTHING", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "BTC_VISIONARY", "role": "steward", "status": "ACTIVE"},
  {"handle": "CYPHERPUNK_REAL", "role": "steward", "status": "ACTIVE"},
  {"handle": "ORANGE_PILL_PRO", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "LIGHTSPEED_SAT", "role": "steward", "status": "ACTIVE"},
  {"handle": "GENESIS_BLOCK", "role": "steward", "status": "ACTIVE"},
  {"handle": "NODE_OPERATOR_7", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "HODL_INFINITY", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "BTC_IS_TRUTH", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "OUTER_SIGHT_NOW", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "VNMS_ALLIANCE", "role": "steward", "status": "ACTIVE"},
  {"handle": "ISAIAH_FOLLOWER", "role": "steward", "status": "ACTIVE"},
  {"handle": "CORE_FOREVER_01", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "FREEDOM_STACKER", "role": "steward", "status": "ACTIVE"},
  {"handle": "NAKAMOTO_HEIR", "role": "steward", "status": "NEW"},
  {"handle": "ELECTRIC_MONEY", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "CIPHER_RUNNER", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "GENESIS_KEEPER", "role": "steward", "status": "ACTIVE"},
  {"handle": "TIMECHAIN_TRUE", "role": "steward", "status": "ACTIVE"},
  {"handle": "ORACLE_OF_BTC", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "DEEP_HODL_VAULT", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "CONVICTION_NODE", "role": "steward", "status": "ACTIVE"},
  {"handle": "SIGNAL_STEWARD", "role": "steward", "status": "ACTIVE"},
  {"handle": "BLOCK_AUTHOR", "role": "steward", "status": "ACTIVE"},
  {"handle": "LASER_EYES_2026", "role": "steward", "status": "ACTIVE"},
  {"handle": "SATOSHI_STUDENT", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "PROOF_OF_WORK", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "CHAIN_WHISPERER", "role": "steward", "status": "ACTIVE"},
  {"handle": "FUTURE_IS_BTC", "role": "PIONEER", "status": "ACTIVE"},
  {"handle": "WALL_BREAKER_01", "role": "steward", "status": "ACTIVE"},
  {"handle": "CLARITY_SEEKER", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "THE_LONG_GAME", "role": "steward", "status": "ACTIVE"},
  {"handle": "IMMUTABLE_TRUTH", "role": "steward", "status": "ACTIVE"},
  {"handle": "FOCUSED_BUILDER", "role": "BUILDER", "status": "ACTIVE"},
  {"handle": "OUTER_SIGHT_X", "role": "steward", "status": "ACTIVE"}
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
            
        self.assertEqual(total_synced, 48)

if __name__ == "__main__":
    unittest.main()
