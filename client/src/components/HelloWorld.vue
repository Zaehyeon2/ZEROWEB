<template>
  <div class="hello">
    <table class="table table-border">
      <thead class="thead">
        <tr>
          <th scope="col">순위</th>
          <th scope="col">이름</th>
          <th scope="col">한마디</th>
          <th scope='col'>푼 문제수</th>
          <th scope='col'>정답률</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(data, index) in msg" :key="index">
          <td>{{ data.rank }}</td>
          <td><a :href="data.url" :class="data.color">
          {{ data.name }}</a></td>
          <td>{{ data.comment }}</td>
          <td>{{ data.pro }}</td>
          <td>{{ data.per  }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: [],
    };
  },
  methods: {
    getdata() {
      const path = 'http://testzerone.iptime.org:5000/rank';
      axios.post(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getdata();
  },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
a {
  text-decoration: none;
  color: blue;
}

.table {
  margin-top: 50px;
  padding: 10px;
  display: inline-block;
  text-align: center;
  border: solid 1px;
}

.thead {
  border: solid 1px;
}

td {
  padding: 4px;
}

.violet{
  font-weight: bold;
  color: rgb(170,0,170);
}

.green{
  font-weight: bold;
  color: rgb(0,128,0);
}

.cyan{
  font-weight: bold;
  color: rgb(3, 168, 158);
}

.normal {
  font-weight: none;
  color: rgb(0,118,192);
}


</style>
