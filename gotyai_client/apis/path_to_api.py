import typing_extensions

from gotyai_client.paths import PathValues
from gotyai_client.apis.paths.api2_json_shutdown import Api2JsonShutdown
from gotyai_client.apis.paths.api2_json_flush import Api2JsonFlush
from gotyai_client.apis.paths.api2_json_user_info_token import Api2JsonUserInfoToken
from gotyai_client.apis.paths.api2_json_fit_one_classifier_uuid import Api2JsonFitOneClassifierUuid
from gotyai_client.apis.paths.api2_json_predict_many_classifier_uuid import Api2JsonPredictManyClassifierUuid
from gotyai_client.apis.paths.api2_json_explain_one_classifier_uuid import Api2JsonExplainOneClassifierUuid
from gotyai_client.apis.paths.api2_json_explain_many_classifier_uuid import Api2JsonExplainManyClassifierUuid
from gotyai_client.apis.paths.api2_json_fit_many_classifier_uuid import Api2JsonFitManyClassifierUuid
from gotyai_client.apis.paths.api2_json_predict_one_classifier_uuid import Api2JsonPredictOneClassifierUuid
from gotyai_client.apis.paths.api2_json_disable_source_disabled import Api2JsonDisableSourceDisabled
from gotyai_client.apis.paths.api2_json_billing_history_token import Api2JsonBillingHistoryToken
from gotyai_client.apis.paths.api2_json_retrieve_key_token import Api2JsonRetrieveKeyToken
from gotyai_client.apis.paths.api2_json_procure_key_token_recaptchav2 import Api2JsonProcureKeyTokenRecaptchav2
from gotyai_client.apis.paths.api2_json_procure_key_token import Api2JsonProcureKeyToken
from gotyai_client.apis.paths.api2_json_resend_key_token_recaptchav2 import Api2JsonResendKeyTokenRecaptchav2
from gotyai_client.apis.paths.api2_json_available_plans import Api2JsonAvailablePlans
from gotyai_client.apis.paths.api2_json_available_plans_token import Api2JsonAvailablePlansToken
from gotyai_client.apis.paths.api2_json_subscribe_plan_plan_name_token import Api2JsonSubscribePlanPlanNameToken
from gotyai_client.apis.paths.api2_json_subscribe_plan_on_behalf_plan_name_api_key import Api2JsonSubscribePlanOnBehalfPlanNameApiKey
from gotyai_client.apis.paths.api2_json_remove_user_account_token import Api2JsonRemoveUserAccountToken
from gotyai_client.apis.paths.api2_json_remove_user_account_on_behalf_api_key import Api2JsonRemoveUserAccountOnBehalfApiKey
from gotyai_client.apis.paths.api2_json_update_limit_usage_limit_hard_or_soft_token import Api2JsonUpdateLimitUsageLimitHardOrSoftToken
from gotyai_client.apis.paths.api2_json_billing_info_token import Api2JsonBillingInfoToken
from gotyai_client.apis.paths.api2_json_update_user_info_email_display_name_token import Api2JsonUpdateUserInfoEmailDisplayNameToken
from gotyai_client.apis.paths.api2_json_update_billing_info_token import Api2JsonUpdateBillingInfoToken
from gotyai_client.apis.paths.api2_json_ip_addresses_blacklist_candidates import Api2JsonIpAddressesBlacklistCandidates
from gotyai_client.apis.paths.api2_json_email_blacklist_patterns import Api2JsonEmailBlacklistPatterns
from gotyai_client.apis.paths.api2_json_charge_new_stripe_token_stripe_email import Api2JsonChargeNewStripeTokenStripeEmail
from gotyai_client.apis.paths.api2_json_payment_info_token import Api2JsonPaymentInfoToken
from gotyai_client.apis.paths.api2_json_update_payment_default_defaut_source_id_token import Api2JsonUpdatePaymentDefaultDefautSourceIdToken
from gotyai_client.apis.paths.api2_json_remove_payment_source_id_token import Api2JsonRemovePaymentSourceIdToken
from gotyai_client.apis.paths.api2_json_software_version import Api2JsonSoftwareVersion
from gotyai_client.apis.paths.api2_json_namsor_counter import Api2JsonNamsorCounter
from gotyai_client.apis.paths.api2_json_billing_currencies import Api2JsonBillingCurrencies
from gotyai_client.apis.paths.api2_json_verify_email_email_token import Api2JsonVerifyEmailEmailToken
from gotyai_client.apis.paths.api2_json_verify_remove_email_email_token import Api2JsonVerifyRemoveEmailEmailToken
from gotyai_client.apis.paths.api2_json_stats import Api2JsonStats
from gotyai_client.apis.paths.api2_json_api_usage import Api2JsonApiUsage
from gotyai_client.apis.paths.api2_json_api_usage_history import Api2JsonApiUsageHistory
from gotyai_client.apis.paths.api2_json_api_usage_history_aggregate import Api2JsonApiUsageHistoryAggregate
from gotyai_client.apis.paths.api2_json_add_credits_api_key_usage_credits_user_message import Api2JsonAddCreditsApiKeyUsageCreditsUserMessage
from gotyai_client.apis.paths.api2_json_invalidate_cache import Api2JsonInvalidateCache
from gotyai_client.apis.paths.api2_json_debug_level_logger_level import Api2JsonDebugLevelLoggerLevel
from gotyai_client.apis.paths.api2_json_api_key_info import Api2JsonApiKeyInfo
from gotyai_client.apis.paths.api2_json_explainability_source_explainable import Api2JsonExplainabilitySourceExplainable
from gotyai_client.apis.paths.api2_json_switch_default_api_key_active_default_blocked import Api2JsonSwitchDefaultAPIKeyActiveDefaultBlocked
from gotyai_client.apis.paths.api2_json_email_blacklist_pattern_add_pattern import Api2JsonEmailBlacklistPatternAddPattern
from gotyai_client.apis.paths.api2_json_email_blacklist_pattern_remove_pattern import Api2JsonEmailBlacklistPatternRemovePattern
from gotyai_client.apis.paths.api2_json_count_spam_non_spam_duration_millis import Api2JsonCountSpamNonSpamDurationMillis
from gotyai_client.apis.paths.api2_json_count_spam_non_spam import Api2JsonCountSpamNonSpam
from gotyai_client.apis.paths.api2_json_name_blacklist_pattern_add_pattern import Api2JsonNameBlacklistPatternAddPattern
from gotyai_client.apis.paths.api2_json_name_blacklist_pattern_remove_pattern import Api2JsonNameBlacklistPatternRemovePattern
from gotyai_client.apis.paths.api2_json_name_blacklist_patterns import Api2JsonNameBlacklistPatterns
from gotyai_client.apis.paths.api2_json_signups_ip_address import Api2JsonSignupsIpAddress
from gotyai_client.apis.paths.api2_json_corporate_key_api_key_corporate import Api2JsonCorporateKeyApiKeyCorporate
from gotyai_client.apis.paths.api2_json_spamsurge_block_disposable_emails import Api2JsonSpamsurgeBlockDisposableEmails
from gotyai_client.apis.paths.api2_json_multinomial_create import Api2JsonMultinomialCreate
from gotyai_client.apis.paths.api2_json_multinomial_classifier_name import Api2JsonMultinomialClassifierName
from gotyai_client.apis.paths.api2_json_multinomial import Api2JsonMultinomial

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API2_JSON_SHUTDOWN: Api2JsonShutdown,
        PathValues.API2_JSON_FLUSH: Api2JsonFlush,
        PathValues.API2_JSON_USER_INFO_TOKEN: Api2JsonUserInfoToken,
        PathValues.API2_JSON_FIT_ONE_CLASSIFIER_UUID: Api2JsonFitOneClassifierUuid,
        PathValues.API2_JSON_PREDICT_MANY_CLASSIFIER_UUID: Api2JsonPredictManyClassifierUuid,
        PathValues.API2_JSON_EXPLAIN_ONE_CLASSIFIER_UUID: Api2JsonExplainOneClassifierUuid,
        PathValues.API2_JSON_EXPLAIN_MANY_CLASSIFIER_UUID: Api2JsonExplainManyClassifierUuid,
        PathValues.API2_JSON_FIT_MANY_CLASSIFIER_UUID: Api2JsonFitManyClassifierUuid,
        PathValues.API2_JSON_PREDICT_ONE_CLASSIFIER_UUID: Api2JsonPredictOneClassifierUuid,
        PathValues.API2_JSON_DISABLE_SOURCE_DISABLED: Api2JsonDisableSourceDisabled,
        PathValues.API2_JSON_BILLING_HISTORY_TOKEN: Api2JsonBillingHistoryToken,
        PathValues.API2_JSON_RETRIEVE_KEY_TOKEN: Api2JsonRetrieveKeyToken,
        PathValues.API2_JSON_PROCURE_KEY_TOKEN_RECAPTCHAV2: Api2JsonProcureKeyTokenRecaptchav2,
        PathValues.API2_JSON_PROCURE_KEY_TOKEN: Api2JsonProcureKeyToken,
        PathValues.API2_JSON_RESEND_KEY_TOKEN_RECAPTCHAV2: Api2JsonResendKeyTokenRecaptchav2,
        PathValues.API2_JSON_AVAILABLE_PLANS: Api2JsonAvailablePlans,
        PathValues.API2_JSON_AVAILABLE_PLANS_TOKEN: Api2JsonAvailablePlansToken,
        PathValues.API2_JSON_SUBSCRIBE_PLAN_PLAN_NAME_TOKEN: Api2JsonSubscribePlanPlanNameToken,
        PathValues.API2_JSON_SUBSCRIBE_PLAN_ON_BEHALF_PLAN_NAME_API_KEY: Api2JsonSubscribePlanOnBehalfPlanNameApiKey,
        PathValues.API2_JSON_REMOVE_USER_ACCOUNT_TOKEN: Api2JsonRemoveUserAccountToken,
        PathValues.API2_JSON_REMOVE_USER_ACCOUNT_ON_BEHALF_API_KEY: Api2JsonRemoveUserAccountOnBehalfApiKey,
        PathValues.API2_JSON_UPDATE_LIMIT_USAGE_LIMIT_HARD_OR_SOFT_TOKEN: Api2JsonUpdateLimitUsageLimitHardOrSoftToken,
        PathValues.API2_JSON_BILLING_INFO_TOKEN: Api2JsonBillingInfoToken,
        PathValues.API2_JSON_UPDATE_USER_INFO_EMAIL_DISPLAY_NAME_TOKEN: Api2JsonUpdateUserInfoEmailDisplayNameToken,
        PathValues.API2_JSON_UPDATE_BILLING_INFO_TOKEN: Api2JsonUpdateBillingInfoToken,
        PathValues.API2_JSON_IP_ADDRESSES_BLACKLIST_CANDIDATES: Api2JsonIpAddressesBlacklistCandidates,
        PathValues.API2_JSON_EMAIL_BLACKLIST_PATTERNS: Api2JsonEmailBlacklistPatterns,
        PathValues.API2_JSON_CHARGE_NEW_STRIPE_TOKEN_STRIPE_EMAIL: Api2JsonChargeNewStripeTokenStripeEmail,
        PathValues.API2_JSON_PAYMENT_INFO_TOKEN: Api2JsonPaymentInfoToken,
        PathValues.API2_JSON_UPDATE_PAYMENT_DEFAULT_DEFAUT_SOURCE_ID_TOKEN: Api2JsonUpdatePaymentDefaultDefautSourceIdToken,
        PathValues.API2_JSON_REMOVE_PAYMENT_SOURCE_ID_TOKEN: Api2JsonRemovePaymentSourceIdToken,
        PathValues.API2_JSON_SOFTWARE_VERSION: Api2JsonSoftwareVersion,
        PathValues.API2_JSON_NAMSOR_COUNTER: Api2JsonNamsorCounter,
        PathValues.API2_JSON_BILLING_CURRENCIES: Api2JsonBillingCurrencies,
        PathValues.API2_JSON_VERIFY_EMAIL_EMAIL_TOKEN: Api2JsonVerifyEmailEmailToken,
        PathValues.API2_JSON_VERIFY_REMOVE_EMAIL_EMAIL_TOKEN: Api2JsonVerifyRemoveEmailEmailToken,
        PathValues.API2_JSON_STATS: Api2JsonStats,
        PathValues.API2_JSON_API_USAGE: Api2JsonApiUsage,
        PathValues.API2_JSON_API_USAGE_HISTORY: Api2JsonApiUsageHistory,
        PathValues.API2_JSON_API_USAGE_HISTORY_AGGREGATE: Api2JsonApiUsageHistoryAggregate,
        PathValues.API2_JSON_ADD_CREDITS_API_KEY_USAGE_CREDITS_USER_MESSAGE: Api2JsonAddCreditsApiKeyUsageCreditsUserMessage,
        PathValues.API2_JSON_INVALIDATE_CACHE: Api2JsonInvalidateCache,
        PathValues.API2_JSON_DEBUG_LEVEL_LOGGER_LEVEL: Api2JsonDebugLevelLoggerLevel,
        PathValues.API2_JSON_API_KEY_INFO: Api2JsonApiKeyInfo,
        PathValues.API2_JSON_EXPLAINABILITY_SOURCE_EXPLAINABLE: Api2JsonExplainabilitySourceExplainable,
        PathValues.API2_JSON_SWITCH_DEFAULT_APIKEY_ACTIVE_DEFAULT_BLOCKED: Api2JsonSwitchDefaultAPIKeyActiveDefaultBlocked,
        PathValues.API2_JSON_EMAIL_BLACKLIST_PATTERN_ADD_PATTERN: Api2JsonEmailBlacklistPatternAddPattern,
        PathValues.API2_JSON_EMAIL_BLACKLIST_PATTERN_REMOVE_PATTERN: Api2JsonEmailBlacklistPatternRemovePattern,
        PathValues.API2_JSON_COUNT_SPAM_NON_SPAM_DURATION_MILLIS: Api2JsonCountSpamNonSpamDurationMillis,
        PathValues.API2_JSON_COUNT_SPAM_NON_SPAM: Api2JsonCountSpamNonSpam,
        PathValues.API2_JSON_NAME_BLACKLIST_PATTERN_ADD_PATTERN: Api2JsonNameBlacklistPatternAddPattern,
        PathValues.API2_JSON_NAME_BLACKLIST_PATTERN_REMOVE_PATTERN: Api2JsonNameBlacklistPatternRemovePattern,
        PathValues.API2_JSON_NAME_BLACKLIST_PATTERNS: Api2JsonNameBlacklistPatterns,
        PathValues.API2_JSON_SIGNUPS_IP_ADDRESS: Api2JsonSignupsIpAddress,
        PathValues.API2_JSON_CORPORATE_KEY_API_KEY_CORPORATE: Api2JsonCorporateKeyApiKeyCorporate,
        PathValues.API2_JSON_SPAMSURGE_BLOCK_DISPOSABLE_EMAILS: Api2JsonSpamsurgeBlockDisposableEmails,
        PathValues.API2_JSON_MULTINOMIAL_CREATE: Api2JsonMultinomialCreate,
        PathValues.API2_JSON_MULTINOMIAL_CLASSIFIER_NAME: Api2JsonMultinomialClassifierName,
        PathValues.API2_JSON_MULTINOMIAL: Api2JsonMultinomial,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API2_JSON_SHUTDOWN: Api2JsonShutdown,
        PathValues.API2_JSON_FLUSH: Api2JsonFlush,
        PathValues.API2_JSON_USER_INFO_TOKEN: Api2JsonUserInfoToken,
        PathValues.API2_JSON_FIT_ONE_CLASSIFIER_UUID: Api2JsonFitOneClassifierUuid,
        PathValues.API2_JSON_PREDICT_MANY_CLASSIFIER_UUID: Api2JsonPredictManyClassifierUuid,
        PathValues.API2_JSON_EXPLAIN_ONE_CLASSIFIER_UUID: Api2JsonExplainOneClassifierUuid,
        PathValues.API2_JSON_EXPLAIN_MANY_CLASSIFIER_UUID: Api2JsonExplainManyClassifierUuid,
        PathValues.API2_JSON_FIT_MANY_CLASSIFIER_UUID: Api2JsonFitManyClassifierUuid,
        PathValues.API2_JSON_PREDICT_ONE_CLASSIFIER_UUID: Api2JsonPredictOneClassifierUuid,
        PathValues.API2_JSON_DISABLE_SOURCE_DISABLED: Api2JsonDisableSourceDisabled,
        PathValues.API2_JSON_BILLING_HISTORY_TOKEN: Api2JsonBillingHistoryToken,
        PathValues.API2_JSON_RETRIEVE_KEY_TOKEN: Api2JsonRetrieveKeyToken,
        PathValues.API2_JSON_PROCURE_KEY_TOKEN_RECAPTCHAV2: Api2JsonProcureKeyTokenRecaptchav2,
        PathValues.API2_JSON_PROCURE_KEY_TOKEN: Api2JsonProcureKeyToken,
        PathValues.API2_JSON_RESEND_KEY_TOKEN_RECAPTCHAV2: Api2JsonResendKeyTokenRecaptchav2,
        PathValues.API2_JSON_AVAILABLE_PLANS: Api2JsonAvailablePlans,
        PathValues.API2_JSON_AVAILABLE_PLANS_TOKEN: Api2JsonAvailablePlansToken,
        PathValues.API2_JSON_SUBSCRIBE_PLAN_PLAN_NAME_TOKEN: Api2JsonSubscribePlanPlanNameToken,
        PathValues.API2_JSON_SUBSCRIBE_PLAN_ON_BEHALF_PLAN_NAME_API_KEY: Api2JsonSubscribePlanOnBehalfPlanNameApiKey,
        PathValues.API2_JSON_REMOVE_USER_ACCOUNT_TOKEN: Api2JsonRemoveUserAccountToken,
        PathValues.API2_JSON_REMOVE_USER_ACCOUNT_ON_BEHALF_API_KEY: Api2JsonRemoveUserAccountOnBehalfApiKey,
        PathValues.API2_JSON_UPDATE_LIMIT_USAGE_LIMIT_HARD_OR_SOFT_TOKEN: Api2JsonUpdateLimitUsageLimitHardOrSoftToken,
        PathValues.API2_JSON_BILLING_INFO_TOKEN: Api2JsonBillingInfoToken,
        PathValues.API2_JSON_UPDATE_USER_INFO_EMAIL_DISPLAY_NAME_TOKEN: Api2JsonUpdateUserInfoEmailDisplayNameToken,
        PathValues.API2_JSON_UPDATE_BILLING_INFO_TOKEN: Api2JsonUpdateBillingInfoToken,
        PathValues.API2_JSON_IP_ADDRESSES_BLACKLIST_CANDIDATES: Api2JsonIpAddressesBlacklistCandidates,
        PathValues.API2_JSON_EMAIL_BLACKLIST_PATTERNS: Api2JsonEmailBlacklistPatterns,
        PathValues.API2_JSON_CHARGE_NEW_STRIPE_TOKEN_STRIPE_EMAIL: Api2JsonChargeNewStripeTokenStripeEmail,
        PathValues.API2_JSON_PAYMENT_INFO_TOKEN: Api2JsonPaymentInfoToken,
        PathValues.API2_JSON_UPDATE_PAYMENT_DEFAULT_DEFAUT_SOURCE_ID_TOKEN: Api2JsonUpdatePaymentDefaultDefautSourceIdToken,
        PathValues.API2_JSON_REMOVE_PAYMENT_SOURCE_ID_TOKEN: Api2JsonRemovePaymentSourceIdToken,
        PathValues.API2_JSON_SOFTWARE_VERSION: Api2JsonSoftwareVersion,
        PathValues.API2_JSON_NAMSOR_COUNTER: Api2JsonNamsorCounter,
        PathValues.API2_JSON_BILLING_CURRENCIES: Api2JsonBillingCurrencies,
        PathValues.API2_JSON_VERIFY_EMAIL_EMAIL_TOKEN: Api2JsonVerifyEmailEmailToken,
        PathValues.API2_JSON_VERIFY_REMOVE_EMAIL_EMAIL_TOKEN: Api2JsonVerifyRemoveEmailEmailToken,
        PathValues.API2_JSON_STATS: Api2JsonStats,
        PathValues.API2_JSON_API_USAGE: Api2JsonApiUsage,
        PathValues.API2_JSON_API_USAGE_HISTORY: Api2JsonApiUsageHistory,
        PathValues.API2_JSON_API_USAGE_HISTORY_AGGREGATE: Api2JsonApiUsageHistoryAggregate,
        PathValues.API2_JSON_ADD_CREDITS_API_KEY_USAGE_CREDITS_USER_MESSAGE: Api2JsonAddCreditsApiKeyUsageCreditsUserMessage,
        PathValues.API2_JSON_INVALIDATE_CACHE: Api2JsonInvalidateCache,
        PathValues.API2_JSON_DEBUG_LEVEL_LOGGER_LEVEL: Api2JsonDebugLevelLoggerLevel,
        PathValues.API2_JSON_API_KEY_INFO: Api2JsonApiKeyInfo,
        PathValues.API2_JSON_EXPLAINABILITY_SOURCE_EXPLAINABLE: Api2JsonExplainabilitySourceExplainable,
        PathValues.API2_JSON_SWITCH_DEFAULT_APIKEY_ACTIVE_DEFAULT_BLOCKED: Api2JsonSwitchDefaultAPIKeyActiveDefaultBlocked,
        PathValues.API2_JSON_EMAIL_BLACKLIST_PATTERN_ADD_PATTERN: Api2JsonEmailBlacklistPatternAddPattern,
        PathValues.API2_JSON_EMAIL_BLACKLIST_PATTERN_REMOVE_PATTERN: Api2JsonEmailBlacklistPatternRemovePattern,
        PathValues.API2_JSON_COUNT_SPAM_NON_SPAM_DURATION_MILLIS: Api2JsonCountSpamNonSpamDurationMillis,
        PathValues.API2_JSON_COUNT_SPAM_NON_SPAM: Api2JsonCountSpamNonSpam,
        PathValues.API2_JSON_NAME_BLACKLIST_PATTERN_ADD_PATTERN: Api2JsonNameBlacklistPatternAddPattern,
        PathValues.API2_JSON_NAME_BLACKLIST_PATTERN_REMOVE_PATTERN: Api2JsonNameBlacklistPatternRemovePattern,
        PathValues.API2_JSON_NAME_BLACKLIST_PATTERNS: Api2JsonNameBlacklistPatterns,
        PathValues.API2_JSON_SIGNUPS_IP_ADDRESS: Api2JsonSignupsIpAddress,
        PathValues.API2_JSON_CORPORATE_KEY_API_KEY_CORPORATE: Api2JsonCorporateKeyApiKeyCorporate,
        PathValues.API2_JSON_SPAMSURGE_BLOCK_DISPOSABLE_EMAILS: Api2JsonSpamsurgeBlockDisposableEmails,
        PathValues.API2_JSON_MULTINOMIAL_CREATE: Api2JsonMultinomialCreate,
        PathValues.API2_JSON_MULTINOMIAL_CLASSIFIER_NAME: Api2JsonMultinomialClassifierName,
        PathValues.API2_JSON_MULTINOMIAL: Api2JsonMultinomial,
    }
)
