webpackJsonp([10],{ZiZD:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s={name:"officeassessment",data:function(){return{tableData:[],xtableData:[],aid:"",index:"",multipleSelection:[],select_cate:"",select_word:"",del_list:[],is_search:!1,addVisible:!1,delVisible:!1,editVisible:!1,xaddVisible:!1,xdelVisible:!1,showtable:!0,form:{name:"",date:"",phone:""},idx:-1}},created:function(){this.getData()},computed:{},methods:{objectSpanMethod:function(e){e.row,e.column,e.rowIndex,e.columnIndex},getData:function(){var e=this;this.url="/testftcg/config/getConfigAssessment?&subordinateType=2",this.$axios.get(this.url).then(function(t){if(t.status=200){var a=t.data.data;a.sort((s="req",function(e,t){return e[s]-t[s]})),a.some(function(e){var t={0:"减分项",1:"加分项"};a.map(function(e){var a=e.assessmentType;return e.assessmentType=t[a]?t[a]:a,e})}),e.tableData=a}else e.$message.error(t.data.msg);var s})},handlecheck:function(e,t){this.showtable=!this.showtable,this.aid=this.tableData[e].id,this.index=e,"{}"!=this.tableData[e].answerJson&&(this.xtableData=this.tableData[e].answerJson)},back:function(){this.showtable=!this.showtable},add:function(){this.addVisible=!0},addtable:function(){var e=this;null!=this.form.oneLevelName&&null!=this.form.shortName&&null!=this.form.fraction&&null!=this.form.info&&null!=this.form.assessmentType?(this.url="/testftcg/config/baseConfigAssessment?token="+localStorage.token+"&subordinateType= 2 &answerJson= {} &oneLevelName="+this.form.oneLevelName+"&shortName="+this.form.shortName+"&fraction="+this.form.fraction+"&info="+this.form.info+"&assessmentType="+this.form.assessmentType+"&req="+this.form.req,this.$axios.get(this.url).then(function(t){console.log(t),(t.data.code=1)?(e.addVisible=!1,e.$message.success("插入数据成功"),e.getData(),e.form.fraction="",e.form.info="",e.form.assessmentType="",e.form.shortName="",e.form.oneLevelName="",e.form.req="",e.getData()):e.$message.error("插入数据失败")})):this.$message.error("请输入数据后再提交")},xadd:function(e,t){var a=this;console.log(this.xtableData),this.$prompt("请输入答案名称","提示",{confirmButtonText:"确定",cancelButtonText:"取消",inputPlaceholder:"请输入新增的答案内容"}).then(function(e){var t=e.value;if(console.log(t),null==t)a.$message.error("输入点东西再改啊大哥");else{var s='{"des":"'+t+'"}';a.url="/testftcg/config/addAssessmentQuestion?token="+localStorage.token+"&id="+a.aid+"&desJson="+s,a.$axios.get(a.url).then(function(e){console.log(e),(e.data.code=1)?(a.$message.success("答案插入成功"),a.editVisible=!1):(a.$message.error(e.data.msg),a.editVisible=!1),a.getData(),setTimeout(function(){a.xtableData=a.tableData[a.index].answerJson},300)})}}).catch(function(){})},filterTag:function(e,t){return t.tag===e},handleEdit:function(e,t){this.editVisible=!0,this.aid=this.tableData[e].id,this.index=e,console.log(this.aid)},editVisible1:function(e){var t=this;this.$prompt("请输入一级指标","提示",{confirmButtonText:"确定",cancelButtonText:"取消",inputPlaceholder:this.tableData[this.index].oneLevelName}).then(function(e){var a=e.value;console.log(a),null==a?t.$message.error("输入点东西再改啊大哥"):(t.url="/testftcg/config/editConfigAssessment?token="+localStorage.token+"&id="+t.aid+"&oneLevelName="+a,t.$axios.get(t.url).then(function(e){console.log(e),(e.data.code=1)?(t.$message.success("数据修改成功"),t.editVisible=!1):(t.$message.error(e.data.msg),t.editVisible=!1),t.getData()}))}).catch(function(){})},editVisible2:function(){var e=this;this.$prompt("请输入二级指标","提示",{confirmButtonText:"确定",cancelButtonText:"取消",inputPlaceholder:this.tableData[this.index].shortName}).then(function(t){var a=t.value;console.log(a),null==a?e.$message.error("输入点东西再改啊大哥"):(e.url="/testftcg/config/editConfigAssessment?token="+localStorage.token+"&id="+e.aid+"&shortName="+a,e.$axios.get(e.url).then(function(t){console.log(t),(t.data.code=1)?(e.$message.success("数据修改成功"),e.editVisible=!1):(e.$message.error(t.data.msg),e.editVisible=!1),e.getData()}))}).catch(function(){})},editVisible3:function(){var e=this;this.$prompt("请输入分数(仅限数字)","修改数字可能导致历史数据不准",{confirmButtonText:"确定",cancelButtonText:"取消",inputPlaceholder:this.tableData[this.index].fraction}).then(function(t){var a=t.value;console.log(a),null==a?e.$message.error("输入点东西再改啊大哥"):(e.url="/testftcg/config/editConfigAssessment?token="+localStorage.token+"&id="+e.aid+"&fraction="+a,e.$axios.get(e.url).then(function(t){console.log(t),(t.data.code=1)?(e.$message.success("数据修改成功"),e.editVisible=!1):(e.$message.error(t.data.msg),e.editVisible=!1),e.getData()}))}).catch(function(){})},editVisible4:function(){var e=this;this.$prompt("请输入问题描述)","提示",{confirmButtonText:"确定",cancelButtonText:"取消",inputPlaceholder:this.tableData[this.index].info}).then(function(t){var a=t.value;console.log(a),null==a?e.$message.error("输入点东西再改啊大哥"):(e.url="/testftcg/config/editConfigAssessment?token="+localStorage.token+"&id="+e.aid+"&info="+a,e.$axios.get(e.url).then(function(t){console.log(t),(t.data.code=1)?(e.$message.success("数据修改成功"),e.editVisible=!1):(e.$message.error(t.data.msg),e.editVisible=!1),e.getData()}))}).catch(function(){})},editVisible5:function(){var e=this;this.$prompt("请输入排序值（仅限数字）","提示",{confirmButtonText:"确定",cancelButtonText:"取消",inputPlaceholder:this.tableData[this.index].req}).then(function(t){var a=t.value;console.log(a),null==a?e.$message.error("输入点东西再改啊大哥"):(e.url="/testftcg/config/editConfigAssessment?token="+localStorage.token+"&id="+e.aid+"&req="+a,e.$axios.get(e.url).then(function(t){console.log(t),(t.data.code=1)?(e.$message.success("数据修改成功"),e.editVisible=!1):(e.$message.error(t.data.msg),e.editVisible=!1),e.getData()}))}).catch(function(){})},xhandleEdit:function(e,t){var a=this;console.log(this.xtableData[e].index),this.$prompt("请输入编辑的答案内容","提示",{confirmButtonText:"确定",cancelButtonText:"取消",inputPlaceholder:this.xtableData[e].des}).then(function(t){var s=t.value;console.log(s),null==s?a.$message.error("输入点东西再改啊大哥"):(a.url="/testftcg/config/editConfigAssessment?token="+localStorage.token+"&id="+a.aid+"&answerDes="+s+"&answerIndex="+a.xtableData[e].index,a.$axios.get(a.url).then(function(e){console.log(e),(e.data.code=1)?a.$message.success("数据修改成功"):a.$message.error(e.data.msg),a.getData(),setTimeout(function(){a.xtableData=a.tableData[a.index].answerJson},300)}))}).catch(function(){})},handleSelectionChange:function(e){this.multipleSelection=e},handleDelete:function(e,t){this.$message.error("本数据不能删除，请谨慎操作，如需操作，请联系运维管理")},xhandleDelete:function(e,t){var a=this;this.idx=e,this.xdelVisible=!0,this.$confirm("此操作将删除本条问题的答案, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){a.url="/testftcg/config/delAssessmentQuestion?token="+localStorage.token+"&id="+a.aid+"&index="+a.xtableData[e].index,a.$axios.get(a.url).then(function(e){console.log(e),(e.data.code=200)?a.$message.success("已成功删除"):a.$message.error(e.data.msg),a.getData(),setTimeout(function(){a.xtableData=a.tableData[a.index].answerJson},300)})}).catch(function(){})}}},o={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"table"},[a("div",{directives:[{name:"show",rawName:"v-show",value:e.showtable,expression:"showtable"}],staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-lx-cascades"}),e._v(" 小区考核数据")])],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:!e.showtable,expression:"!showtable"}],staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-lx-cascades"}),e._v(" 小区考核数据--问题答案数据")])],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:e.showtable,expression:"showtable"}],staticClass:"container"},[a("div",{staticClass:"handle-box"},[a("el-button",{staticClass:"add",attrs:{type:"primary",icon:"search"},on:{click:e.add}},[e._v("新增考核数据")])],1),e._v(" "),a("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:e.tableData,"span-method":e.objectSpanMethod,border:""},on:{"selection-change":e.handleSelectionChange}},[a("el-table-column",{attrs:{prop:"id",label:"id",width:"50"}}),e._v(" "),a("el-table-column",{attrs:{prop:"oneLevelName",label:"一级指标",width:"115"}}),e._v(" "),a("el-table-column",{attrs:{prop:"shortName",label:"二级指标",width:"115"}}),e._v(" "),a("el-table-column",{attrs:{prop:"fraction",label:"分值",width:"50"}}),e._v(" "),a("el-table-column",{attrs:{prop:"assessmentType",label:"问题类型",width:"80"}}),e._v(" "),a("el-table-column",{attrs:{prop:"info",label:"具体要求",type:"textarea",width:"380"}}),e._v(" "),a("el-table-column",{attrs:{prop:"req",label:"排序",width:"50"}}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"245",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{type:"text",icon:"el-icon-edit"},on:{click:function(a){e.handleEdit(t.$index,t.row)}}},[e._v("编辑")]),e._v(" "),a("el-button",{staticClass:"red",attrs:{type:"text",icon:"el-icon-delete"},on:{click:function(a){e.handleDelete(t.$index,t.row)}}},[e._v("删除")]),e._v(" "),a("el-button",{staticClass:"blue",attrs:{type:"text",icon:"el-icon-info"},on:{click:function(a){e.handlecheck(t.$index,t.row)}}},[e._v("问题答案设置")])]}}])})],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:!e.showtable,expression:"!showtable"}],staticClass:"container"},[a("div",{staticClass:"handle-box"},[a("el-button",{attrs:{type:"primary",icon:"search"},on:{click:e.back}},[e._v("返回")]),e._v(" "),a("el-button",{staticClass:"add",attrs:{type:"primary",icon:"search"},on:{click:e.xadd}},[e._v("新增答案")])],1),e._v(" "),a("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:e.xtableData,border:""},on:{"selection-change":e.handleSelectionChange}},[a("el-table-column",{attrs:{type:"selection",width:"55",align:"center"}}),e._v(" "),a("el-table-column",{attrs:{prop:"index",label:"id",width:"100"}}),e._v(" "),a("el-table-column",{attrs:{prop:"des",label:"问题内容",width:"320"}}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"260",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{type:"text",icon:"el-icon-edit"},on:{click:function(a){e.xhandleEdit(t.$index,t.row)}}},[e._v("编辑")]),e._v(" "),a("el-button",{staticClass:"red",attrs:{type:"text",icon:"el-icon-delete"},on:{click:function(a){e.xhandleDelete(t.$index,t.row)}}},[e._v("删除")])]}}])})],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"编辑考核问题",visible:e.editVisible,width:"20%"},on:{"update:visible":function(t){e.editVisible=t}}},[a("el-form",{ref:"form",attrs:{model:e.form,"label-width":"50%"}},[a("el-form-item",{attrs:{label:"一级指标"}},[a("el-button",{on:{click:e.editVisible1}},[e._v("编辑")])],1),e._v(" "),a("el-form-item",{attrs:{label:"二级指标"}},[a("el-button",{on:{click:e.editVisible2}},[e._v("编辑")])],1),e._v(" "),a("el-form-item",{attrs:{label:"分值"}},[a("el-button",{on:{click:e.editVisible3}},[e._v("编辑")])],1),e._v(" "),a("el-form-item",{attrs:{label:"描述"}},[a("el-button",{on:{click:e.editVisible4}},[e._v("编辑")])],1),e._v(" "),a("el-form-item",{attrs:{label:"排序"}},[a("el-button",{on:{click:e.editVisible5}},[e._v("编辑")])],1)],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"新增考核问题",visible:e.addVisible,width:"30%"},on:{"update:visible":function(t){e.addVisible=t}}},[a("el-form",{ref:"form",attrs:{model:e.form,"label-width":"70px"}},[a("el-form-item",{attrs:{label:"一级指标"}},[a("el-input",{attrs:{placeholder:"输入一级指标"},model:{value:e.form.oneLevelName,callback:function(t){e.$set(e.form,"oneLevelName",t)},expression:"form.oneLevelName"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"简称"}},[a("el-input",{attrs:{placeholder:"输入简称"},model:{value:e.form.shortName,callback:function(t){e.$set(e.form,"shortName",t)},expression:"form.shortName"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"描述"}},[a("el-input",{attrs:{placeholder:"输入描述"},model:{value:e.form.info,callback:function(t){e.$set(e.form,"info",t)},expression:"form.info"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"分数"}},[a("el-input",{attrs:{placeholder:"输入分数"},model:{value:e.form.fraction,callback:function(t){e.$set(e.form,"fraction",t)},expression:"form.fraction"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"排序值"}},[a("el-input",{attrs:{placeholder:"输入排序值"},model:{value:e.form.req,callback:function(t){e.$set(e.form,"req",t)},expression:"form.req"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"问题类型"}},[a("el-select",{attrs:{placeholder:"请选择问题类型"},model:{value:e.form.assessmentType,callback:function(t){e.$set(e.form,"assessmentType",t)},expression:"form.assessmentType"}},[a("el-option",{key:"0",attrs:{label:"减分项",value:"0"}}),e._v(" "),a("el-option",{key:"1",attrs:{label:"加分项",value:"1"}})],1)],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.addVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.addtable}},[e._v("确 定")])],1)],1)],1)},staticRenderFns:[]};var i=a("VU/8")(s,o,!1,function(e){a("m0py")},"data-v-b20618be",null);t.default=i.exports},m0py:function(e,t){}});