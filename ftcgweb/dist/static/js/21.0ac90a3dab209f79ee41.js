webpackJsonp([21],{WBOU:function(e,t){},qb5Q:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s={name:"sortingstreet",data:function(){return{tableData:[],otableData:[],xtableData:[],cur_page:1,activeName:"",imagesUrl:[],jid:"",sid:"",multipleSelection:[],select_cate:"",select_word:"",del_list:[],is_search:!1,addVisible:!1,editVisible:!1,xaddVisible:!1,xeditVisible:!1,showtable:!0,form:{name:"",date:"",phone:""},idx:-1,pagenum:0,totalnum:0}},created:function(){var e=this;this.jid="",this.url="/testftcg/config/getStreets?token="+localStorage.token,this.$axios.get(this.url).then(function(t){1!=t.data.code?e.$message.error(t.data.msg):(t.data.code=1)?(e.tableData=t.data.data,e.activeName=e.tableData[0].name,e.jid=e.tableData[0].id,setTimeout(function(){e.getData(e.tableData[0].id)},300)):console.log("不知出啥问题了")})},computed:{},methods:{handleCurrentChange:function(e){var t=this;this.pagenum=e-1,this.otableData="",setTimeout(function(){t.getData(t.jid)},300)},getData:function(e){var t=this;this.url="/testftcg/sorting/getSortingStreet?streetId="+e+"&token="+localStorage.token+"&page="+this.pagenum+"&pageSize=10",this.$axios.get(this.url).then(function(e){1!=e.data.code?t.$message.error(e.data.msg):(e.data.code=1)?(console.log(e.data),t.totalnum=e.data.allPage,t.otableData=e.data.data,t.otableData.some(function(e){var a={0:"普通小区",1:"学校",2:"政府机关",3:"收储运公司"},s={0:"进行中",1:"审核中",2:"审核打回",3:"审核通过","-1":"已删除"};t.otableData.map(function(e){var t=e.type,o=e.state;return e.type=a[t]?a[t]:t,e.state=s[o]?s[o]:o,e})})):console.log("不知出啥问题了")})},handleClick:function(e,t){this.otableData="",this.jid=this.tableData[e.index].id,this.getData(this.jid),console.log(this.jid)},xgetData:function(e){var t=this;this.xtableData="",this.url="/testftcg/assessment/getAssessmentDetails?token="+localStorage.token+"&userAssessmentId="+e,this.$axios.get(this.url).then(function(e){1!=e.data.code?t.$message.error(e.data.msg):(e.data.code=1)?(t.xtableData=e.data.data.questionList,console.log(e)):console.log("不知出啥问题了")})},handlecheck:function(e,t){this.$message("查询数据")},handleDo:function(e,t){var a=this;this.$confirm("是否需要审核本条记录?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){a.$message.error("审核开发中")}).catch(function(){})},handleshowpic:function(e,t){console.log(t.id),console.log(e)},back:function(){this.showtable=!this.showtable},add:function(){this.addVisible=!0},timestampToTime:function(e,t){var a=new Date(e.createTime);return a.getFullYear()+"-"+((a.getMonth()+1<10?"0"+(a.getMonth()+1):a.getMonth()+1)+"-")+(a.getDate()+" ")+(a.getHours()+":")+(a.getMinutes()+":")+a.getSeconds()},addtable:function(){var e=this;null==this.form.addname||this.form.addrole?this.$message.error("请输入数据后再提交"):(this.url="/testftcg/config/baseConfigVillage?token="+localStorage.token+"&name="+this.form.addname+"&number="+this.form.addnumber+"&address="+this.form.addaddress+"&personCharge="+this.form.addpersonCharge+"&phone="+this.form.addphone+"&remarks="+this.form.addremarks,this.$axios.get(this.url).then(function(t){console.log(t),(t.status=200)?(e.addVisible=!1,e.$message.success("街道数据新增成功"),e.form.addname="",e.form.addnumber="",e.form.addaddress="",e.form.addpersonCharge="",e.form.addphone="",e.form.addremarks="",e.getData()):e.$message.error(t.data.msg)}))},xadd:function(e,t){this.xaddVisible=!0},xaddtable:function(){var e=this;null==this.form.xaddname?this.$message.error("请输入数据后再提交"):(this.url="/testftcg/config/baseConfigCommunity?token="+localStorage.token+"&name="+this.form.xaddname+"&number="+this.form.xaddnumber+"&address="+this.form.xaddaddress+"&personCharge="+this.form.xaddpersonCharge+"&phone="+this.form.xaddphone+"&remarks="+this.form.xaddremarks+"&streetId="+this.jid,this.$axios.get(this.url).then(function(t){console.log(t),(t.data.code=1)?(e.xaddVisible=!1,e.$message.success("街道数据新增成功"),e.form.xaddname="",e.form.xaddnumber="",e.form.xaddaddress="",e.form.xaddpersonCharge="",e.form.xaddphone="",e.form.xaddremarks="",e.xgetData(e.jid)):e.$message.error(t.data.msg)}))},filterTag:function(e,t){return t.tag===e},handleEdit:function(e,t){this.jid=t.id,this.editVisible=!0,this.form.name=this.otableData[e].name,this.form.number=this.otableData[e].number,this.form.address=this.otableData[e].address,this.form.personCharge=this.otableData[e].personCharge,this.form.phone=this.otableData[e].phone,this.form.remarks=this.otableData[e].remarks},saveEdit:function(e,t){var a=this;this.url="/testftcg/config/editBaseConfigVillage?token="+localStorage.token+"&name="+this.form.name+"&number="+this.form.number+"&address="+this.form.address+"&personCharge="+this.form.personCharge+"&phone="+this.form.phone+"&remarks="+this.form.remarks+"&streetId="+this.jid,this.$axios.get(this.url).then(function(e){console.log(e),(e.data.code=1)?(a.editVisible=!1,a.$message.success("街道数据编辑成功"),a.form.name="",a.form.number="",a.form.address="",a.form.personCharge="",a.form.phone="",a.form.remarks="",a.getData()):a.$message.error(e.data.msg)})},xhandleEdit:function(e,t){this.sid=t.id,this.xeditVisible=!0,this.form.name=this.xtableData[e].name,this.form.number=this.xtableData[e].number,this.form.address=this.xtableData[e].address,this.form.personCharge=this.xtableData[e].personCharge,this.form.phone=this.xtableData[e].phone,this.form.remarks=this.xtableData[e].remarks},xsaveEdit:function(e,t){var a=this;this.url="/testftcg/config/editBaseConfigCommunity?token="+localStorage.token+"&name="+this.form.name+"&number="+this.form.number+"&address="+this.form.address+"&personCharge="+this.form.personCharge+"&phone="+this.form.phone+"&remarks="+this.form.remarks+"&communityId="+this.sid,this.$axios.get(this.url).then(function(e){console.log(e),(e.data.code=1)?(a.xeditVisible=!1,a.$message.success("社区数据编辑成功"),a.form.name="",a.form.number="",a.form.address="",a.form.personCharge="",a.form.phone="",a.form.remarks="",a.xgetData(a.jid)):a.$message.error(e.data.msg)})},handleSelectionChange:function(e){this.multipleSelection=e},handleDelete:function(e,t){var a=this;this.idx=e,this.$confirm("此操作将删除本条街道数据, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){console.log(a.tableData[a.idx].id),a.url="/testftcg/config/deleteStreet?token="+localStorage.token+"&streetId="+a.tableData[a.idx].id,a.$axios.get(a.url).then(function(e){console.log(e),(e.status=200)?(a.xgetData(a.jid),a.$message.success("删除成功")):a.$message.error(e.data.msg),a.getData()})}).catch(function(){})},xhandleDelete:function(e,t){var a=this;console.log(t.id),this.$confirm("此操作将删除本条社区数据, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){a.url="/testftcg/config/deleteCommunity?token="+localStorage.token+"&communityId="+t.id,a.$axios.get(a.url).then(function(e){console.log(e),(e.status=200)?(a.xgetData(a.jid),a.$message.success("删除成功")):a.$message.error(e.data.msg),a.getData()})}).catch(function(){})}}},o={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"table"},[a("div",{directives:[{name:"show",rawName:"v-show",value:e.showtable,expression:"showtable"}],staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-lx-cascades"}),e._v(" 督导日志\n      ")])],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:!e.showtable,expression:"!showtable"}],staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-lx-cascades"}),e._v(" 督导日志--督导详情\n      ")])],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:e.showtable,expression:"showtable"}],staticClass:"container"},[a("div",{staticClass:"handle-box"},[a("el-tabs",{attrs:{type:"card"},on:{"tab-click":e.handleClick},model:{value:e.activeName,callback:function(t){e.activeName=t},expression:"activeName"}},e._l(e.tableData,function(e){return a("el-tab-pane",{key:e.id,attrs:{label:e.name,name:e.name}})}))],1),e._v(" "),a("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:e.otableData,border:""},on:{"selection-change":e.handleSelectionChange}},[a("el-table-column",{attrs:{prop:"id",label:"id",width:"50"}}),e._v(" "),a("el-table-column",{attrs:{prop:"villageInfo.name",label:"小区名",width:"120"}}),e._v(" "),a("el-table-column",{attrs:{prop:"communityInfo.name",label:"社区名",width:"80"}}),e._v(" "),a("el-table-column",{attrs:{prop:"householdInfo",label:"住户",width:"130"}}),e._v(" "),a("el-table-column",{attrs:{prop:"remarks",label:"描述",width:"270"}}),e._v(" "),a("el-table-column",{attrs:{prop:"userInfo.name",label:"督导人",width:"80"}}),e._v(" "),a("el-table-column",{attrs:{prop:"createTime",formatter:e.timestampToTime,label:"提交时间",width:"160"}}),e._v(" "),a("el-table-column",{attrs:{prop:"url",label:"图片",width:"90"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-popover",{attrs:{placement:"left",title:"大图",trigger:"hover"}},[a("img",{staticStyle:{width:"460px",height:"680px"},attrs:{src:t.row.imgs[0].url,alt:""}}),e._v(" "),a("img",{staticStyle:{"max-height":"50px","max-width":"50px"},attrs:{slot:"reference",src:t.row.imgs[0].url,alt:t.row.imgs[0].url},slot:"reference"})])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"120",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{type:"text",icon:"el-icon-info"},on:{click:function(a){e.handlecheck(t.$index,t.row)}}},[e._v("查看详情")])]}}])})],1),e._v(" "),a("div",{staticClass:"pagination"},[a("el-pagination",{attrs:{background:"",layout:"prev, pager, next",total:e.totalnum},on:{"current-change":e.handleCurrentChange}})],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:!e.showtable,expression:"!showtable"}],staticClass:"container"},[a("div",{staticClass:"handle-box"},[a("el-button",{staticClass:"add",attrs:{type:"primary",icon:"search"},on:{click:e.back}},[e._v("返回")])],1),e._v(" "),a("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:e.xtableData,border:""},on:{"selection-change":e.handleSelectionChange}},[a("el-table-column",{attrs:{prop:"id",label:"id",width:"50"}}),e._v(" "),a("el-table-column",{attrs:{prop:"info",label:"问题",width:"340"}}),e._v(" "),a("el-table-column",{attrs:{prop:"fraction",label:"问题分数",width:"100"}}),e._v(" "),a("el-table-column",{attrs:{prop:"answerInfo.fraction",label:"考核得分",width:"100"}}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"260",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{slot:"reference"},on:{click:function(a){e.handleshowpic(t.$index,t.row)}},slot:"reference"},[e._v("查看图片")])]}}])})],1),e._v(" "),a("div",{staticClass:"pagination"})],1)])},staticRenderFns:[]};var r=a("VU/8")(s,o,!1,function(e){a("WBOU")},"data-v-3b50ae4b",null);t.default=r.exports}});