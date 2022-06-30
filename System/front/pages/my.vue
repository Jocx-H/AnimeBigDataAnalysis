<!--
@File   : my.vue
@Time   : 2022‎/‎6‎/25 11:26:56
@Author : Sparkling-Y
@Desc   : 详情页
-->

<template>
	<view>
		<!-- 导航栏 -->
		<view class="navi">
			<uni-row>
				<!-- dilidili图标 -->
				<uni-col :span="16">
					<view class="dilidili">
						<image @click="navi_main()" style="height: 40px;float: left;" mode="heightFix" src="../static/dilidili.png">
						</image>
					</view>
				</uni-col>
				<!-- 用户头像 -->
				<uni-col :span="2">
					<view class="portrait">
						<image style="height: 40px; width: 40px; display: block; margin: 0 auto;border-radius: 50%;  border: 3rpx solid #ffb9d4;" src="../static/portrait.jpg">
						</image>
					</view>
					<text class="portrait-txt">
						{{this.name}}
					</text>
				</uni-col>
				<!-- 足迹 -->
				<uni-col :span="2">
					<view class="foot">
						<image style="width: 42px; display: block; margin: 0 auto;" mode="widthFix" src="../static/foot.png">
						</image>
					</view>
					<text class="foot-txt">
						足迹
					</text>
				</uni-col>
				<!-- 本站 -->
				<uni-col :span="2">
					<view class="exit">
						<image @click="navi_dilidili()" style="width: 42px; display: block; margin: 0 auto;" mode="widthFix" src="../static/admin.png">
						</image>
					</view>
					<text class="exit-txt">
						本站
					</text>
				</uni-col>
				<!-- 退出-->
				<uni-col :span="2">
					<view class="exit">
						<image @click="exit()" style="width: 42px; display: block; margin: 0 auto;" mode="widthFix" src="../static/exit.png">
						</image>
					</view>
					<text class="exit-txt">
						退出
					</text>
				</uni-col>
			</uni-row>
		</view>
		<!-- 顶部区域 -->
		<view class="top">
			<!-- 头像 -->
			<image class="top_portrait" src="../static/portrait.jpg"></image>
			<!-- 昵称 -->
			<text class="nick_name"> {{name}}</text>
		</view>
		<!-- 按钮（足迹和数据分析） -->
		<view class="option">
			<uni-row>
				<uni-col :span="2">
					<button :plain="true" style="border: 1px solid #ffffff00 !important;"class="btn_foot" @click="show_foot()">
						<text  :style="{'color': (foot_or_data==0 ? '#9a9bcf':'#4c4351')}" style="line-height: 50rpx; font-size: 40rpx;font-family: cute;">足迹</text>
					</button>
				</uni-col>
				<uni-col :span="6">
					<button :plain="true" style="border: 1px solid #ffffff00 !important;"class="btn_foot" @click="show_data()">
						<text  :style="{'color': (foot_or_data==1 ? '#9a9bcf':'#4c4351')}" style="line-height: 50rpx; font-size: 40rpx;font-family: cute;">数据分析</text>
					</button>
				</uni-col>
			</uni-row>
		</view>
		<!-- 内容（足迹） -->
		<view class="foot-content" v-if="foot_or_data==0">
			<view style="margin-left: 32px; margin-bottom: calc(2%);" v-for="(item, i) in foot_id" :key="i+'b'">
				<view class="foot_content_image">
					<image style="width: 350rpx;" :src="foot_pic[i]" mode="aspectFit" @click="toDetail(foot_id[i])"></image>
				</view>
				<text class="foot_content_title"> {{foot_name[i]}} </text>
			</view>
		</view>
		<!-- 内容（数据分析） -->
		<view class="data-content" v-if="foot_or_data==1">
			
			
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				temp_6: [0,1,2,3,4,5],
				temp_12: [6,7,8,9,10,11],
				name: "miao",	// 用户昵称
				foot_or_data: 0,	// 0为足迹，1为数据分析
				foot_pic:[			// 足迹的封面图片
					"http://i0.hdslb.com/bfs/bangumi/1cc333ff578e5ea9fded7e454953a4e2291440c2.png",
					"http://i0.hdslb.com/bfs/bangumi/image/4f3edbede7fc0bdb52842075cf8faaa1c5953eaa.png",
					"http://i0.hdslb.com/bfs/bangumi/image/39f7d690deb477004673f40e0fe65c78895c94f4.png",
					"http://i0.hdslb.com/bfs/bangumi/image/a9497ed9b2ad8fd3b77289734769f81bd3948d75.png",
					"http://i0.hdslb.com/bfs/bangumi/image/91e9534cc55aa1a6dc959e7d6d33bde970208232.png",
					"http://i0.hdslb.com/bfs/bangumi/image/cece1d7eaabd0fac10480efec3d879c542247734.png",
					"http://i0.hdslb.com/bfs/bangumi/image/376d7e69a667bcb1c0b934a4e35e07e7fa23110b.png",
					"http://i0.hdslb.com/bfs/bangumi/image/fd492888df64bbc3b821dac5d516dbc1c2fe5f08.png",
					"http://i0.hdslb.com/bfs/bangumi/image/9d8d2922b08f3d08d018e6e59e49607cf16d39e6.png",
					"http://i0.hdslb.com/bfs/bangumi/image/847e9dbb6876fb37a30199a5c88910704976d45b.png",
					"http://i0.hdslb.com/bfs/bangumi/image/82d628408f5472f1440982e880b0b4f0146862ad.png",
					// "http://i0.hdslb.com/bfs/bangumi/image/f5128c939b24909c7cb75bab51be0ee0c4d1b33a.jpg"
				],
				foot_name:[			// 足迹的图片标题
					"青春猪头少年不会梦到兔女郎学姐",
					"Re：从零开始的异世界生活",
					"辉夜大小姐想让我告白",
					"间谍过家家",
					"咒术回战",
					"工作细胞",
					"国王排名",
					"关于我转生变成史莱姆这档事",
					"JOJO的奇妙冒险",
					"小林家的龙女仆 第二季",
					"我的青春恋爱物语果然有问题",
					// "四月是你的谎言"
				],
				foot_id:[			// 足迹的内容id
					"001","002","003","004","005","006","007","008","009","010","011",
				]
			}
		},
		methods: {
			navi_my(){
				uni.navigateTo({
					url: '/pages/my',
				})
			},
			navi_main(){
				uni.navigateTo({
					url: '/pages/main',
				})
			},
			navi_dilidili(){
				uni.navigateTo({
					url: '/pages/dilidili',
				})
			},
			exit(){
				uni.navigateTo({
					url: '/pages/login',
				})
			},
			show_foot(){
				this.foot_or_data = 0;
			},
			show_data(){
				this.foot_or_data = 1;
			},
			// 跳转详情页
			toDetail(idenfr){
				// 打开新标签页
				var { href } = this.$router.resolve({ path: "detail", query: {  idfr: idenfr } }); 
				window.open(href, '_blank');
			},
		}
	}
