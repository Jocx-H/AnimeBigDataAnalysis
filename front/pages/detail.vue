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
					<text class="portrait-txt">
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
		<!-- 详情信息 -->
		<view class="detail-box">
			<!-- 封面 -->
			<image class="detail-img" :src="pic_path" mode="heightFix"></image>
			<!-- 标题 -->
			<text class="detail-title"> {{title}} </text>
			<view class="detail-biaoqian0">
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{biaoqian[0]}} </text>
			</view>
			<view class="detail-biaoqian1">
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{biaoqian[1]}} </text>
			</view>
			<view class="detail-biaoqian2">
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{biaoqian[2]}} </text>
			</view>
			<view class="detail-biaoqian3">
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{biaoqian[3]}} </text>
			</view>
			<!-- 总播放量、弹幕总数、评分、是否完结、共xx话-->
			<view class="detail-play">
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> 总播放 </text>
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{total_play}} </text>
			</view>
			<view class="detail-danmu">
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> 弹幕总数 </text>
				<text style="line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{total_danmu}} </text>
			</view>
			<view class="detail-score"> 
				<text style="font-size: 70rpx; color: #fea726; line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{score}} </text>
			</view>
			<u-icon class="detail-star-0" name="star" color="#fea726" ></u-icon>
			<u-icon class="detail-star-1" name="star" color="#fea726" ></u-icon>
			<u-icon class="detail-star-2" name="star" color="#fea726" ></u-icon>
			<u-icon class="detail-star-3" name="star" color="#fea726" ></u-icon>
			<u-icon class="detail-star-4" name="star" color="#fea726" ></u-icon>
			<u-icon class="detail-star-0" name="star-fill" v-if="score>=1.5" color="#fea726" ></u-icon>
			<u-icon class="detail-star-1" name="star-fill" v-if="score>=3.5" color="#fea726" ></u-icon>
			<u-icon class="detail-star-2" name="star-fill" v-if="score>=5.5" color="#fea726" ></u-icon>
			<u-icon class="detail-star-3" name="star-fill" v-if="score>=7.5" color="#fea726" ></u-icon>
			<u-icon class="detail-star-4" name="star-fill" v-if="score>=9.5" color="#fea726" ></u-icon>
			<view class="detail-score-num">
				<text style="font-size: 15rpx; color: #ffffff; line-height: 1.5;display: flex;align-items: center;justify-content: center;"> {{score_num}}人点评 </text>
			</view>
			<view class="detail-info">
				<text>{{info}}</text>
			</view>
			<!-- 简介 -->
			<view class="detail-brief">
				<text>简介：{{brief}}</text>
			</view>
			
			<!-- 原网页链接 -->
			<view class="detail-link">
				<image src="../static/tobili_dm.png" style="height: 120rpx;" mode="heightFix" v-if="tag==0" @click="toSource()"></image>
				<image src="../static/tobili_mh.png" style="height: 120rpx;" mode="heightFix" v-if="tag==1" @click="toSource()"></image>
				<image src="../static/tobili_xs.png" style="height: 120rpx;" mode="heightFix" v-if="tag==2" @click="toSource()"></image>
			</view>
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
								<u-button type="primary" size="small" :plain="true" color="#61666d" shape="circle" icon="reload" text="换一换"></u-button>
							</view>
						</uni-col>
					</uni-row>
					<uni-row>
						<uni-col :span="4" v-for="(item, i) in temp_6" :key="i+'b'">
							<view class="rec_content_image">
								<image style="width: 350rpx;" :src="rec_dm_pic_list[item]" mode="aspectFit" @click="toDetail(rec_dm_id_list[item])"></image>
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
								<u-button type="primary" size="small" :plain="true" color="#61666d" shape="circle" icon="reload" text="换一换"></u-button>
							</view>
						</uni-col>
					</uni-row>
					<uni-row>
						<uni-col :span="4" v-for="(item, i) in temp_6" :key="i+'b'">
							<view class="rec_content_image">
								<image style="width: 390rpx;" :src="rec_mh_pic_list[i]" mode="aspectFit" @click="toDetail(rec_mh_id_list[item])"></image>
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
								<u-button type="primary" size="small" :plain="true" color="#61666d" shape="circle" icon="reload" text="换一换"></u-button>
							</view>
						</uni-col>
					</uni-row>
					<uni-row>
						<uni-col :span="4" v-for="(item, i) in temp_6" :key="i+'b'">
							<view class="rec_content_image">
								<image style="width: 390rpx;" :src="rec_xs_pic_list[i]" mode="aspectFit" @click="toDetail(rec_xs_id_list[item])"></image>
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
				name: "miao",	// 用户昵称
				title: "青春猪头少年不会梦到兔女郎学姐",		// 题目
				biaoqian: ["小说改","恋爱","奇幻","校园"],	// 标签
				total_play: 2100,			// 播放量
				total_danmu: 410,			// 弹幕总数
				score: 9.8,					// 总评分
				score_num: 155392,			// 评分人数
				info: "已完结，全13话",		// 完结信息和集数
				is_collect: false,			// 是否收藏
				pingfen_num: 0,				// 评分分数
				is_pingfen: false,			// 是否评分
				curr_link: "https://www.bilibili.com/bangumi/play/ss25733",		// 当前的原视频链接
				brief: "青春期症候群——这是一种只发生在易敏感和不稳定的青春期的、不可思议的现象。例如，在梓川咲太面前出现的野生兔女郎。她的真实身份是高中高年级学生，明星活动休止的女演员樱岛麻衣。她迷人的身姿，不知为何在周围的人眼里看不出来。咲太决定解开这一谜题。在与麻衣一起度过的时间里，咲太知道了她秘密的想法……女主人公们一个接一个地出现在咲太的周围，她们都有着“青春期症候群”。在天空和大海都很闪耀的小镇上，开始了令人激动的故事。",					// 简介
				pic_path: "http://i0.hdslb.com/bfs/bangumi/1cc333ff578e5ea9fded7e454953a4e2291440c2.png",	// 图片
				// 动漫、漫画、小说推荐的封面图片
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
				// 动漫、漫画、小说推荐的标题
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
				// 动漫、漫画、小说推荐的标识符，用于跳转详情页
				rec_dm_id_list:["001","002","003","004","005","006","007","008","009","010","011","012"],
				rec_mh_id_list:["001","002","003","004","005","006","007","008","009","010","011","012"],
				rec_xs_id_list:["001","002","003","004","005","006","007","008","009","010","011","012"],
			}
		},
		onLoad(option) {
			this.idenfr = option.idnfr
			// 【Todo】后端获取tag
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
			toDetail(idenfr){
				// 打开新标签页
				var { href } = this.$router.resolve({ path: "detail", query: { idfr: idenfr } }); 
				window.open(href, '_blank');
			},
			toSource(){
				// 打开新标签页
				var href = this.curr_link;
				window.open(href, '_blank');
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
		        filter: blur(13px); 
	}
	.detail-img{
		margin-top: calc(2%);
		margin-left: calc(3%);
		height: 610rpx;
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
		width: 80rpx;
		height: 40rpx;
		font-size: 20rpx;
		color: #ffffffd9;
		position: absolute;
		line-height: 2;
		z-index:2;
		border-radius: 15%;
		border: 3rpx solid #ffffffd9;
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
		width: 130rpx;
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
		width: 130rpx;
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
		height: 70rpx;
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
		margin-left: calc(5%);
		margin-right: calc(5%);
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
</style>
