<template>
  <!-- 街道 -->
  <div class="table">
    <div class="crumbs"
         v-show="showtable">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item><i class="el-icon-lx-cascades"></i> 街道基础数据</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 小区 -->
    <div class="crumbs"
         v-show="!showtable">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item><i class="el-icon-lx-cascades"></i> 街道基础数据--小区基础数据</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 街道表格 -->
    <div class="container"
         v-show="showtable">
      <div class="handle-box">

        <el-button type="primary"
                   class="add"
                   icon="search"
                   @click="add">新增街道</el-button>
      </div>
      <el-table :data="tableData"
                border
                class="table"
                ref="multipleTable"
                @selection-change="handleSelectionChange">
        <el-table-column type="selection"
                         width="55"
                         align="center"></el-table-column>

        <el-table-column prop="id"
                         label="id"
                         width="150">
        </el-table-column>
        <el-table-column prop="name"
                         label="街道名"
                         width="150">
        </el-table-column>
        <el-table-column label="操作"
                         width="260"
                         align="center">
          <template slot-scope="scope">
            <el-button type="text"
                       icon="el-icon-edit"
                       @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button type="text"
                       icon="el-icon-delete"
                       class="red"
                       @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            <el-button type="text"
                       icon="el-icon-info"
                       class="blue"
                       @click="handlecheck(scope.$index, scope.row)">查看街道内小区</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination">

      </div>
    </div>
    <!-- 小区表格 -->
    <div class="container"
         v-show="!showtable">
      <div class="handle-box">
        <el-button type="primary"
                   icon="search"
                   @click="back">返回</el-button>
        <el-button type="primary"
                   class="add"
                   icon="search"
                   @click="xadd">新增小区</el-button>
      </div>
      <el-table :data="xtableData"
                border
                class="table"
                ref="multipleTable"
                @selection-change="handleSelectionChange">
        <el-table-column type="selection"
                         width="55"
                         align="center"></el-table-column>

        <el-table-column prop="id"
                         label="id"
                         width="150">
        </el-table-column>
        <el-table-column prop="type"
                         label="类型"
                         width="150">
        </el-table-column>
        <el-table-column prop="name"
                         label="小区名"
                         width="150">
        </el-table-column>
        <el-table-column label="操作"
                         width="260"
                         align="center">
          <template slot-scope="scope">
            <el-button type="text"
                       icon="el-icon-edit"
                       @click="xhandleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button type="text"
                       icon="el-icon-delete"
                       class="red"
                       @click="xhandleDelete(scope.$index, scope.row)">删除</el-button>
            <el-button type="text"
                       icon="el-icon-info"
                       class="blue"
                       @click="xhandlecheck(scope.$index, scope.row)">查看小区内住户</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination">

      </div>
    </div>

    <!-- 新增街道弹出框 -->
    <el-dialog title="新增街道"
               :visible.sync="addVisible"
               width="30%">
      <el-form ref="form"
               :model="form"
               label-width="70px">
        <el-form-item label="名称">
          <el-input v-model="form.addname"
                    placeholder="输入街道名"></el-input>
        </el-form-item>

      </el-form>
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addtable">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 新增小区弹出框 -->
    <el-dialog title="新增小区"
               :visible.sync="xaddVisible"
               width="30%">
      <el-form ref="form"
               :model="form"
               label-width="70px">
        <el-form-item label="名称">
          <el-input v-model="form.xaddname"
                    placeholder="输入小区名"></el-input>
        </el-form-item>
        <el-form-item label="小区类型">
          <!-- <el-input v-model="form.xaddtype"
                    placeholder="0是普通小区，1是学校，2是政府机关"></el-input> -->
          <el-select v-model="form.xaddtype"
                     placeholder="请选择用户">
            <el-option key="0"
                       label="普通小区"
                       value="0"></el-option>
            <el-option key="1"
                       label="学校"
                       value="1"></el-option>
            <el-option key="2"
                       label="政府机关"
                       value="2"></el-option>
          </el-select>
        </el-form-item>

      </el-form>
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="xaddVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="xaddtable">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 删除街道提示框 -->
    <el-dialog title="删除街道提示"
               :visible.sync="delVisible"
               width="300px"
               center>
      <div class="del-dialog-cnt">删除不可恢复，是否确定删除？</div>
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="delVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="deleteRow">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 删除小区提示框 -->
    <el-dialog title="删除小区提示"
               :visible.sync="xdelVisible"
               width="300px"
               center>
      <div class="del-dialog-cnt">删除不可恢复，是否确定删除？</div>
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="xdelVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="xdeleteRow">确 定</el-button>
      </span>
    </el-dialog>
  </div>

</template>

