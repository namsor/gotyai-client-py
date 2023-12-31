# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from gotyai_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API2_JSON_SHUTDOWN = "/api2/json/shutdown"
    API2_JSON_FLUSH = "/api2/json/flush"
    API2_JSON_USER_INFO_TOKEN = "/api2/json/userInfo/{token}"
    API2_JSON_FIT_ONE_CLASSIFIER_UUID = "/api2/json/fitOne/{classifierUuid}"
    API2_JSON_PREDICT_MANY_CLASSIFIER_UUID = "/api2/json/predictMany/{classifierUuid}"
    API2_JSON_EXPLAIN_ONE_CLASSIFIER_UUID = "/api2/json/explainOne/{classifierUuid}"
    API2_JSON_EXPLAIN_MANY_CLASSIFIER_UUID = "/api2/json/explainMany/{classifierUuid}"
    API2_JSON_FIT_MANY_CLASSIFIER_UUID = "/api2/json/fitMany/{classifierUuid}"
    API2_JSON_PREDICT_ONE_CLASSIFIER_UUID = "/api2/json/predictOne/{classifierUuid}"
    API2_JSON_DISABLE_SOURCE_DISABLED = "/api2/json/disable/{source}/{disabled}"
    API2_JSON_BILLING_HISTORY_TOKEN = "/api2/json/billingHistory/{token}"
    API2_JSON_RETRIEVE_KEY_TOKEN = "/api2/json/retrieveKey/{token}"
    API2_JSON_PROCURE_KEY_TOKEN_RECAPTCHAV2 = "/api2/json/procureKey/{token}/{recaptchav2}"
    API2_JSON_PROCURE_KEY_TOKEN = "/api2/json/procureKey/{token}"
    API2_JSON_RESEND_KEY_TOKEN_RECAPTCHAV2 = "/api2/json/resendKey/{token}/{recaptchav2}"
    API2_JSON_AVAILABLE_PLANS = "/api2/json/availablePlans"
    API2_JSON_AVAILABLE_PLANS_TOKEN = "/api2/json/availablePlans/{token}"
    API2_JSON_SUBSCRIBE_PLAN_PLAN_NAME_TOKEN = "/api2/json/subscribePlan/{planName}/{token}"
    API2_JSON_SUBSCRIBE_PLAN_ON_BEHALF_PLAN_NAME_API_KEY = "/api2/json/subscribePlanOnBehalf/{planName}/{apiKey}"
    API2_JSON_REMOVE_USER_ACCOUNT_TOKEN = "/api2/json/removeUserAccount/{token}"
    API2_JSON_REMOVE_USER_ACCOUNT_ON_BEHALF_API_KEY = "/api2/json/removeUserAccountOnBehalf/{apiKey}"
    API2_JSON_UPDATE_LIMIT_USAGE_LIMIT_HARD_OR_SOFT_TOKEN = "/api2/json/updateLimit/{usageLimit}/{hardOrSoft}/{token}"
    API2_JSON_BILLING_INFO_TOKEN = "/api2/json/billingInfo/{token}"
    API2_JSON_UPDATE_USER_INFO_EMAIL_DISPLAY_NAME_TOKEN = "/api2/json/updateUserInfo/{email}/{displayName}/{token}"
    API2_JSON_UPDATE_BILLING_INFO_TOKEN = "/api2/json/updateBillingInfo/{token}"
    API2_JSON_IP_ADDRESSES_BLACKLIST_CANDIDATES = "/api2/json/ipAddressesBlacklistCandidates"
    API2_JSON_EMAIL_BLACKLIST_PATTERNS = "/api2/json/emailBlacklistPatterns"
    API2_JSON_CHARGE_NEW_STRIPE_TOKEN_STRIPE_EMAIL = "/api2/json/chargeNew/{stripeToken}/{stripeEmail}"
    API2_JSON_PAYMENT_INFO_TOKEN = "/api2/json/paymentInfo/{token}"
    API2_JSON_UPDATE_PAYMENT_DEFAULT_DEFAUT_SOURCE_ID_TOKEN = "/api2/json/updatePaymentDefault/{defautSourceId}/{token}"
    API2_JSON_REMOVE_PAYMENT_SOURCE_ID_TOKEN = "/api2/json/removePayment/{sourceId}/{token}"
    API2_JSON_SOFTWARE_VERSION = "/api2/json/softwareVersion"
    API2_JSON_NAMSOR_COUNTER = "/api2/json/namsorCounter"
    API2_JSON_BILLING_CURRENCIES = "/api2/json/billingCurrencies"
    API2_JSON_VERIFY_EMAIL_EMAIL_TOKEN = "/api2/json/verifyEmail/{emailToken}"
    API2_JSON_VERIFY_REMOVE_EMAIL_EMAIL_TOKEN = "/api2/json/verifyRemoveEmail/{emailToken}"
    API2_JSON_STATS = "/api2/json/stats"
    API2_JSON_API_USAGE = "/api2/json/apiUsage"
    API2_JSON_API_USAGE_HISTORY = "/api2/json/apiUsageHistory"
    API2_JSON_API_USAGE_HISTORY_AGGREGATE = "/api2/json/apiUsageHistoryAggregate"
    API2_JSON_ADD_CREDITS_API_KEY_USAGE_CREDITS_USER_MESSAGE = "/api2/json/addCredits/{apiKey}/{usageCredits}/{userMessage}"
    API2_JSON_INVALIDATE_CACHE = "/api2/json/invalidateCache"
    API2_JSON_DEBUG_LEVEL_LOGGER_LEVEL = "/api2/json/debugLevel/{logger}/{level}"
    API2_JSON_API_KEY_INFO = "/api2/json/apiKeyInfo"
    API2_JSON_EXPLAINABILITY_SOURCE_EXPLAINABLE = "/api2/json/explainability/{source}/{explainable}"
    API2_JSON_SWITCH_DEFAULT_APIKEY_ACTIVE_DEFAULT_BLOCKED = "/api2/json/switchDefaultAPIKeyActive/{defaultBlocked}"
    API2_JSON_EMAIL_BLACKLIST_PATTERN_ADD_PATTERN = "/api2/json/emailBlacklistPatternAdd/{pattern}"
    API2_JSON_EMAIL_BLACKLIST_PATTERN_REMOVE_PATTERN = "/api2/json/emailBlacklistPatternRemove/{pattern}"
    API2_JSON_COUNT_SPAM_NON_SPAM_DURATION_MILLIS = "/api2/json/countSpamNonSpam/{durationMillis}"
    API2_JSON_COUNT_SPAM_NON_SPAM = "/api2/json/countSpamNonSpam"
    API2_JSON_NAME_BLACKLIST_PATTERN_ADD_PATTERN = "/api2/json/nameBlacklistPatternAdd/{pattern}"
    API2_JSON_NAME_BLACKLIST_PATTERN_REMOVE_PATTERN = "/api2/json/nameBlacklistPatternRemove/{pattern}"
    API2_JSON_NAME_BLACKLIST_PATTERNS = "/api2/json/nameBlacklistPatterns"
    API2_JSON_SIGNUPS_IP_ADDRESS = "/api2/json/signups/{ipAddress}"
    API2_JSON_CORPORATE_KEY_API_KEY_CORPORATE = "/api2/json/corporateKey/{apiKey}/{corporate}"
    API2_JSON_SPAMSURGE_BLOCK_DISPOSABLE_EMAILS = "/api2/json/spamsurge/{blockDisposableEmails}"
    API2_JSON_MULTINOMIAL_CREATE = "/api2/json/multinomialCreate"
    API2_JSON_MULTINOMIAL_CLASSIFIER_NAME = "/api2/json/multinomial/{classifierName}"
    API2_JSON_MULTINOMIAL = "/api2/json/multinomial"
