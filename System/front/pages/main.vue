<!--
@File   : main.vue
@Time   : 2022/6/21 ‏‎16:11:44
@Author : Sparkling-Y
@Desc   : 主页
-->

<template>
	<view>
		<!-- 导航栏 -->
		<view class="navi">
			<uni-row>
				<!-- dilidili图标 -->
				<uni-col :span="16">
					<view class="dilidili">
						<image style="height: 40px;float: left;cursor:pointer;text-decoration:none;" mode="heightFix" src="../static/dilidili.png">
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
		<!-- 标签选择 -->
		<view class="tag-box">
			<!-- 一级标签 -->
			<uni-row>
				<uni-col :span="2">
					<button class="btn_1st" @click="change_dm()">
						<text :style="{'color': (tag==0 ? '#ffb9d4':'#61666d')}" style="line-height: 50rpx; font-size: 50rpx;">动漫</text>
					</button>
				</uni-col>
				<uni-col :span="2">
					<button class="btn_1st" @click="change_mh()">
						<text :style="{'color': (tag==1 ? '#ffb9d4':'#61666d')}" style="line-height: 50rpx; font-size: 45rpx;">漫画</text>
					</button>
				</uni-col>
				<uni-col :span="2">
					<button class="btn_1st" @click="change_xs()">
						<text :style="{'color': (tag==2 ? '#ffb9d4':'#61666d')}" style="line-height: 50rpx; font-size: 45rpx;">小说</text>
					</button>
				</uni-col>
				<uni-col :span="2">
					<button class="btn_1st" @click="change_cp()">
						<text :style="{'color': (tag==3 ? '#ffb9d4':'#61666d')}" style="line-height: 50rpx; font-size: 45rpx;">Cosplay</text>
					</button>
				</uni-col>
			</uni-row>
		</view>
		<!-- 轮播图 -->
		<view class="swiper-box">
			<u-swiper height="350px" :list="swiper_list" indicator indicatorMode="line" indicatorActiveColor="#ffa4c3" keyName="image" :autoplay="true" :circular="true" @change="e => curr_swiper = e.current" @click="clickSwiper">
			</u-swiper>
		</view>
		<!-- 推荐内容 -->
		<view class="rec_box">
			<!-- “猜您喜欢”  “换一换” -->
			<uni-row>
				<uni-col :span="12">
					<text style="float: left; margin-left: calc(20%);font-family: cute; font-size: 24px;">猜您喜欢</text>
				</uni-col>
				<uni-col :span="12">
					<view style="width: 100px; float: right; margin-right: calc(20%);">
						<u-button type="primary" :plain="true" color="#61666d" shape="circle" icon="reload" text="换一换" @click="change_change(tag)"></u-button>
					</view>
				</uni-col>
			</uni-row>
			<!-- 推荐的动漫、漫画、小说 -->
			<view v-if="tag!=3" class="rec_content">
				<uni-row>
					<uni-col :span="4" v-for="(item, i) in temp_6" :key="i+'b'">
						<!-- 动漫 -->
						<view class="rec_content_image">
							<image v-if="tag==0" style="cursor:pointer;text-decoration:none;width: 350rpx;border-top-left-radius: 15px; border-top-right-radius: 15px;border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;" :src="rec_dm_pic_list[item]" mode="aspectFill" @click="toDetail(0, item)"></image>
						</view>
						<text v-if="tag==0" class="rec_content_title"> {{rec_dm_name_list[item]}} </text>
						<!-- 漫画 -->
						<view class="rec_content_image">
							<image v-if="tag==1" style="cursor:pointer;text-decoration:none;width: 360rpx;border-top-left-radius: 15px; border-top-right-radius: 15px;border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;" :src="rec_mh_pic_list[item]" mode="aspectFill" @click="toDetail(1, item)"></image>
						</view>
						<text v-if="tag==1" class="rec_content_title"> {{rec_mh_name_list[item]}} </text>
						<!-- 小说 -->
						<view class="rec_content_image">
							<image v-if="tag==2" style="cursor:pointer;text-decoration:none;width: 360rpx;border-top-left-radius: 15px; border-top-right-radius: 15px;border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;" :src="rec_xs_pic_list[item]" mode="aspectFill" @click="toDetail(2, item)"></image>
						</view>
						<text v-if="tag==2" class="rec_content_title"> {{rec_xs_name_list[item]}} </text>
					</uni-col>
				</uni-row>
				<uni-row>
					<uni-col :span="4" v-for="(item, i) in temp_12" :key="i+'b'">
						<!-- 动漫 -->
						<view class="rec_content_image">
							<image v-if="tag==0" style="cursor:pointer;text-decoration:none;width: 350rpx;border-top-left-radius: 15px; border-top-right-radius: 15px;border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;" :src="rec_dm_pic_list[item]" mode="aspectFill" @click="toDetail(0, item)"></image>
						</view>
						<text v-if="tag==0" class="rec_content_title"> {{rec_dm_name_list[item]}} </text>
						<!-- 漫画-->
						<view class="rec_content_image">
							<image v-if="tag==1" style="cursor:pointer;text-decoration:none;width: 360rpx;border-top-left-radius: 15px; border-top-right-radius: 15px;border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;" :src="rec_mh_pic_list[item]" mode="aspectFill" @click="toDetail(1, item)"></image>
						</view>
						<text v-if="tag==1" class="rec_content_title"> {{rec_mh_name_list[item]}} </text>
						<!-- 小说 -->
						<view class="rec_content_image">
							<image v-if="tag==2" style="cursor:pointer;text-decoration:none;width: 360rpx;border-top-left-radius: 15px; border-top-right-radius: 15px;border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;" :src="rec_xs_pic_list[item]" mode="aspectFill" @click="toDetail(2, item)"></image>
						</view>
						<text v-if="tag==2" class="rec_content_title"> {{rec_xs_name_list[item]}} </text>
					</uni-col>
				</uni-row>
			</view>
			<!-- 推荐的cosplay -->
			<view v-if="tag == 3" class="rec_content_cp">
				<uni-row>
					<uni-col :span="4" v-for="(item, i) in temp_6" :key="i+'b'">
						<!-- cosplay -->
						<view class="rec_content_image_cp">
							<image @click="toWeb(i)" v-if="tag==3" style="cursor:pointer;text-decoration:none;width: 370rpx;border-top-left-radius: 10px; border-top-right-radius: 10px;border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;" :src="rec_cp_pic_list[item]"  mode="aspectFill" ></image>
						</view>
						<text v-if="tag==3" class="rec_content_title"> {{rec_cp_name_list[item]}} </text>
					</uni-col>
				</uni-row>
				<uni-row>
					<uni-col :span="4" v-for="(item, i) in temp_12" :key="i+'b'">
						<!-- cosplay -->
						<view class="rec_content_image_cp">
							<image @click="toWeb(i)" v-if="tag==3" style="cursor:pointer;text-decoration:none;width: 370rpx;border-top-left-radius: 10px; border-top-right-radius: 10px;border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;" :src="rec_cp_pic_list[item]"  mode="aspectFill"></image>
						</view>
						<text v-if="tag==3" class="rec_content_title"> {{rec_cp_name_list[item]}} </text>
					</uni-col>
				</uni-row>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				temp_6: [0,1,2,3,4,5],
				temp_12: [6,7,8,9,10,11],
				id:   0,		// 用户名
				name: "miao",	// 用户昵称
				tag:  0,		// 一级分类标签，0为动漫，1为漫画，2为小说，3为cosplay
				// 轮播图
				curr_swiper: 0,				// 当前的轮播图
				swiper_list: [{				// 轮播图的图片
					image: '../static/swiper_1.png',
					},{
					image: '../static/swiper_2.png',
					},{
					image: '../static/swiper_3.png',
					},{
					image: '../static/swiper_4.png',
					},{
					image: '../static/swiper_5.png',
				}],
				swiper_link_list: [			// 轮播图的链接
					"https://www.bilibili.com/bangumi/play/ep518291?from_spmid=666.4.0.0", 
					"https://www.bilibili.com/bangumi/play/ep515120?from_spmid=666.4.0.0", 
					"https://www.bilibili.com/bangumi/play/ep515368?from_spmid=666.4.0.0", 
					"https://www.bilibili.com/bangumi/play/ep478923?from_spmid=666.4.0.0", 
					"https://www.bilibili.com/bangumi/play/ss41410?spm_id_from=333.337.0.0"
				],
				curr_swiper_link: "",		// 当前轮播图的链接
				// 动漫、漫画、小说、cosplay推荐的图片
				rec_dm_pic_list:["","","","","","","","","","","",""],
				rec_mh_pic_list:["","","","","","","","","","","",""],
				rec_xs_pic_list:["","","","","","","","","","","",""],
				rec_cp_pic_list:["","","","","","","","","","","",""],
				// 动漫、漫画、小说、cosplay推荐的标题
				rec_dm_name_list:["","","","","","","","","","","",""],
				rec_mh_name_list:["","","","","","","","","","","",""],
				rec_xs_name_list:["","","","","","","","","","","",""],
				rec_cp_name_list:["","","","","","","","","","","",""],
				// 动漫、漫画、小说、cosplay推荐的标识符，用于跳转详情页
				rec_dm_id_list:[1,1,1,1,1,1,1,1,1,1,1,1,],
				rec_mh_id_list:[1,1,1,1,1,1,1,1,1,1,1,1,],
				rec_xs_id_list:[1,1,1,1,1,1,1,1,1,1,1,1,],
				rec_cp_id_list:[1,1,1,1,1,1,1,1,1,1,1,1,],
				// cosplay链接
				rec_cp_link_list: [],
			}
		},
		methods: {
			// 切换一级标签
			change_dm(){ this.tag=0; this.index=0;},		// 【Todo】请求获取轮播图
			change_mh(){ this.tag=1; this.index=0;},		// 【Todo】请求获取轮播图
			change_xs(){ this.tag=2; this.index=0;},		// 【Todo】请求获取轮播图
			change_cp(){ this.tag=3; this.index=0;},		// 【Todo】请求获取轮播图
			// 切换二级标签
			change_dm_list(i){ this.index = i; },		// 【Todo】请求获取二级标签的rec_某某_name_list 、 图片
			change_mh_list(i){ this.index = i; },		// 【Todo】请求获取二级标签的rec_某某_name_list 、 图片
			change_xs_list(i){ this.index = i; },		// 【Todo】请求获取二级标签的rec_某某_name_list 、 图片
			change_cp_list(i){ this.index = i; },		// 【Todo】请求获取二级标签的rec_某某_name_list 、 图片
			// 点击轮播图跳转
			clickSwiper(){
				this.curr_swiper_link = this.swiper_link_list[this.curr_swiper];
				// 打开新标签页
				var href = this.curr_swiper_link;
				window.open(href, '_blank');
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
			toWeb(i){
				var href = this.rec_cp_link_list[i];
				window.open(href, '_blank');
			},
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
				else if (t == 3){
					uni.request({
						url: 'http://124.70.91.77:8000/api/hot/cosplay?uid=' + this.id,
						method: 'GET',
						success: res => {
							console.log(res)
							this.rec_cp_id_list = res.data.result.cosid
							this.rec_cp_name_list = res.data.result.title
							this.rec_cp_pic_list = res.data.result.cover
							this.rec_cp_link_list = res.data.result.url
						},
					})
				}
			}
		},
		onLoad(option){
			this.id = option.id
			this.name = option.name
			this.tag = 0
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
			uni.request({
				url: 'http://124.70.91.77:8000/api/hot/cosplay?uid=' + this.id,
				method: 'GET',
				success: res => {
					console.log(res)
					this.rec_cp_id_list = res.data.result.cosid
					this.rec_cp_name_list = res.data.result.title
					this.rec_cp_pic_list = res.data.result.cover
					this.rec_cp_link_list = res.data.result.url
				},
			})
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
	
	.tag-box{
		margin-left: calc(10%);
	}
	.btn_1st{
		margin-top: calc(10%);
		margin-left: 10rpx;
		height: 80rpx;
		font-family: cute;
	}
	.btn_2st{
		margin-top: calc(10%);
		margin-left: 10rpx;
		height: 60rpx;
		font-family: cute;
		font-size: 10px;
	}
	.swiper-box{
		margin-top: calc(1%);
		margin-left: calc(10%);
		margin-right: calc(10%);
		margin-bottom: calc(1%);
	}
	button::after{
		border: none;
	}
	.rec_box{
		margin-bottom: calc(5%);
	}
	.rec_content{
		margin-left: calc(9%);
		margin-right: calc(9%);
	}
	.rec_content_title{
		margin-top: 10px;
		margin-bottom: 5px;
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
	.rec_content_cp{
		margin-left: calc(9%);
		margin-right: calc(9%);
	}
	.rec_content_image_cp{
		margin-top: 6px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
</style>
