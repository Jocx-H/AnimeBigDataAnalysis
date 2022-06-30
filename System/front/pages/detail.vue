<!--
@File   : detail.vue
@Time   : 2022/6/23 ‏‎15:42:01
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
						<image style="cursor:pointer;text-decoration:none;height: 40px;float: left;" mode="heightFix" src="../static/dilidili.png">
						</image>
					</view>
				</uni-col>
				<!-- 用户头像 -->
				<uni-col :span="2">
					<view class="portrait">
						<image @click="navi_my()"  style="cursor:pointer;text-decoration:none;height: 40px; width: 40px; display: block; margin: 0 auto;border-radius: 50%;  border: 3rpx solid #ffb9d4;" src="../static/portrait.jpg">
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
		<!-- 详情信息 -->
		<view class="detail-box">
			<!-- 封面 -->
			<image class="detail-img" :src="pic_path" mode="aspectFill"></image>
			<!-- 标题 -->
			<text class="detail-title"> {{title}} </text>
			<view class="detail-biaoqian0" >
				<text v-if="biaoqian[j]!=''" v-for="(item, j) in biaoqian" :key="j+'b'" style="width: 40px; position: absolute;line-height: 1.5;display: flex;align-items: center;justify-content: center;border-radius: 15%;border: 3rpx solid #ffffffd9;" :style="{ marginLeft: j*50 + 'px' }"> {{biaoqian[j]}} </text>
			</view>
			<!-- 总播放量、弹幕总数、评分、是否完结、共xx话-->
			<view class="detail-play" v-if="tag == 0" >
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> 总播放 </text>
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{total_play}} </text>
			</view>
			<view class="detail-danmu" v-if="tag == 0" >
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> 弹幕总数 </text>
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{total_danmu}} </text>
			</view>
			<view class="detail-author" v-if="tag == 1" >
				<text style="line-height: 1.5;"> 作者:  {{author}}</text>
			</view>
			<view class="detail-author" v-if="tag == 2" >
				<text style="line-height: 1.5;"> 更新时间:  {{update}}</text>
			</view>
			<view class="detail-score" v-if="tag == 0 || tag == 2"> 
				<text style="font-size: 70rpx; color: #fea726; line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{score}} </text>
			</view>
			<u-icon class="detail-star-0" name="star" color="#fea726" v-if="tag == 0 || tag == 2"></u-icon>
			<u-icon class="detail-star-1" name="star" color="#fea726" v-if="tag == 0 || tag == 2"></u-icon>
			<u-icon class="detail-star-2" name="star" color="#fea726" v-if="tag == 0 || tag == 2"></u-icon>
			<u-icon class="detail-star-3" name="star" color="#fea726" v-if="tag == 0 || tag == 2"></u-icon>
			<u-icon class="detail-star-4" name="star" color="#fea726" v-if="tag == 0 || tag == 2"></u-icon>
			<u-icon class="detail-star-0" name="star-fill" v-if="score>=1.5&&(tag==0 || tag==2)" color="#fea726" ></u-icon>
			<u-icon class="detail-star-1" name="star-fill" v-if="score>=3.5&&(tag==0 || tag==2)" color="#fea726" ></u-icon>
			<u-icon class="detail-star-2" name="star-fill" v-if="score>=5.5&&(tag==0 || tag==2)" color="#fea726" ></u-icon>
			<u-icon class="detail-star-3" name="star-fill" v-if="score>=7.5&&(tag==0 || tag==2)" color="#fea726" ></u-icon>
			<u-icon class="detail-star-4" name="star-fill" v-if="score>=9.5&&(tag==0 || tag==2)" color="#fea726" ></u-icon>
			<view class="detail-score-num" v-if="tag == 0 || tag == 2">
				<text style="font-size: 15rpx; color: #ffffff; line-height: 1.5;"> {{score_num}} </text>
			</view>
			<view class="detail-info" v-if="tag != 2">
				<text>{{info}}</text>
			</view>
			<!-- 简介 -->
			<view class="detail-brief" v-if="tag == 0 || tag == 2">
				<text>简介：{{brief}}</text>
			</view>
			
			<!-- 原网页链接 -->
			<div class="detail-link">
				<image src="../static/tobili_dm.png" style="cursor:pointer;text-decoration:none;height: 120rpx;" mode="heightFix" v-if="tag==0" @click="toSource()"></image>
				<image src="../static/tobili_mh.png" style="cursor:pointer;text-decoration:none;height: 120rpx;" mode="heightFix" v-if="tag==1" @click="toSource()"></image>
				<image src="../static/tobili_xs.png" style="cursor:pointer;text-decoration:none;height: 120rpx;" mode="heightFix" v-if="tag==2" @click="toSource()"></image>
			</div>
			<!-- 收藏 -->
			<view class="detail-collect">
				<u-button v-if="is_collect == false" type="primary" style="padding: 0 25px !important;" color="#f36392" shape="circle" icon="heart" text="收藏" @click="collect()"></u-button>
				<u-button v-if="is_collect == true" type="primary" style="padding: 0 25px !important;" color="#f36392" shape="circle" icon="heart-fill" text="收藏" @click="collect()"></u-button>
			</view>
			<!-- 评分 -->
			<view class="detail-pingfen">
				<u-icon class="detail-pingfen-0" name="star" color="#fea726" size="30" @click="pingfen(0)"></u-icon>
				<u-icon class="detail-pingfen-1" name="star" color="#fea726" size="30" @click="pingfen(1)"></u-icon>
				<u-icon class="detail-pingfen-2" name="star" color="#fea726" size="30" @click="pingfen(2)"></u-icon>
				<u-icon class="detail-pingfen-3" name="star" color="#fea726" size="30" @click="pingfen(3)"></u-icon>
				<u-icon class="detail-pingfen-4" name="star" color="#fea726" size="30" @click="pingfen(4)"></u-icon>
				<u-icon class="detail-pingfen-0" name="star-fill" color="#fea726" size="30" v-if="is_pingfen == true"  @click="pingfen(0)"></u-icon>
				<u-icon class="detail-pingfen-1" name="star-fill" color="#fea726" size="30" v-if="is_pingfen == true && (pingfen_num>=1)" @click="pingfen(1)"></u-icon>
				<u-icon class="detail-pingfen-2" name="star-fill" color="#fea726" size="30" v-if="is_pingfen == true && (pingfen_num>=2)" @click="pingfen(2)"></u-icon>
				<u-icon class="detail-pingfen-3" name="star-fill" color="#fea726" size="30" v-if="is_pingfen == true && (pingfen_num>=3)" @click="pingfen(3)"></u-icon>
				<u-icon class="detail-pingfen-4" name="star-fill" color="#fea726" size="30" v-if="is_pingfen == true && (pingfen_num>=4)" @click="pingfen(4)"></u-icon>
				<text style="position: absolute;z-index:2;font-size:16px;color: #ffffff; margin-left: 350rpx;margin-top: 2px;" > 点评 </text>
			</view>
			
			<!-- 毛玻璃特效 -->
			<image class="detail-glass" :src="pic_path" mode="aspectFill"></image>
			
			
		</view>
		<view class="recommand">
			<view style="height: 740rpx;"></view>
			<view class="recommand-content">
				<!-- 动漫推荐 -->
				<view style="margin-bottom: calc(1%);">
					<uni-row>
						<uni-col :span="12">
							<text style="float: left; margin-top: 10px;  margin-left: calc(3%);font-family: cute; font-size: 24px;">动漫推荐</text>
						</uni-col>
						<uni-col :span="12">
							<view style="width: 100px; margin-top: 10px;  float: right; margin-right: calc(5%);">
								<u-button type="primary" size="small" :plain="true" color="#61666d" shape="circle" icon="reload" text="换一换" @click="change_change(0)"></u-button>
							</view>
						</uni-col>
					</uni-row>
					<uni-row>
						<uni-col :span="4" v-for="(item, i) in temp_6" :key="i+'b'">
							<view class="rec_content_image">
								<image style="cursor:pointer;text-decoration:none;width: 350rpx;border-top-left-radius: 15px; border-top-right-radius: 15px;border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;" :src="rec_dm_pic_list[item]" mode="aspectFill" @click="toDetail(0, item)"></image>
							</view>
							<text class="rec_content_title"> {{rec_dm_name_list[item]}} </text>
						</uni-col>
					</uni-row>
				</view>
				<!-- 漫画推荐 -->
				<view style="border-top: 3rpx solid #d8d8d887; margin-bottom: calc(1%);">
					<uni-row>
						<uni-col :span="12">
							<text style="float: left; margin-top: 10px;  margin-left: calc(3%);font-family: cute; font-size: 24px;">漫画推荐</text>
						</uni-col>
						<uni-col :span="12">
							<view style="width: 100px; margin-top: 10px;  float: right; margin-right: calc(5%);">
								<u-button type="primary" size="small" :plain="true" color="#61666d" shape="circle" icon="reload" text="换一换" @click="change_change(1)"></u-button>
							</view>
						</uni-col>
					</uni-row>
					<uni-row>
						<uni-col :span="4" v-for="(item, i) in temp_6" :key="i+'b'">
							<view class="rec_content_image">
								<image style="cursor:pointer;text-decoration:none;width: 350rpx;border-top-left-radius: 15px; border-top-right-radius: 15px;border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;" :src="rec_mh_pic_list[i]" mode="aspectFill" @click="toDetail(1, item)"></image>
							</view>
							<text class="rec_content_title"> {{rec_mh_name_list[item]}} </text>
						</uni-col>
					</uni-row>
				</view>
				<!-- 小说推荐 -->
				<view style="border-top: 3rpx solid #d8d8d887; margin-bottom: calc(1%);">
					<uni-row>
						<uni-col :span="12">
							<text style="float: left; margin-top: 10px;  margin-left: calc(3%);font-family: cute; font-size: 24px;">小说推荐</text>
						</uni-col>
						<uni-col :span="12">
							<view style="width: 100px; margin-top: 10px;  float: right; margin-right: calc(5%);">
								<u-button type="primary" size="small" :plain="true" color="#61666d" shape="circle" icon="reload" text="换一换" @click="change_change(2)"></u-button>
							</view>
						</uni-col>
					</uni-row>
					<uni-row>
						<uni-col :span="4" v-for="(item, i) in temp_6" :key="i+'b'">
							<view class="rec_content_image">
								<image style="cursor:pointer;text-decoration:none;width: 350rpx;border-top-left-radius: 15px; border-top-right-radius: 15px;border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;" :src="rec_xs_pic_list[i]" mode="aspectFill" @click="toDetail(2, item)"></image>
							</view>
							<text class="rec_content_title"> {{rec_xs_name_list[item]}} </text>
						</uni-col>
					</uni-row>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				temp_6: [0,1,2,3,4,5],
				tag:  0,		// 一级标签
				idenfr: 0,		// 标识符id
				id:   0,		// 用户名
				name: "",	// 用户昵称
				title: "",		// 题目
				author: "",									// 作者
				biaoqian: [],	// 标签
				update: "",					// 更新时间
				total_play: 2100,			// 播放量
				total_danmu: 410,			// 弹幕总数
				score: 9.8,					// 总评分
				score_num: 155392,			// 评分人数
				info: "",		// 完结信息和集数
				is_collect: false,			// 是否收藏
				pingfen_num: 0,				// 评分分数
				is_pingfen: false,			// 是否评分
				curr_link: "",		// 当前的原视频链接
				brief: "",					// 简介
				pic_path: "",	// 图片
				// 动漫、漫画、小说推荐的封面图片
				rec_dm_pic_list:["","","","","","","","","","","",""],
				rec_mh_pic_list:["","","","","","","","","","","",""],
				rec_xs_pic_list:["","","","","","","","","","","",""],
				// 动漫、漫画、小说推荐的标题
				rec_dm_name_list:["","","","","","","","","","","",""],
				rec_mh_name_list:["","","","","","","","","","","",""],
				rec_xs_name_list:["","","","","","","","","","","",""],
				// 动漫、漫画、小说推荐的标识符，用于跳转详情页
				rec_dm_id_list:["","","","","","","","","","","",""],
				rec_mh_id_list:["","","","","","","","","","","",""],
				rec_xs_id_list:["","","","","","","","","","","",""],
			}
		},
		onLoad(option) {
			this.id = option.id
			this.name = option.name
			this.idenfr = option.idfr
			// 动漫、漫画、小说推荐
			uni.request({
				url: 'http://124.70.91.77:8000/api/hot/anime?uid=' + this.id,
				method: 'GET',
				success: res => {
					console.log(res)
					this.rec_dm_id_list = res.data.result.aid
					this.rec_dm_name_list = res.data.result.title
					this.rec_dm_pic_list = res.data.result.cover
				},
			})
			uni.request({
				url: 'http://124.70.91.77:8000/api/hot/novel?uid=' + this.id,
				method: 'GET',
				success: res => {
					console.log(res)
					this.rec_xs_id_list = res.data.result.nid
					this.rec_xs_name_list = res.data.result.title
					this.rec_xs_pic_list = res.data.result.cover
				},
			})
			uni.request({
				url: 'http://124.70.91.77:8000/api/hot/comic?uid=' + this.id,
				method: 'GET',
				success: res => {
					console.log(res)
					this.rec_mh_id_list = res.data.result.cid
					this.rec_mh_name_list = res.data.result.title
					this.rec_mh_pic_list = res.data.result.cover
				},
			})
			// 获取详情信息
			console.log(option.idfr)
			uni.request({
				url: 'http://124.70.91.77:8000/api/stat/detail?did=' + option.idfr,
				method: 'GET',
				success: res => {
					console.log(res)
					if (res.data.type == "anime"){
						this.tag = 0
						this.title = res.data.result.title
						this.curr_link = res.data.result.video_link
						this.pic_path = res.data.result.cover
						this.biaoqian = res.data.result.media_tags.split(',')
						this.total_play = res.data.result.views
						this.total_danmu = res.data.result.danmakus
						this.info = res.data.result.index_show
						this.score_num = res.data.result.cm_count
						this.score = res.data.result.score
						this.brief = res.data.result.introduce
					}
					else if (res.data.type == "comic"){
						this.tag = 1
						this.title = res.data.result.title
						this.curr_link = res.data.result.url
						this.biaoqian = res.data.result.type.split(',')
						this.pic_path = res.data.result.cover
						this.info = res.data.result.state
						this.author = res.data.result.author
					}
					else if (res.data.type == "novel"){
						this.tag = 2
						this.title = res.data.result.title
						this.author = res.data.result.author
						this.curr_link = res.data.result.url
						this.pic_path = res.data.result.cover
						this.score = res.data.result.score
						this.biaoqian = res.data.result.type.split(',')
						this.brief = res.data.result.introduce
						this.update = res.data.result.update_time
						this.score_num = res.data.result.cm_count
					}
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
			collect(){
				if (this.is_collect == false){
					this.is_collect = true;
				}
				else{
					this.is_collect = false;
				}
			},
			pingfen(i){
				console.log("click:  ", i);
				console.log("before:", this.pingfen_num);
				this.is_pingfen = true;
				this.pingfen_num = i;
				console.log("after:", this.pingfen_num);
			},
			// 跳转详情页
			toDetail(t, i){
				// console.log("ToDetail:")
				// console.log("dm:  ",this.rec_dm_id_list)
				// console.log("mh:  ",this.rec_mh_id_list)
				// console.log("xs:  ",this.rec_xs_id_list)
				// console.log("cp:  ",this.rec_cp_id_list)
				if (t == 0){
					// 打开动漫新标签页
					var { href } = this.$router.resolve({ path: "detail", query: { id:this.id, name: this.name, idfr: this.rec_dm_id_list[i] } }); 
					window.open(href, '_blank');
				}
				else if (t == 1){
					// 打开漫画新标签页
					var { href } = this.$router.resolve({ path: "detail", query: { id:this.id, name: this.name, idfr: this.rec_mh_id_list[i] } }); 
					window.open(href, '_blank');
				}
				else if (t == 2){
					// 打开漫画新标签页
					var { href } = this.$router.resolve({ path: "detail", query: { id:this.id, name: this.name, idfr: this.rec_xs_id_list[i] } }); 
					window.open(href, '_blank');
				}
				
			},
			toSource(){
				// 打开新标签页
				var href = this.curr_link;
				window.open(href, '_blank');
			},
			// 换一换
			change_change(t){
				if (t == 0){
					uni.request({
						url: 'http://124.70.91.77:8000/api/hot/anime?uid=' + this.id,
						method: 'GET',
						success: res => {
							console.log(res)
							this.rec_dm_id_list = res.data.result.aid
							this.rec_dm_name_list = res.data.result.title
							this.rec_dm_pic_list = res.data.result.cover
						},
					})
				}
				else if (t == 1){
					uni.request({
						url: 'http://124.70.91.77:8000/api/hot/comic?uid=' + this.id,
						method: 'GET',
						success: res => {
							console.log(res)
							this.rec_mh_id_list = res.data.result.cid
							this.rec_mh_name_list = res.data.result.title
							this.rec_mh_pic_list = res.data.result.cover
						},
					})
				}
				else if (t == 2){
					uni.request({
						url: 'http://124.70.91.77:8000/api/hot/novel?uid=' + this.id,
						method: 'GET',
						success: res => {
							console.log(res)
							this.rec_xs_id_list = res.data.result.nid
							this.rec_xs_name_list = res.data.result.title
							this.rec_xs_pic_list = res.data.result.cover
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

	.detail-box{
		margin-top: calc(1%);
		margin-left: calc(5%);
		margin-right: calc(5%);
		margin-bottom: calc(5%);
		position: absolute;
		width: 2750rpx;
		height: 730rpx;
		line-height: 2;
		border-radius: 5px;
		background: rgba(255, 255, 255, .3);
		overflow: hidden;
	}
	.detail-glass{
		width: 2750rpx;
		height: 730rpx;
		
		-webkit-filter: blur(10px); /* Chrome, Opera */
		   -moz-filter: blur(10px);
		    -ms-filter: blur(10px);    
		        filter: blur(60px); 
	}
	.detail-img{
		margin-top: calc(2%);
		margin-left: calc(3%);
		height: 610rpx;
		width: 450rpx;
		position: absolute;
		z-index:2;
		border-radius: 2%;
		border: 5rpx solid #ffffff;
	}
	.detail-title{
		margin-top: calc(2%);
		margin-left: calc(22%);
		/* font-family: cute; */
		font-weight: 600;
		font-size: 40rpx;
		color: #ffffff;
		position: absolute;
		z-index:2;
	}
	.detail-biaoqian0{
		margin-top: calc(5%);
		margin-left: calc(22%);
		width: 160rpx;
		height: 40rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		line-height: 2;
		z-index:2;
/* 		border-radius: 15%;
		border: 3rpx solid #ffffffd9; */
	}
	.detail-biaoqian1{
		margin-top: calc(5%);
		margin-left: calc(26%);
		width: 80rpx;
		height: 40rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
		border-radius: 15%;
		border: 3rpx solid #ffffffd9;
	}
	.detail-biaoqian2{
		margin-top: calc(5%);
		margin-left: calc(30%);
		width: 80rpx;
		height: 40rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
		border-radius: 15%;
		border: 3rpx solid #ffffffd9;
	}
	.detail-biaoqian3{
		margin-top: calc(5%);
		margin-left: calc(34%);
		width: 80rpx;
		height: 40rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
		border-radius: 15%;
		border: 3rpx solid #ffffffd9;
	}
	.detail-play{
		margin-top: calc(8%);
		margin-left: calc(21%);
		width: 150rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
		/* border-radius: 20%; */
		border-right: 3rpx solid #ffffff87;;
	}
	.detail-danmu{
		margin-top: calc(8%);
		margin-left: calc(26%);
		width: 150rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-author{
		margin-top: calc(8%);
		margin-left: calc(22%);
		width: 300rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-score{
		margin-top: calc(8%);
		margin-left: calc(75%);
		width: 130rpx;
		height: 30rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	
	.detail-star-0{
		margin-top: calc(8%);
		margin-left: calc(80%);
		width: 130rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-star-1{
		margin-top: calc(8%);
		margin-left: calc(81% + 3px);
		width: 130rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-star-2{
		margin-top: calc(8%);
		margin-left: calc(82% + 6px);
		width: 130rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-star-3{
		margin-top: calc(8%);
		margin-left: calc(83% + 9px);
		width: 130rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-star-4{
		margin-top: calc(8%);
		margin-left: calc(84% + 12px);
		width: 130rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-score-num{
		margin-top: calc(10%);
		margin-left: calc(80%);
		width: 170rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-info{
		margin-top: calc(12%);
		margin-left: calc(22%);
		width: 220rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-brief{
		margin-top: calc(14% + 6px);
		margin-left: calc(22%);
		width: 2000rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-link{
		margin-top: calc(16% + 10px);
		margin-left: calc(22%);
		position: absolute;
		z-index:2;
	}
	.detail-collect{
		margin-top: calc(21% + 5px);
		margin-left: calc(40%);
		position: absolute;
		z-index:2;
	}
	.detail-pingfen{
		position: absolute;
		z-index:2;
		border: 2px solid #ffffff;
		width:  450rpx; 
		height: 75rpx; 
		margin-top: calc(21% + 5px); 
		margin-left: calc(50%);
		border-top-right-radius: 100px;
		border-top-left-radius: 100px;
		border-bottom-left-radius: 100px;
		border-bottom-right-radius: 100px;
	}
	.detail-pingfen-0{
		cursor:pointer;
		text-decoration:none;
		margin-top: 5rpx;
		margin-left: 10rpx;
		width: 130rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:2;
	}
	.detail-pingfen-1{
		cursor:pointer;
		text-decoration:none;
		margin-top: 5rpx;
		margin-left: 70rpx;
		width: 130rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:3;
	}
	.detail-pingfen-2{
		cursor:pointer;
		text-decoration:none;
		margin-top: 5rpx;
		margin-left: 130rpx;
		width: 130rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:4;
	}
	.detail-pingfen-3{
		cursor:pointer;
		text-decoration:none;
		margin-top: 5rpx;
		margin-left: 190rpx;
		width: 130rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:5;
	}
	.detail-pingfen-4{
		margin-top: 5rpx;
		margin-left: 250rpx;
		width: 130rpx;
		height: 70rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		z-index:6;
	}
	
	.recommand{
		margin-top: calc(1%);
		margin-left: calc(5%);
		margin-right: calc(5%);
		margin-bottom: calc(5%);
		width: 2750rpx;
		height: 2750rpx;
		background: rgba(255, 255, 255, .3);
		background-color: #f4f5f7;
	}
	.recommand-content{
		margin-left: calc(4%);
		margin-right: calc(4%);
		background-color: #ffffff;
	}
	.rec_content_title{
		margin-top: 10px;
		font-family: cute;
		font-size: 12px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.rec_content_image{
		margin-top: 10px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	div{
		list-style: none;
		transition: .3s linear;
	}
	div:hover{
		transform: scale(1.1);    /*盒子放大*/
	}
	div::before, div::after{
	    position: absolute;
	    content: '';
	    transition: 1.3s ease-out ;
	}
</style>
