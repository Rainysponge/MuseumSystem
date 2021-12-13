<template>
	
	<view class="uni-common-mt">
		<view class="logo-content">
			<image class="logo" src="/static/scan_icon.png" @tap="doNothing()"></image>
		</view>
		
		<view class="uni-form-item uni-column">
			<view class="with-fun">
				<input class="uni-input inputText" placeholder="输入用户名" type="text" :value="userName" maxlength="15" @input="userNameInput"/>
			</view>
		</view>
		
		<view class="line"></view>
		
		
		<view class="uni-form-item uni-column">
			<view class="with-fun">
				<input 
					class="uni-input inputText" 
					placeholder="输入密码" 
					password="true"
					type="text" :value="password" maxlength="15" @input="passwordInput"
					/>
			</view>
		</view>
		
		<view class="line"></view>
		
		<view class="uni-padding-wrap uni-common-mt" v-show="loginButtonHide">
			<button type="primary" :disabled="false" @tap="loginFunc">登录</button>
		</view>
		
		<view class="uni-padding-wrap uni-common-mt" v-show="loginOutButtonHide">
			<button type="primary" :disabled="false" @tap="loginOutFunc">退出</button>
		</view>
		
		
		<view class="devIdText">
			设备ID号:<br>
			<text style="color: #0A98D5;">123</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				btnAddDisable: true,
				loginButtonHide : true,
				loginOutButtonHide : false,
				userName : "",
				password: "",
			}
		},
		onLoad() {
			uni.request({//向云端服务发送请求
				url: this.globalVal.api_url.login,
				// http://127.0.0.1:8000/user/login

				method: 'POST',
				data: {
					"req": "2",  // 询问是否已有用户登录
				},
				success: res => {
					// console.log(url);
					console.log(res);
					if(200 == res.statusCode){
						// 用户已经登陆，渲染用户信息
						this.loginButtonHide = false;
						this.loginOutButtonHide = true;
						userName = res.data.userName;
						
						
					}else if(404 == res.statusCode){
						console.log("后端失去连接");
					}else{
						// 给出登录按钮
						
					}
				},
				fail: () => {},
				complete: () => {
					uni.hideLoading();
				}
			});
		},
		methods: {
			userNameInput(e){
				this.userName = e.target.value;
			},
			passwordInput(e){
				this.password = e.target.value;
			},
			loginFunc(){
				uni.request({//向云端服务发送请求
					url: this.globalVal.api_url.login,
					// http://127.0.0.1:8000/user/login
				
					method: 'POST',
					data: {
						userName: this.userName,
						password: this.password,
					},
					success: res => {
						// console.log(url);
						console.log(res);
						if(200 == res.statusCode){
							if(res.data.rspCode == '0'){
								this.loginButtonHide = false;
								this.loginOutButtonHide = true;
							}
							uni.hideLoading();
							uni.showToast({
								title: res.data.message,
								icon:"none",
								duration:2500
							});
							
						}
						
					},
					fail: () => {},
					complete: () => {
						uni.hideLoading();
					},
					header:{
						"Content-Type": "application/json",
						"User-Agent": "PostmanRuntime/7.28.3",
						Cookie: "csrftoken=qoMdFtRxPD8CDZjdvhfqogGD6mQ1i4KiYOUbHlGnkz7dNldx3f7CPqfVK055dZ0z; sessionid=88lmudgefyc7s3e6wogh4fb3g9lk4t2m",
						
					},
				});
			},
			loginOutFunc(){
				uni.request({//向云端服务发送请求
					url: this.globalVal.api_url.loginOut,
					// http://127.0.0.1:8000/user/login
				
					method: 'POST',
					data: {
						userName: this.userName,
					},
					success: res => {
						// console.log(url);
						console.info(res);
						if(200 == res.statusCode){
							if(res.data.rsp == '0'){
								// 退出成功
								this.loginButtonHide = true;
								this.loginOutButtonHide = false;
								
							}else{
								// 退出失败
							}
							
							uni.hideLoading();
							uni.showToast({
								title: res.data.message,
								icon:"none",
								duration:2500
							});
						}
						
					},
					fail: () => {},
					complete: () => {
						uni.hideLoading();
					},
					header:{
						"Content-Type": "application/json",
						"User-Agent": "PostmanRuntime/7.28.3",
						Cookie: "csrftoken=qoMdFtRxPD8CDZjdvhfqogGD6mQ1i4KiYOUbHlGnkz7dNldx3f7CPqfVK055dZ0z; sessionid=88lmudgefyc7s3e6wogh4fb3g9lk4t2m",
						
					},
				});
			},
			doNothing(){
			}
			// scanDev(){
			// 	uni.scanCode({//启动摄像头扫描模组二维码获取IMEI号
			// 		success: (res) => {
			// 			var result;
			// 			console.log('条码类型：' + res.scanType);
			// 			console.log('条码内容：' + res.result);
			// 			if(res.result.length>15){
			// 				result = res.result.substring(0,15);
			// 			}else{
			// 				result = res.result;
			// 			}
			// 			console.log('result：' + result);
			// 			this.imei = result;
			// 			this.btnAddDisable = false;
			// 		},
			// 		fail: (err) => {
			// 			console.log(err);
			// 			// #ifdef MP
			// 			uni.getSetting({
			// 				success: (res) => {
			// 					let authStatus = res.authSetting['scope.camera'];
			// 					if (!authStatus) {
			// 						uni.showModal({
			// 							title: '授权失败',
			// 							content: this.i18n.content_note.text_app_name+'需要使用您的相机，请在设置界面打开相关权限',
			// 							success: (res) => {
			// 								if (res.confirm) {
			// 									uni.openSetting()
			// 								}
			// 							}
			// 						})
			// 					}
			// 				}
			// 			})
			// 			// #endif
			// 		}
			// 	});
			// },
			// imeiInput(e){
			// 	console.log("imeiInput");
			// 	this.imei = e.target.value;
			// 	if(15 == this.imei.length){
			// 		this.btnAddDisable = false;
			// 	}else{
			// 		this.btnAddDisable = true;
			// 	}
			// },
			// nameInput(e){
			// 	console.log("nameInput");
			// 	this.devname = e.target.value;
			// 	if(5 < this.devname.length){
			// 		this.btnRenameDisable = false;
			// 	}else{
			// 		this.btnRenameDisable = true;
			// 	}
			// },
			// regDev(){
			// 	console.log("regDev URL:"+this.globalVal.default_url.devReg);
			// 	uni.showLoading({
			// 		title: '注册中...',
			// 		mask: false
			// 	});
			// 	var errcode = 1;
			// 	var errmsg = "失败";
			// 	uni.request({//向云端服务发送设备注册请求
			// 		url: this.globalVal.default_url.devReg,
			// 		method: 'POST',
			// 		data: {
			// 			imei:this.imei
			// 		},
			// 		success: res => {
			// 			console.log(res);
			// 			if(200 == res.statusCode){
			// 				errcode = res.data.errcode;
			// 				if(0 == errcode){
			// 					errmsg = "注册成功";
			// 					this.devid = res.data.deviceId;
			// 					this.devname = res.data.deviceName;
			// 					this.btnInfoDisable = false;
			// 				}else{
			// 					errmsg = res.data.errmsg;
			// 				}
			// 			}
			// 		},
			// 		fail: () => {},
			// 		complete: () => {
			// 			uni.hideLoading();
			// 			uni.showToast({
			// 				title: errmsg,
			// 				icon:"none",
			// 				duration:2500
			// 			});
			// 		}
			// 	});
			// }
			
		}
	}
</script>

<style>
	.logo-content {
		text-align: center;
		margin-top: 200upx;
		margin-bottom: 100upx;
	}
	
	.logo {
		height: 120upx;
		width: 120upx;
	}
	
	.line {
		width: 90%;
		height: 1px;
		margin-left: 30upx;
		margin-right: 30upx;
		background-color: #cccccc;
		margin-top: 1px;
	}
	
	.inputText {
		margin-left: 30upx;
	}
	.devIdText{
		margin-left: 30upx;
		margin-right: 30upx;
	}
</style>
