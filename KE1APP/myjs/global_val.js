//http://127.0.0.1:8888, https://wifirelay.hanxe.com
const default_host = "https://wifirelay.hanxe.com/gateway/iotgateway/ke1extend/"; 
const api_host = "http://127.0.0.1:8000/"
var default_url = {
	devReg : default_host+'devreg',
	devInfo : default_host+'devinfo',
	devCmd : default_host+'devcmd',
	devHistory : default_host+'devhistory'
}

var api_url = {
	login : api_host + 'user/login',
	loginOut : api_host + 'user/loginOut',
}
export default {
  default_url,
  api_url
}