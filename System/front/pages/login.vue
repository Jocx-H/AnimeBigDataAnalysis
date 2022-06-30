<!--
@File   : login.vue
@Time   : 2022/6/21 14:41:04
@Author : Sparkling-Y
@Desc   : 登陆界面
-->

<template>
	<view>
		<!-- 图标 -->
		<view class="dilidili">
			<image mode="widthFix" src="../static/dilidili.png">
			</image>
		</view>
		<!-- 用户名 -->
		<view class="admin">
			<input class="uni-input" v-model="form.id" type="number" placeholder="用户名" placeholder-style="font-size:40rpx;color:#ACACAC;" />
		</view>
		<!-- 密码 -->
		<view class="pwd">
			<input class="uni-input"  v-model="form.password" password type="text" placeholder="密码"  placeholder-style="font-size:40rpx;color:#ACACAC;"/>
		</view>
		<!-- 登录 -->
		<button class="log-btn" @click="log_in()">
			<text>登录</text>
		</button>
		<!-- 背景图 -->
		<view class="bg">
			<uni-row :gutter="0">
				<uni-col :span="12">
					<view>
						<image style="width: 200px;" mode="aspectFit" src="../static/login_left.png">
						</image>
					</view>
				</uni-col>
				<uni-col :span="12">
					<view class="bg-right">
						<image style="width: 200px;" mode="aspectFit" src="../static/login_right.png">
						</image>
					</view>
				</uni-col>
			</uni-row>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				form: {
					id: '',
					password: '',
				},
			}
		},
		methods: {
			log_in() {
				// 和后端交互再用
				uni.setStorage({
					key: 'password',
					data: this.form.password,
				});
				uni.setStorage({
					key: 'id',
					data: this.form.id,
				});
				uni.request({
					url: 'http://124.70.91.77:8000/api/user/login?account=' + this.form.id + '&password=' + this.form.password,
					method: 'POST',
					success: res => {
						console.log(res)
						uni.navigateTo({
							url: "./main?id=" + res.data.usr.uid + "&name=" + res.data.usr.uname
						})
					},
				})
				
			},
		}
	}
</script>

<style>	
	page{
		height: 100%;
		position: fixed;
	}
	@font-face{
		font-family: cute;
		src: url('~@/static/TsangerXWZ.ttf');
		@include flex;
		flex-direction: row;
		flex-wrap: wrap;
		align-items: center;
	}
	.dilidili{
		margin-top: calc(8%);
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.admin{
		font-family: cute;
		margin-top:calc(3%);
		margin-left:calc(40%);
		margin-right:calc(40%);
		height: 70rpx;
		display: flex;
		align-items: center;
		justify-content: center;
		border: 5rpx solid #d9d9d9;
		border-radius: 20rpx;
		/* padding: 10rpx; */
	}
	.pwd{
		font-family: cute;
		margin-top:calc(2%);
		margin-left:calc(40%);
		margin-right:calc(40%);
		height: 70rpx;
		display: flex;
		align-items: center;
		justify-content: center;
		border: 5rpx solid #d9d9d9;
		border-radius: 20rpx;
		/* padding: 10rpx; */
	}
	.bg{
		bottom: 0;
	}
	.bg-right{
		float: right;
	}
	.log-btn{
		font-family: cute;
		margin-top:calc(4%);
		margin-left:calc(45%);
		margin-right:calc(45%);
		margin-bottom:calc(2%);
		height: 90rpx;
		background-color: #ffa4c3;
		color: #ffffff;
		font-size: 45rpx;
		font-family: cute;
		line-height: 45px;
		border-radius: 20rpx;
		box-shadow: 0px 3px 1px -2px rgba(0, 0, 0, 0.2), 0px 3px 2px 0px rgba(0, 0, 0, 0.15), 0px 1px 5px 0px rgba(0, 0, 0, 0.12);
	}
	button{
		list-style: none;
		transition: .3s linear;
	}
	button:hover{
		background-color: #ffb9d4;
		transform: scale(1.1);    /*盒子放大*/
	}
	button::before, button::after{
	    position: absolute;
	    content: '';
	    transition: 1.3s ease-out ;
	}
</style>
