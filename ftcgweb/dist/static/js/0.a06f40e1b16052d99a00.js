webpackJsonp([0],{"7nbJ":function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var l={name:"assessmenttable",data:function(){return{tableData:[],xtableData:[],cur_page:1,multipleSelection:[],select_cate:"",select_word:"",del_list:[],is_search:!1,addVisible:!1,delVisible:!1,xaddVisible:!1,xdelVisible:!1,showtable:!0,form:{name:"",date:"",phone:""},idx:-1}},created:function(){this.getData()},computed:{},methods:{getData:function(){var e=this;this.url="/testftcg/config/getConfigAssessment?token="+localStorage.token+"&subordinateType=0 &assessmentType=0",this.$axios.get(this.url).then(function(t){(t.status=200)?(e.tableData=t.data.data[0].levelList.levelList,e.tableData[0].name="无台账记录扣8分，台帐记录不完整扣5分，没有定期向辖区街道办事处报送数据扣3分",e.tableData[0].name1="查阅资料",e.tableData[1].name="每缺少一类容器，扣2分;未设置投放指引牌,扣4分",e.tableData[1].name1="现场查看",console.log(e.tableData)):e.$message.error(t.data.msg)})},xgetData:function(e){var t=this;console.log("接受的id是"+e),this.url="/testftcg/config/getVillages?token="+localStorage.token+"&streetId="+e,this.$axios.get(this.url).then(function(e){if(console.log(e),1!=e.data.code)t.$message.error(e.data.msg);else if(e.data.code=1){t.xtableData=e.data.data,console.log(t.xtableData);t.xtableData;t.xtableData.some(function(e){var a={0:"普通小区",1:"学校",2:"政府机关"};t.xtableData.map(function(e){var t=e.type;return e.type=a[t]?a[t]:t,e})})}else console.log("不知出啥问题了")})},handlecheck:function(){this.$message.success("开发中……")},back:function(){this.showtable=!this.showtable},add:function(){this.$message.success("开发中……")},addtable:function(){this.$message.success("开发中……")},xadd:function(e,t){this.xaddVisible=!0},xaddtable:function(){var e=this;null!=this.form.xaddname&&null!=this.form.xaddtype?(this.url="/testftcg/config/baseConfigVillage?token="+localStorage.token+"&streetId="+localStorage.xid+"&name="+this.form.xaddname+"&type="+this.form.xaddtype,this.$axios.get(this.url).then(function(t){console.log(t),(t.status=200)?(e.xaddVisible=!1,e.$message.success("插入数据成功"),e.form.xaddname="",e.form.xaddtype="",e.xgetData(localStorage.xid)):console.log("不知出啥问题了")})):this.$message.error("请输入数据后再提交")},filterTag:function(e,t){return t.tag===e},handleEdit:function(e,t){this.$message.error("创建后暂不支持修改街道信息，如需操作，请联系运维管理")},xhandleEdit:function(e,t){this.$message.error("创建后暂不支持修改小区信息，如需操作，请联系运维管理")},handleSelectionChange:function(e){this.multipleSelection=e},handleDelete:function(e,t){this.$message.success("开发中……")},deleteRow:function(){var e=this;this.url="/testftcg/config/deleteStreet?token="+localStorage.token+"&streetId="+this.tableData[this.idx].id,this.$axios.get(this.url).then(function(t){console.log(t),(t.status=200)?(e.tableData.splice(e.idx,1),e.$message.success("删除成功"),e.delVisible=!1):console.log("不知出啥问题了")})},xhandleDelete:function(e,t){this.idx=e,this.xdelVisible=!0},xdeleteRow:function(){var e=this;this.url="/testftcg/config/deleteVillage?token="+localStorage.token+"&villageId="+this.xtableData[this.idx].id,this.$axios.get(this.url).then(function(t){console.log(t),(t.status=200)?(e.xtableData.splice(e.idx,1),e.$message.success("删除成功"),e.xdelVisible=!1):console.log("不知出啥问题了")})}}},s={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"table"},[a("div",{directives:[{name:"show",rawName:"v-show",value:e.showtable,expression:"showtable"}],staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-lx-cascades"}),e._v(" 街道基础数据")])],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:!e.showtable,expression:"!showtable"}],staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-lx-cascades"}),e._v(" 街道基础数据--小区基础数据")])],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:e.showtable,expression:"showtable"}],staticClass:"container"},[a("div",{staticClass:"handle-box"},[a("el-button",{staticClass:"add",attrs:{type:"primary",icon:"search"},on:{click:e.add}},[e._v("新增考核数据")])],1),e._v(" "),a("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:e.tableData,border:""},on:{"selection-change":e.handleSelectionChange}},[a("el-table-column",{attrs:{type:"selection",width:"55",align:"center"}}),e._v(" "),a("el-table-column",{attrs:{prop:"info",label:"具体要求",width:"220"}}),e._v(" "),a("el-table-column",{attrs:{prop:"fraction",label:"分值",width:"50"}}),e._v(" "),a("el-table-column",{attrs:{prop:"name",label:"评价标准",width:"220"}}),e._v(" "),a("el-table-column",{attrs:{prop:"levelTitle",label:"所属指标",width:"100"}}),e._v(" "),a("el-table-column",{attrs:{prop:"name1",label:"评价方法",width:"80"}}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"250",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{type:"text",icon:"el-icon-edit"},on:{click:function(a){e.handleEdit(t.$index,t.row)}}},[e._v("编辑")]),e._v(" "),a("el-button",{staticClass:"red",attrs:{type:"text",icon:"el-icon-delete"},on:{click:function(a){e.handleDelete(t.$index,t.row)}}},[e._v("删除")]),e._v(" "),a("el-button",{staticClass:"blue",attrs:{type:"text",icon:"el-icon-info"},on:{click:function(a){e.handlecheck(t.$index,t.row)}}},[e._v("问题答案设置")])]}}])})],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:!e.showtable,expression:"!showtable"}],staticClass:"container"},[a("div",{staticClass:"handle-box"},[a("el-button",{attrs:{type:"primary",icon:"search"},on:{click:e.back}},[e._v("返回")]),e._v(" "),a("el-button",{staticClass:"add",attrs:{type:"primary",icon:"search"},on:{click:e.xadd}},[e._v("新增小区")])],1),e._v(" "),a("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:e.xtableData,border:""},on:{"selection-change":e.handleSelectionChange}},[a("el-table-column",{attrs:{type:"selection",width:"55",align:"center"}}),e._v(" "),a("el-table-column",{attrs:{prop:"id",label:"id",width:"150"}}),e._v(" "),a("el-table-column",{attrs:{prop:"type",label:"类型",width:"150"}}),e._v(" "),a("el-table-column",{attrs:{prop:"name",label:"小区名",width:"150"}}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"260",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{type:"text",icon:"el-icon-edit"},on:{click:function(a){e.xhandleEdit(t.$index,t.row)}}},[e._v("编辑")]),e._v(" "),a("el-button",{staticClass:"red",attrs:{type:"text",icon:"el-icon-delete"},on:{click:function(a){e.xhandleDelete(t.$index,t.row)}}},[e._v("删除")])]}}])})],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"新增街道",visible:e.addVisible,width:"30%"},on:{"update:visible":function(t){e.addVisible=t}}},[a("el-form",{ref:"form",attrs:{model:e.form,"label-width":"70px"}},[a("el-form-item",{attrs:{label:"名称"}},[a("el-input",{attrs:{placeholder:"输入街道名"},model:{value:e.form.addname,callback:function(t){e.$set(e.form,"addname",t)},expression:"form.addname"}})],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.addVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.addtable}},[e._v("确 定")])],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"新增小区",visible:e.xaddVisible,width:"30%"},on:{"update:visible":function(t){e.xaddVisible=t}}},[a("el-form",{ref:"form",attrs:{model:e.form,"label-width":"70px"}},[a("el-form-item",{attrs:{label:"名称"}},[a("el-input",{attrs:{placeholder:"输入小区名"},model:{value:e.form.xaddname,callback:function(t){e.$set(e.form,"xaddname",t)},expression:"form.xaddname"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"小区类型"}},[a("el-select",{attrs:{placeholder:"请选择用户"},model:{value:e.form.xaddtype,callback:function(t){e.$set(e.form,"xaddtype",t)},expression:"form.xaddtype"}},[a("el-option",{key:"0",attrs:{label:"普通小区",value:"0"}}),e._v(" "),a("el-option",{key:"1",attrs:{label:"学校",value:"1"}}),e._v(" "),a("el-option",{key:"2",attrs:{label:"政府机关",value:"2"}})],1)],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.xaddVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.xaddtable}},[e._v("确 定")])],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"删除街道提示",visible:e.delVisible,width:"300px",center:""},on:{"update:visible":function(t){e.delVisible=t}}},[a("div",{staticClass:"del-dialog-cnt"},[e._v("删除不可恢复，是否确定删除？")]),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.delVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.deleteRow}},[e._v("确 定")])],1)]),e._v(" "),a("el-dialog",{attrs:{title:"删除小区提示",visible:e.xdelVisible,width:"300px",center:""},on:{"update:visible":function(t){e.xdelVisible=t}}},[a("div",{staticClass:"del-dialog-cnt"},[e._v("删除不可恢复，是否确定删除？")]),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.xdelVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.xdeleteRow}},[e._v("确 定")])],1)])],1)},staticRenderFns:[]};var i=a("VU/8")(l,s,!1,function(e){a("Je7l")},"data-v-8b58b9dc",null);t.default=i.exports},Je7l:function(e,t){}});