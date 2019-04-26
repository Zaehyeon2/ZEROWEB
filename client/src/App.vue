<template>
  <div id="app">
    <div class="bar">
        <div class="logo">
            <a href="#">
                <img class="tlogo" src="./assets/textlogo.png">
            </a>
        </div>
    </div>

    <img class="ilogo" src="./assets/logo.png" width=300px>
    <div class="ZO">
      <div class="ZOinfo">
          Hanyang Univ. ERICA<br>Division of Computer Science<br>
      </div>
      <div class="ZOname">
          0&1<br>
      </div>
      <div class="ZOinfo">
          Algorithm Programming Academy
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.bar {
    text-align: center;
    height: 80px;
    vertical-align: middle;
    position: fixed;
    left: 0;
    top: 0;
    right: 0;
    background-color: rgba(255, 255, 255, 0.9);
    z-index: 1050;
    text-decoration: none;
}

.bar img {
    height: 20px;
    padding-left: 40px;
}

.logo {
    width: 260px;
    display: inline-block;
}
.bar a,
.bar a:hover {
    margin-top: 20px;
    display: inline-block;
    text-decoration: none;
    font-size: 28px;
    margin-right: 50px;
    color: rgb(78, 72, 72);
    vertical-align: middle;
}

.ilogo{
  margin-top:50px;
}

.ZO {
    margin-top: 50px;
    text-align: center;
    /* display: inline-block; */
}

.ZOinfo {
    font-size: 30px;
    margin-bottom: 20px;
}

.ZOname {
    font-size: 40px;
}
</style>
