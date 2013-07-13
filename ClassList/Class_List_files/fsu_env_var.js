//FSU login and associated system pages variables.
var env_name = 'Campus Solutions';
var env_app_ver = '9.0';
var env_tools_ver = '8.52';

//Environment indicator variable.
var env_db_id = 'SPRDCS';

var env_root_url = "https://campus.omni.fsu.edu/psp/sprdcs/";

// CAS SERVER URL --  This MUST match entry in URL Definition FSU_CAS_SERVER
var env_cas_url = "https://cas.fsu.edu/cas/";
// The casproxy is only for the signon page. It helps to receive the uid/pwd from the signon page
// and passes it appropriately to the CAS signon authentication. Prior to CAS Upgrade this should
// be equal to env_cas_url.
var env_cas_proxy_url = "https://cas.fsu.edu/cas/casproxy/login";

// Portal Login URL.
var portal_login_url = 'https://portal.omni.fsu.edu/psp/sprdep/?cmd=login';

// Web Server Indicator variable
// This is the debug to show us web server in the javascript (Page -> View Source -> View fsu_env_var.js).
var env_web_indicator = 'CP1D';

// Google Analytics variable
// This should be blank in DEV,TST, 13 in QNA, 12 in PRD. 
var env_google_analytics = '12';
