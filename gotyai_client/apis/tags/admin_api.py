# coding: utf-8

"""
    Gotyai API v3

    Gotyai API : the Spartan explainable AI   # noqa: E501

    The version of the OpenAPI document: 3.0.2
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""

from gotyai_client.paths.api2_json_name_blacklist_patterns.get import AbuseNamePatterns
from gotyai_client.paths.api2_json_add_credits_api_key_usage_credits_user_message.get import AddCredits
from gotyai_client.paths.api2_json_api_key_info.get import ApiKeyInfo
from gotyai_client.paths.api2_json_api_usage.get import ApiUsage
from gotyai_client.paths.api2_json_api_usage_history.get import ApiUsageHistory
from gotyai_client.paths.api2_json_api_usage_history_aggregate.get import ApiUsageHistoryAggregate
from gotyai_client.paths.api2_json_available_plans.get import AvailablePlans
from gotyai_client.paths.api2_json_available_plans_token.get import AvailablePlans1
from gotyai_client.paths.api2_json_billing_currencies.get import BillingCurrencies
from gotyai_client.paths.api2_json_billing_history_token.get import BillingHistory
from gotyai_client.paths.api2_json_billing_info_token.get import BillingInfo
from gotyai_client.paths.api2_json_charge_new_stripe_token_stripe_email.get import ChargeNew
from gotyai_client.paths.api2_json_corporate_key_api_key_corporate.get import CorporateKey
from gotyai_client.paths.api2_json_count_spam_non_spam_duration_millis.get import CountSpamNonSpam
from gotyai_client.paths.api2_json_count_spam_non_spam.get import CountSpamNonSpam1
from gotyai_client.paths.api2_json_debug_level_logger_level.get import DebugLevel
from gotyai_client.paths.api2_json_disable_source_disabled.get import Disable
from gotyai_client.paths.api2_json_email_blacklist_pattern_add_pattern.get import EmailBlacklistPatternAdd
from gotyai_client.paths.api2_json_email_blacklist_pattern_remove_pattern.get import EmailBlacklistPatternRemove
from gotyai_client.paths.api2_json_email_blacklist_patterns.get import EmailBlacklistPatterns
from gotyai_client.paths.api2_json_explainability_source_explainable.get import Explainability
from gotyai_client.paths.api2_json_flush.get import Flush
from gotyai_client.paths.api2_json_namsor_counter.get import GotyaCounter
from gotyai_client.paths.api2_json_invalidate_cache.get import InvalidateCache
from gotyai_client.paths.api2_json_ip_addresses_blacklist_candidates.get import IpAddressesBlacklistCandidates
from gotyai_client.paths.api2_json_name_blacklist_pattern_add_pattern.get import NameBlacklistPatternAdd
from gotyai_client.paths.api2_json_name_blacklist_pattern_remove_pattern.get import NameBlacklistPatternRemove
from gotyai_client.paths.api2_json_payment_info_token.get import PaymentInfo
from gotyai_client.paths.api2_json_procure_key_token_recaptchav2.get import ProcureKey
from gotyai_client.paths.api2_json_procure_key_token.get import ProcureKey1
from gotyai_client.paths.api2_json_remove_payment_source_id_token.get import RemovePayment
from gotyai_client.paths.api2_json_remove_user_account_token.get import RemoveUserAccount
from gotyai_client.paths.api2_json_remove_user_account_on_behalf_api_key.get import RemoveUserAccountOnBehalf
from gotyai_client.paths.api2_json_resend_key_token_recaptchav2.get import ResendKey
from gotyai_client.paths.api2_json_retrieve_key_token.get import RetrieveKey
from gotyai_client.paths.api2_json_shutdown.get import Shutdown
from gotyai_client.paths.api2_json_signups_ip_address.get import Signups
from gotyai_client.paths.api2_json_software_version.get import SoftwareVersion
from gotyai_client.paths.api2_json_spamsurge_block_disposable_emails.get import Spamsurge
from gotyai_client.paths.api2_json_stats.get import Stats
from gotyai_client.paths.api2_json_subscribe_plan_plan_name_token.get import SubscribePlan
from gotyai_client.paths.api2_json_subscribe_plan_on_behalf_plan_name_api_key.get import SubscribePlanOnBehalf
from gotyai_client.paths.api2_json_switch_default_api_key_active_default_blocked.get import SwitchDefaultApiKeyActive
from gotyai_client.paths.api2_json_update_billing_info_token.post import UpdateBillingInfo
from gotyai_client.paths.api2_json_update_limit_usage_limit_hard_or_soft_token.get import UpdateLimit
from gotyai_client.paths.api2_json_update_payment_default_defaut_source_id_token.get import UpdatePaymentDefault
from gotyai_client.paths.api2_json_update_user_info_email_display_name_token.get import UpdateUserInfo
from gotyai_client.paths.api2_json_user_info_token.get import UserInfo
from gotyai_client.paths.api2_json_verify_email_email_token.get import VerifyEmail
from gotyai_client.paths.api2_json_verify_remove_email_email_token.get import VerifyRemoveEmail


class AdminApi(
    AbuseNamePatterns,
    AddCredits,
    ApiKeyInfo,
    ApiUsage,
    ApiUsageHistory,
    ApiUsageHistoryAggregate,
    AvailablePlans,
    AvailablePlans1,
    BillingCurrencies,
    BillingHistory,
    BillingInfo,
    ChargeNew,
    CorporateKey,
    CountSpamNonSpam,
    CountSpamNonSpam1,
    DebugLevel,
    Disable,
    EmailBlacklistPatternAdd,
    EmailBlacklistPatternRemove,
    EmailBlacklistPatterns,
    Explainability,
    Flush,
    GotyaCounter,
    InvalidateCache,
    IpAddressesBlacklistCandidates,
    NameBlacklistPatternAdd,
    NameBlacklistPatternRemove,
    PaymentInfo,
    ProcureKey,
    ProcureKey1,
    RemovePayment,
    RemoveUserAccount,
    RemoveUserAccountOnBehalf,
    ResendKey,
    RetrieveKey,
    Shutdown,
    Signups,
    SoftwareVersion,
    Spamsurge,
    Stats,
    SubscribePlan,
    SubscribePlanOnBehalf,
    SwitchDefaultApiKeyActive,
    UpdateBillingInfo,
    UpdateLimit,
    UpdatePaymentDefault,
    UpdateUserInfo,
    UserInfo,
    VerifyEmail,
    VerifyRemoveEmail,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
