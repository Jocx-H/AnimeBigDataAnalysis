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
						<image @click="navi_main()" style="cursor:pointer;text-decoration:none;height: 40px;float: left;" mode="heightFix" src="../static/dilidili.png">
						</image>
					</view>
				</uni-col>
				<!-- 用户头像 -->
				<uni-col :span="2">
					<view class="portrait">
						<image style="cursor:pointer;text-decoration:none;height: 40px; width: 40px; display: block; margin: 0 auto;border-radius: 50%;  border: 3rpx solid #ffb9d4;" src="../static/portrait.jpg">
						</image>
					</view>
					<text class="portrait-txt">
						{{this.name}}
					</text>
				</uni-col>
				<!-- 足迹 -->
				<uni-col :span="2">
					<view class="foot">
						<image style="cursor:pointer;text-decoration:none;width: 42px; display: block; margin: 0 auto;" mode="widthFix" src="../static/foot.png">
						</image>
					</view>
					<text class="foot-txt">
						足迹
					</text>
				</uni-col>
				<!-- 本站 -->
				<uni-col :span="2">
					<view class="exit">
						<image @click="navi_dilidili()" style="cursor:pointer;text-decoration:none;width: 42px; display: block; margin: 0 auto;" mode="widthFix" src="../static/admin.png">
						</image>
					</view>
					<text class="exit-txt">
						本站
					</text>
				</uni-col>
				<!-- 退出-->
				<uni-col :span="2">
					<view class="exit">
						<image @click="exit()" style="cursor:pointer;text-decoration:none;width: 42px; display: block; margin: 0 auto;" mode="widthFix" src="../static/exit.png">
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
					<image style="width: 350rpx;border-top-left-radius: 10px; border-top-right-radius: 10px;border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;" :src="foot_pic[i]" mode="aspectFill" @click="toDetail(i)"></image>
				</view>
				<text class="foot_content_title"> {{foot_name[i]}} </text>
			</view>
		</view>
		<!-- 内容（数据分析） -->
		<view class="data-content" v-if="foot_or_data==1">
			<text style="font-family: cute;font-size: 50rpx; padding-left: calc(5%);" > 用户画像 </text>
			<qiun-data-charts class="pic" type="radar" :opts="{legend:{position: 'bottom'},extra:{radar:{gridType:'circle', max:10}}}" :chartData="Radar"/>
			<text style="font-family: cute;font-size: 50rpx; padding-left: calc(5%);" > 观看类型统计 </text>
			<qiun-data-charts class="pic" type="rose" :opts="{legend:{position: 'bottom'},extra:{rose:{type:'radius'}}}" :chartData="PieA"/>
			<text style="font-family: cute;font-size: 50rpx; padding-left: calc(5%);" > 观看历史统计 </text>
			<qiun-data-charts class="pic" type="area" :opts="{extra:{area:{type:'curve',addLine:true,gradient:true}}}" :chartData="Line"/>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				temp_6: [0,1,2,3,4,5],
				temp_12: [6,7,8,9,10,11],
				id: 0,
				name: "miao",	// 用户昵称
				foot_or_data: 0,	// 0为足迹，1为数据分析
				foot_pic:["", "",	"",	"",	"",	"",	"",	"",	"",	"",	"", ""],// 足迹的封面图片
				foot_name:["", "",	"",	"",	"",	"",	"",	"",	"",	"",	"", ""],// 足迹的图片标题
				foot_id:[],// 足迹的内容id
				Radar: {	//用户画像
					"categories": [""],
					"series": [{
						"name": "",
						"data": []
					}]
				},
				PieA :{		// 观看类型统计
					"series": [{
						"data": [
					    {
					    	"name": "动漫",
					    	"value": 0
					    }, {
					    	"name": "漫画",
					    	"value": 0
					    }, {
					    	"name": "小说",
					    	"value": 0
					    }
					  ]
					}]
				},
				Line: {		// 观看历史统计
					"categories": ["", "", "", "", "", ""],
					"series": [{
						"name": "动漫",
						"data": []
					}, {
						"name": "漫画",
						"data": []
					}, {
						"name": "小说",
						"data": []
					}]
				},
			}
		},
		onLoad(option){
			this.id = option.id
			this.name = option.name
			uni.request({
				url: 'http://124.70.91.77:8000/api/user/history?uid=' + option.id,
				method: 'POST',
				success: res => {
					console.log(res)
					this.foot_id = res.data.result.id
					this.foot_name = res.data.result.title
					this.foot_pic = res.data.result.cover
				},
			})
			uni.request({
				url: 'http://124.70.91.77:8000/api/user/analysis?uid=' + this.id,
				method: 'POST',
				success: res => {
					console.log(res)
					this.Radar.categories = res.data.result.userImageDir.categories
					this.Radar.series[0]['name'] = res.data.result.userImageDir.name
					this.Radar.series[0]['data'] = res.data.result.userImageDir.data
					this.PieA.series[0].data = res.data.result.sum
					this.Line = res.data.result.lineChart
				},
			})
		},
		methods: {
			navi_my(){
				uni.navigateTo({
					url: "/pages/my?id=" + this.id + "&name=" + this.name
				})
			},
			navi_main(){
				uni.navigateTo({
					url: "/pages/main?id=" + this.id + "&name=" + this.name
				})
			},
			navi_dilidili(){
				uni.navigateTo({
					url: "/pages/dilidili?id=" + this.id + "&name=" + this.name
				})
			},
			exit(){
				uni.navigateTo({
					url: "/pages/login"
				})
			},
			show_foot(){
				this.foot_or_data = 0;
			},
			show_data(){
				this.foot_or_data = 1;
				console.log(",,,,,",this.foot_or_data);
				
			},
			// 跳转详情页
			toDetail(i){
				console.log("i:" , this.foot_id[i][0]);
				if (this.foot_id[i].toString().substring(0,1) == "1"){
					// 打开动漫新标签页
					var { href } = this.$router.resolve({ path: "detail", query: { id:this.id, name: this.name, idfr: this.foot_id[i] } }); 
					window.open(href, '_blank');
				}
				else if (this.foot_id[i].toString().substring(0,1) == "2"){
					// 打开漫画新标签页
					var { href } = this.$router.resolve({ path: "detail", query: { id:this.id, name: this.name, idfr: this.foot_id[i] } }); 
					window.open(href, '_blank');
				}
				else if (this.foot_id[i].toString().substring(0,1) == "3"){
					// 打开漫画新标签页
					var { href } = this.$router.resolve({ path: "detail", query: { id:this.id, name: this.name, idfr: this.foot_id[i] } }); 
					window.open(href, '_blank');
				}
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
		cursor:pointer;
		text-decoration:none;
		margin-top: 30px;
		display: flex;
		flex-wrap: wrap;
		justify-content: left;
		align-content: space-between;
	}
	.foot_content_title{
		width: 350rpx;
		word-break:break-all;
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
		height: 3200rpx; 
		background-color: #ffffff;
		border-top-left-radius: 15px;
		border-top-right-radius: 15px;
		margin-bottom: calc(2%);
	}
	.pic{
		height: 700rpx;
		padding-top: calc(5%);
	}
</style>