<script>
export default {
  name: 'futiantable',
  data () {
    return {
      tableData: [],
      xtableData: [],
      cur_page: 1,
      multipleSelection: [],
      select_cate: '',
      select_word: '',
      del_list: [],
      is_search: false,
      addVisible: false,
      delVisible: false,
      xaddVisible: false,
      xdelVisible: false,
      showtable: true,
      form: {
        name: '',
        date: '',
        phone: ''
      },
      idx: -1
    }
  },
  created () {
    this.getData();
  },
  computed: {
    // newdata () {

    // }
  },
  methods: {
    // 分页导航
    // handleCurrentChange (val) {
    //   this.cur_page = val;
    //   this.getData();
    // },
    // 获取街道数据
    getData () {
      this.url = '/chenjie/testftcg/config/getStreets?token=' + localStorage.token;
      this.$axios.get(this.url, ).then((res) => {
        console.log(res)
        if (res.data.code != 1) {
          this.$message.error(res.data.msg);
        } else if (res.data.code = 1) {
          this.tableData = res.data.data
          console.log(this.tableData)
        } else {
          console.log("不知出啥问题了")
        }
      })
    },
    // 获取小区数据
    xgetData (res) {
      console.log('接受的id是' + res)
      this.url = '/chenjie/testftcg/config/getVillages?token=' + localStorage.token + '&streetId=' + res;
      this.$axios.get(this.url, ).then((res) => {
        console.log(res)
        if (res.data.code != 1) {
          this.$message.error(res.data.msg);
        } else if (res.data.code = 1) {
          this.xtableData = res.data.data
          console.log(this.xtableData)
          var newtable = this.xtableData
          this.xtableData.some((item) => { // item为数组中的元素，index为下标，arr为目标数组
            var toStr = {
              0: '普通小区',
              1: '学校',
              2: '政府机关'
            };
            this.xtableData.map(function (value) {
              var type = value.type;
              value.type = toStr[type] ? toStr[type] : type;
              return value;
            });
          })
        } else {
          console.log("不知出啥问题了")
        }
      })
    },
    //查看街道内小区
    handlecheck (index, row) {
      this.showtable = !this.showtable
      this.xgetData(row.id)
      localStorage.setItem('xid', row.id);
    },
    //查看小区内用户
    xhandlecheck (index, row) {
      console.log(row.id)
    },
    back () {
      this.showtable = !this.showtable
    },
    //点新增街道
    add () {
      this.addVisible = true;
    },
    //点新增街道后保存
    addtable () {
      if (this.form.addname == null || this.form.addtype == null) {
        this.$message.error('请输入数据后再提交');
        return
      } else {
        this.url = '/chenjie/testftcg/config/baseConfigStreet?token=' + localStorage.token + '&name=' + this.form.addname;
        this.$axios.get(this.url, ).then((res) => {
          console.log(res)
          if (res.status = 200) {
            this.addVisible = false;
            this.$message.success('插入数据成功')
            this.form.addname = ''
            this.getData();
          } else {
            console.log("不知出啥问题了")
          }
        })
      }
    },
    //点新增小区
    xadd (index, row) {
      this.xaddVisible = true;
    },
    //点新增小区后保存
    xaddtable () {
      if (this.form.xaddname == null || this.form.xaddtype == null) {
        this.$message.error('请输入数据后再提交');
        return
      } else {
        this.url = '/chenjie/testftcg/config/baseConfigVillage?token=' + localStorage.token + '&streetId=' + localStorage.xid + '&name=' + this.form.xaddname + '&type=' + this.form.xaddtype;
        this.$axios.get(this.url, ).then((res) => {
          console.log(res)
          if (res.status = 200) {
            this.xaddVisible = false;
            this.$message.success('插入数据成功')
            this.form.xaddname = '';
            this.form.xaddtype = '';
            this.xgetData(localStorage.xid);
          } else {
            console.log("不知出啥问题了")
          }
        })
      }
    },
    filterTag (value, row) {
      return row.tag === value;
    },
    // 点编辑
    handleEdit (index, row) {
      this.$message.error('创建后暂不支持修改街道信息，如需操作，请联系运维管理');
    },
    xhandleEdit (index, row) {
      this.$message.error('创建后暂不支持修改小区信息，如需操作，请联系运维管理');
    },


    handleSelectionChange (val) {
      this.multipleSelection = val;
    },
    //删除街道
    handleDelete (index, row) {
      this.idx = index;
      this.delVisible = true;
    },
    // 确定删除街道
    deleteRow () {
      this.url = '/chenjie/testftcg/config/deleteStreet?token=' + localStorage.token + '&streetId=' + this.tableData[this.idx].id;
      this.$axios.get(this.url, ).then((res) => {
        console.log(res)
        if (res.status = 200) {
          this.tableData.splice(this.idx, 1);
          this.$message.success('删除成功');
          this.delVisible = false;
        } else {
          console.log("不知出啥问题了")
        }
      })
    },
    //删除小区
    xhandleDelete (index, row) {
      this.idx = index;
      this.xdelVisible = true;
    },
    // 确定删除小区
    xdeleteRow () {
      this.url = '/chenjie/testftcg/config/deleteVillage?token=' + localStorage.token + '&villageId=' + this.xtableData[this.idx].id;
      this.$axios.get(this.url, ).then((res) => {
        console.log(res)
        if (res.status = 200) {
          this.xtableData.splice(this.idx, 1);
          this.$message.success('删除成功');
          this.xdelVisible = false;
        } else {
          console.log("不知出啥问题了")
        }
      })
    },
  }
}

</script>

<style scoped>
.handle-box {
  margin-bottom: 20px;
  text-align: right;
}

.handle-select {
  width: 120px;
}

.handle-input {
  width: 300px;
  display: inline-block;
}
.del-dialog-cnt {
  font-size: 16px;
  text-align: center;
}
.table {
  width: 100%;
  font-size: 14px;
}
.red {
  color: #ff0000;
}
.add {
  margin-right: 30%;
}
</style>
