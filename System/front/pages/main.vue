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
						<image style="height: 40px;float: left;" mode="heightFix" src="../static/dilidili.png">
						</image>
					</view>
				</uni-col>
				<!-- 用户头像 -->
				<uni-col :span="2">
					<view class="portrait">
						<image @click="navi_my()"  style="height: 40px; width: 40px; display: block; margin: 0 auto;border-radius: 50%;  border: 3rpx solid #ffb9d4;" src="../static/portrait.jpg">
						</image>
					</view>
					<text v-if="tag==0"  class="portrait-txt">
						{{this.name}}
					</text>
				</uni-col>
				<!-- 足迹 -->
				<uni-col :span="2">
					<view class="foot">
						<image @click="navi_my()" style="width: 42px; display: block; margin: 0 auto;" mode="widthFix" src="../static/foot.png">
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
			<!-- 二级标签 -->
			<uni-row>
				<!-- 动漫的二级标签 -->
				<uni-col :span="1" v-if="tag == 0" v-for="(item, j) in dm_list" :key="j+'b'">
					<button class="btn_2st" @click="change_dm_list(j)">
						<text :style="{'color': (index==j ? '#ffb9d4':'#61666d')}">{{dm_list[j]}}</text>
					</button>
				</uni-col>
				<!-- 漫画的二级标签 -->
				<uni-col :span="1" v-if="tag == 1" v-for="(item, j) in mh_list" :key="j+'b'">
					<button class="btn_2st" @click="change_mh_list(j)">
						<text :style="{'color': (index==j ? '#ffb9d4':'#61666d')}">{{mh_list[j]}}</text>
					</button>
				</uni-col>
				<!-- 小说的二级标签 -->
				<uni-col :span="1" v-if="tag == 2" v-for="(item, j) in xs_list" :key="j+'b'">
					<button class="btn_2st" @click="change_xs_list(j)">
						<text :style="{'color': (index==j ? '#ffb9d4':'#61666d')}">{{xs_list[j]}}</text>
					</button>
				</uni-col>
				<!-- cosplay的二级标签 -->
				<uni-col :span="1" v-if="tag == 3" v-for="(item, j) in cp_list" :key="j+'b'">
					<button class="btn_2st" @click="change_cp_list(j)">
						<text :style="{'color': (index==j ? '#ffb9d4':'#61666d')}">{{cp_list[j]}}</text>
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
						<u-button type="primary" :plain="true" color="#61666d" shape="circle" icon="reload" text="换一换"></u-button>
					</view>
				</uni-col>
			</uni-row>
			<!-- 推荐的动漫、漫画、小说 -->
			<view v-if="tag!=3" class="rec_content">
				<uni-row>
					<uni-col :span="4" v-for="(item, i) in temp_6" :key="i+'b'">
						<!-- 动漫 -->
						<view class="rec_content_image">
							<image v-if="tag==0" style="width: 350rpx;" :src="rec_dm_pic_list[item]" mode="aspectFit" @click="toDetail(rec_dm_id_list[item])"></image>
						</view>
						<text v-if="tag==0" class="rec_content_title"> {{rec_dm_name_list[item]}} </text>
						<!-- 漫画-->
						<view class="rec_content_image">
							<image v-if="tag==1" style="width: 390rpx;" :src="rec_mh_pic_list[i]" mode="aspectFit" @click="toDetail(rec_mh_id_list[item])"></image>
						</view>
						<text v-if="tag==1" class="rec_content_title"> {{rec_mh_name_list[item]}} </text>
						<!-- 小说 -->
						<view class="rec_content_image">
							<image v-if="tag==2" style="width: 390rpx;" :src="rec_xs_pic_list[i]" mode="aspectFit" @click="toDetail(rec_xs_id_list[item])"></image>
						</view>
						<text v-if="tag==2" class="rec_content_title"> {{rec_xs_name_list[item]}} </text>
					</uni-col>
				</uni-row>
				<uni-row>
					<uni-col :span="4" v-for="(item, i) in temp_12" :key="i+'b'">
						<!-- 动漫 -->
						<view class="rec_content_image">
							<image v-if="tag==0" style="width: 390rpx;" :src="rec_dm_pic_list[item]" mode="aspectFit" @click="toDetail(rec_dm_id_list[item])"></image>
						</view>
						<text v-if="tag==0" class="rec_content_title"> {{rec_dm_name_list[item]}} </text>
						<!-- 漫画-->
						<view class="rec_content_image">
							<image v-if="tag==1" style="width: 390rpx;" :src="rec_mh_pic_list[item]" mode="aspectFit" @click="toDetail(rec_mh_id_list[item])"></image>
						</view>
						<text v-if="tag==1" class="rec_content_title"> {{rec_mh_name_list[item]}} </text>
						<!-- 小说 -->
						<view class="rec_content_image">
							<image v-if="tag==2" style="width: 390rpx;" :src="rec_xs_pic_list[item]" mode="aspectFit" @click="toDetail(rec_xs_id_list[item])"></image>
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
							<image v-if="tag==3" style="width: 370rpx;" :src="rec_cp_pic_list[item]"  mode="aspectFit"></image>
						</view>
						<text v-if="tag==3" class="rec_content_title"> {{rec_cp_name_list[0]}} </text>
					</uni-col>
				</uni-row>
				<uni-row>
					<uni-col :span="4" v-for="(item, i) in temp_12" :key="i+'b'">
						<!-- cosplay -->
						<view class="rec_content_image_cp">
							<image v-if="tag==3" style="width: 370rpx;" :src="rec_cp_pic_list[item]"  mode="aspectFit"></image>
						</view>
						<text v-if="tag==3" class="rec_content_title"> {{rec_cp_name_list[0]}} </text>
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
				index: 0,		// 二级分类标签
				// 二级标签列表
				dm_list: ["原创", "校园", "恋爱", "悬疑", "热血"],
				mh_list: ["搞笑", "治愈", "冒险", "推理", "偶像", "少儿"],
				xs_list: ["奇幻", "穿越", "原创"],
				cp_list: ["冒险", "奇幻", "校园", "萝莉", "御姐"],
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
				rec_dm_pic_list:[
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
					"http://i0.hdslb.com/bfs/bangumi/image/f5128c939b24909c7cb75bab51be0ee0c4d1b33a.jpg"
				],
				rec_mh_pic_list:[
					"https://images.dmzj.com/img/webpic/4/1447215436.jpg",
					"https://images.dmzj.com/img/webpic/4/1447215436.jpg",
					"https://images.dmzj.com/img/webpic/4/1447215436.jpg",
					"https://images.dmzj.com/img/webpic/4/1447215436.jpg",
					"https://images.dmzj.com/img/webpic/4/1447215436.jpg",
					"https://images.dmzj.com/img/webpic/4/1447215436.jpg",
					"https://images.dmzj.com/img/webpic/7/1002475871439187470.jpg",
					"https://images.dmzj.com/img/webpic/7/1002475871439187470.jpg",
					"https://images.dmzj.com/img/webpic/7/1002475871439187470.jpg",
					"https://images.dmzj.com/img/webpic/7/1002475871439187470.jpg",
					"https://images.dmzj.com/img/webpic/7/1002475871439187470.jpg",
					"https://images.dmzj.com/img/webpic/7/1002475871439187470.jpg"
				],
				rec_xs_pic_list:[
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg",
					"http://rs.sfacg.com/web/novel/images/NovelCover/Big/2022/05/a4f1a5cf-3dd0-4084-b401-ae72d941311d.jpg"
				],
				rec_cp_pic_list:[
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
					"http://www.cosplay8.com/uploads/allimg/220617/112879-22061G531320-L.jpg",
				],
				// 动漫、漫画、小说、cosplay推荐的标题
				rec_dm_name_list:[
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
					"四月是你的谎言"
				],
				rec_mh_name_list:[
					"妖神记",
					"妖神记",
					"妖神记",
					"妖神记",
					"妖神记",
					"妖神记",
					"我家大师兄脑子有坑",
					"我家大师兄脑子有坑",
					"我家大师兄脑子有坑",
					"我家大师兄脑子有坑",
					"我家大师兄脑子有坑",
					"我家大师兄脑子有坑"
				],
				rec_xs_name_list:[
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我",
					"被病娇师尊追赶的我"
				],
				rec_cp_name_list:[
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇",
					"《东方Project》圣诞礼遇"
				],
				// 动漫、漫画、小说、cosplay推荐的标识符，用于跳转详情页
				rec_dm_id_list:["001","002","003","004","005","006","007","008","009","010","011","012"],
				rec_mh_id_list:["001","002","003","004","005","006","007","008","009","010","011","012"],
				rec_xs_id_list:["001","002","003","004","005","006","007","008","009","010","011","012"],
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
			clickSwiper(){
				this.curr_swiper_link = this.swiper_link_list[this.curr_swiper];
				// 打开新标签页
				var href = this.curr_swiper_link;
				window.open(href, '_blank');
			},
			// 跳转详情页
			toDetail(idenfr){
				// 打开新标签页
				var { href } = this.$router.resolve({ path: "detail", query: { idfr: idenfr } }); 
				window.open(href, '_blank');
			},
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