</script>

<style>
	page{
		overflow-y: auto;
		background-color: #f4f5f7;
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
		margin-top: 13px;
		margin-left: 10px;
	}
	.navi{
		height: 130rpx;
		box-shadow: 0px 3px 5px 0px rgba(0, 0, 0, 0.2);
		background-color: #ffffff;
	}
	.portrait{
		margin-top: 5px;
	}
	.foot{
		margin-top: 5px;
	}
	.exit{
		margin-top: 5px;
	}
	.portrait-txt{
		margin-top: 2px;
		font-family: cute;
		color: #FFb9d4;
		font-size: 13px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.foot-txt{
		font-family: cute;
		color: #FFb9d4;
		font-size: 13px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.exit-txt{
		font-family: cute;
		color: #FFb9d4;
		font-size: 13px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	
	.top{
		margin-top: 1px;
		margin-left: calc(8%);
		margin-right: calc(8%);
		height: 400rpx;
		background-image: url("https://i0.hdslb.com/bfs/space/24d0815514951bb108fbb360b04a969441079315.png@2560w_400h_100q_1o.webp");
	}
	.top_portrait{
		margin-top: 200rpx;
		margin-left: 130rpx;
		height: 65px; 
		width: 65px; 
		position: absolute;
		border-radius: 50%;  
		border: 5rpx solid #ffffff;
		z-index: 2;
	}
	.nick_name{
		margin-top: 220rpx;
		margin-left: 330rpx;
		font-family: cute;
		font-size: 50rpx;
		color: #ffffff;
		position: absolute;
		z-index: 2;
	}
	
	.option{
		margin-left: calc(8%);
		margin-right: calc(8%);
		height: 60px; 
		background-color: #ffffff;
		border-bottom-left-radius: 15px;
		border-bottom-right-radius: 15px;
	}
	.btn_foot{
		margin-top: 8px;
		margin-left: 18px;
	}
	.foot-content{
		margin-top: 10px;
		margin-left: calc(8%);
		margin-right: calc(8%);
		height: auto; 
		background-color: #ffffff;
		border-top-left-radius: 15px;
		border-top-right-radius: 15px;
		display: flex;
		flex-wrap: wrap;
		justify-content: left;
		align-content: space-between;
		margin-bottom: calc(5%);
	}
	.foot_content_image{
		margin-top: 30px;
		display: flex;
		flex-wrap: wrap;
		justify-content: left;
		align-content: space-between;
	}
	.foot_content_title{
		margin-top: 10px;
		font-family: cute;
		font-size: 12px;
        display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: space-around;
		align-items: space-between;
	}
	.data-content{
		margin-top: 10px;
		margin-left: calc(8%);
		margin-right: calc(8%);
		height: 3600rpx; 
		background-color: #ffffff;
		border-top-left-radius: 15px;
		border-top-right-radius: 15px;
	}
</style>
