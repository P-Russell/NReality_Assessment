<template>
  <div>
    <b-navbar toggleable="lg" type="light" variant="light">
      <NuxtLink to="/" class="navbar-brand mr-5">GitHubber</NuxtLink>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <li class="nav-item">
            <NuxtLink
              class="nav-link"
              :class="{ active: $route.name === 'feed-current' }"
              :to="`/${$route.params.feed}/current`"
              >Current</NuxtLink
            >
          </li>
          <li class="nav-item">
            <NuxtLink
              class="nav-link"
              :class="{ active: $route.name === 'feed-read_later' }"
              :to="`/${$route.params.feed}/read_later`"
              >Read Later List</NuxtLink
            >
          </li>
          <li class="nav-item">
            <NuxtLink class="nav-link" :to="`/`">Home</NuxtLink>
          </li>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-form @submit.prevent>
            <b-form-input
              v-model="filter"
              size="sm"
              class="mr-sm-2"
              placeholder="Search Feed"
            ></b-form-input>
            <b-button
              v-if="!$store.state.applyFilter"
              size="sm"
              class="my-2 my-sm-0 search-button"
              type="submit"
              @click="applyFilter"
              >Search</b-button
            >
            <b-button
              v-else
              size="sm"
              class="my-2 my-sm-0 search-button"
              type="submit"
              @click="clearFilter"
              >Clear Search</b-button
            >
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  computed: {
    filter: {
      get() {
        return this.$store.state.filter
      },
      set(v) {
        return this.$store.commit('setFilter', v)
      },
    },
  },
  methods: {
    applyFilter() {
      if (this.filter) {
        this.$store.commit('setApplyFilter', true)
      }
    },
    clearFilter() {
      this.$store.commit('setApplyFilter', false)
      this.$store.commit('setFilter', null)
    },
  },
  watch: {
    filter() {
      if (!this.filter) {
        this.$store.commit('setApplyFilter', false)
      }
    },
  },
}
</script>

<style>
.search-button {
  width: 7rem;
}
</style>
