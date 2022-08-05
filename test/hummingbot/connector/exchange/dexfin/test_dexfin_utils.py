import unittest

from hummingbot.connector.exchange.dexfin import dexfin_utils as utils


class DexfinUtilTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.base_asset = "COINALPHA"
        cls.quote_asset = "HBOT"
        cls.trading_pair = f"{cls.base_asset}-{cls.quote_asset}"
        cls.hb_trading_pair = f"{cls.base_asset}-{cls.quote_asset}"
        cls.ex_trading_pair = f"{cls.base_asset}{cls.quote_asset}"

    def test_is_exchange_information_valid(self):
        invalid_info_1 = {
            "state": "disabled"
        }
        self.assertFalse(utils.is_exchange_information_valid(invalid_info_1))

        invalid_info_2 = {
            "state": None
        }
        self.assertFalse(utils.is_exchange_information_valid(invalid_info_2))

        invalid_info_3 = {
            "state": ""
        }
        self.assertFalse(utils.is_exchange_information_valid(invalid_info_3))

        invalid_info_4 = {}
        self.assertFalse(utils.is_exchange_information_valid(invalid_info_4))

        valid_info = {
            "state": "enabled"
        }

        self.assertTrue(utils.is_exchange_information_valid(valid_info))
