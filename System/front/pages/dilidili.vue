<!--
@File   : dilidili.vue
@Time   : 2022/6/27 ‏‎‏‎9:49:01
@Author : Sparkling-Y
@Desc   : 本站
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
						<image @click="navi_my()" style="cursor:pointer;text-decoration:none;height: 40px; width: 40px; display: block; margin: 0 auto;border-radius: 50%;  border: 3rpx solid #ffb9d4;" src="../static/portrait.jpg">
						</image>
					</view>
					<text class="portrait-txt">
						{{this.name}}
					</text>
				</uni-col>
				<!-- 足迹 -->
				<uni-col :span="2">
					<view class="foot">
						<image @click="navi_my()" style="cursor:pointer;text-decoration:none;width: 42px; display: block; margin: 0 auto;" mode="widthFix" src="../static/foot.png">
						</image>
					</view>
					<text class="foot-txt">
						足迹
					</text>
				</uni-col>
				<!-- 本站 -->
				<uni-col :span="2">
					<view class="exit">
						<image style="cursor:pointer;text-decoration:none;width: 42px; display: block; margin: 0 auto;" mode="widthFix" src="../static/admin.png">
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
		<!-- 选择按钮 -->
		<view class="option">
			<view style="padding-top: 10px;">
				<uni-row>
					<uni-col :span="5">
						<button :plain="true" style="border: 1px solid #ffffff00 !important;"class="btn_foot" @click="show(0)">
							<text  :style="{'color': (choose==0 ? '#9a9bcf':'#4c4351')}" style="line-height: 50rpx; font-size: 50rpx;font-family: cute;">动漫统计</text>
						</button>
					</uni-col>
					<uni-col :span="6">
						<button :plain="true" style="border: 1px solid #ffffff00 !important;"class="btn_foot" @click="show(1)">
							<text  :style="{'color': (choose==1 ? '#9a9bcf':'#4c4351')}" style="line-height: 50rpx; font-size: 50rpx;font-family: cute;">漫画统计</text>
						</button>
					</uni-col>
					<uni-col :span="6">
						<button :plain="true" style="border: 1px solid #ffffff00 !important;"class="btn_foot" @click="show(2)">
							<text  :style="{'color': (choose==2 ? '#9a9bcf':'#4c4351')}" style="line-height: 50rpx; font-size: 50rpx;font-family: cute;">小说统计</text>
						</button>
					</uni-col>
					<uni-col :span="5">
						<button :plain="true" style="border: 1px solid #ffffff00 !important;"class="btn_foot" @click="show(3)">
							<text  :style="{'color': (choose==3 ? '#9a9bcf':'#4c4351')}" style="line-height: 50rpx; font-size: 50rpx;font-family: cute;">Cosplay统计</text>
						</button>
					</uni-col>
				</uni-row>
			</view>
			
		</view>
		<!-- 动漫统计 -->
		<view class="statistic" v-if="choose == 0">
			<text class="title" > 词云统计图 </text>
			<qiun-data-charts style="height: 500rpx;margin-top: calc(1%);" type="word" :chartData="Word"/>
			<text class="title" > 标签分布图 </text>
			<qiun-data-charts type="mount" :opts="{extra:{mount:{type:'bar',widthRatio:0.3,borderWidth: 0,barBorderRadius: [50,50,50,50],linearType: 'custom'}}}" :chartData="Mount"/>
			<text class="title" > 评分分布图 </text>
			<qiun-data-charts type="area" :opts="{extra:{area:{type:'curve',addLine:true,gradient:true}}}"  :chartData="Line"/>
		</view>
		<!-- 漫画统计 -->
		<view class="statistic" v-if="choose == 1">
			<text class="title" > 词云统计图 </text>
			<qiun-data-charts style="height: 500rpx;margin-top: calc(1%);" type="word" :chartData="Word"/>
			<text class="title" > 标签分布图 </text>
			<qiun-data-charts type="mount" :opts="{extra:{mount:{type:'bar',widthRatio:0.3,borderWidth: 0,barBorderRadius: [50,50,50,50],linearType: 'custom'}}}" :chartData="Mount"/>
		</view>
		<!-- 小说统计 -->
		<view class="statistic" v-if="choose == 2">
			<text class="title" > 词云统计图 </text>
			<qiun-data-charts style="height: 500rpx;margin-top: calc(1%);" type="word" :chartData="Word"/>
			<text class="title" > 标签分布图 </text>
			<qiun-data-charts type="mount" :opts="{extra:{mount:{type:'bar',widthRatio:0.3,borderWidth: 0,barBorderRadius: [50,50,50,50],linearType: 'custom'}}}" :chartData="Mount"/>
			<text class="title" > 评分分布图 </text>
			<qiun-data-charts type="area" :opts="{extra:{area:{type:'curve',addLine:true,gradient:true}}}"  :chartData="Line"/>
		</view>
		<!-- Cosplay统计 -->
		<view class="statistic" v-if="choose == 3">
			<text class="title" > 词云统计图 </text>
			<qiun-data-charts style="height: 500rpx;margin-top: calc(1%);" type="word" :chartData="Word"/>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				id: 0,
				name: "miao",	// 用户昵称
				choose: 0,		// 选择按钮:
				Word:{		    // 词云
					"series":[
						{"name": "", "textSize": 0},
					]
				},
				Line: {			// 评分
					"categories": [],
					"series": [{
						"name": "",
						"data": []
					}]
				},
				Mount:{			// 标签
					"series": [{
						"data": [
					    {
					    	"name": "",
					    	"value": 0
					    }
					  ]
					}]
				}
			}
		},
		onLoad(option){
			this.id = option.id
			this.name = option.name
			uni.request({
				url: 'http://124.70.91.77:8000/api/stat/animekeyword',
				method: 'GET',
				success: res => {
					console.log(res)
					this.Word = res.data.result.Word
				},
			})
			uni.request({
				url: 'http://124.70.91.77:8000/api/stat/animetype',
				method: 'GET',
				success: res => {
					console.log(res.data.result)
					this.Mount.series[0]['data'] = res.data.result
				},
			})
			uni.request({
				url: 'http://124.70.91.77:8000/api/stat/animescore',
				method: 'GET',
				success: res => {
					console.log(res.data.result)
					this.Line.categories = res.data.result.categories
					this.Line.series[0]['name'] = "动漫评分"
					this.Line.series[0]['data'] = res.data.result.data
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
			show(i){
				this.choose = i
				if (i == 0){
					uni.request({
						url: 'http://124.70.91.77:8000/api/stat/animekeyword',
						method: 'GET',
						success: res => {
							console.log(res)
							this.Word = res.data.result.Word
						},
					})
					uni.request({
						url: 'http://124.70.91.77:8000/api/stat/animetype',
						method: 'GET',
						success: res => {
							console.log(res.data.result)
							this.Mount.series[0]['data'] = res.data.result
						},
					})
					uni.request({
						url: 'http://124.70.91.77:8000/api/stat/animescore',
						method: 'GET',
						success: res => {
							console.log(res.data.result)
							this.Line.categories = res.data.result.categories
							this.Line.series[0]['name'] = "动漫评分"
							this.Line.series[0]['data'] = res.data.result.data
						},
					})
				}
				else if (i == 2){
					uni.request({
						url: 'http://124.70.91.77:8000/api/stat/novelkeyword',
						method: 'GET',
						success: res => {
							console.log(res)
							this.Word = res.data.result.Word
						},
					})	
					uni.request({
						url: 'http://124.70.91.77:8000/api/stat/noveltype',
						method: 'GET',
						success: res => {
							console.log(res.data.result)
							this.Mount.series[0]['data'] = res.data.result
						},
					})
					uni.request({
						url: 'http://124.70.91.77:8000/api/stat/novelscore',
						method: 'GET',
						success: res => {
							console.log(res.data.result)
							this.Line.categories = res.data.result.categories
							this.Line.series[0]['name'] = "小说评分"
							this.Line.series[0]['data'] = res.data.result.data
						},
					})
				}
				else if (i == 1){
					uni.request({
						url: 'http://124.70.91.77:8000/api/stat/comickeyword',
						method: 'GET',
						success: res => {
							console.log(res)
							this.Word = res.data.result.Word
						},
					})
					uni.request({
						url: 'http://124.70.91.77:8000/api/stat/comictype',
						method: 'GET',
						success: res => {
							console.log(res.data.result)
							this.Mount.series[0]['data'] = res.data.result
						},
					})
				}
				else if (i == 3){
					uni.request({
						url: 'http://124.70.91.77:8000/api/stat/cosplaykeyword',
						method: 'GET',
						success: res => {
							console.log(res)
							this.Word = res.data.result.Word
						},
					})
				}
			}
		
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
	
	.option{
		margin-top: 5px;
		margin-left: calc(8%);
		margin-right: calc(8%);
		height: 60px; 
		background-color: #ffffff;
		border-bottom-left-radius: 15px;
		border-bottom-right-radius: 15px;
	}
	.statistic{
		margin-top: 10px;
		margin-left: calc(8%);
		margin-right: calc(8%);
		height: auto; 
		background-color: #ffffff;
		border-top-left-radius: 15px;
		border-top-right-radius: 15px;
		margin-bottom: calc(5%);
	}
	.title{
		font-family: cute;
		font-size: 50rpx;
		margin-left: calc(3%);
	}
</style>
