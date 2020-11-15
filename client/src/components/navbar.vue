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
              :class="{ active: this.$route.name === 'feed-current' }"
              :to="`/${this.$route.params.feed}/current`"
              >Current</NuxtLink
            >
          </li>
          <li class="nav-item">
            <NuxtLink
              class="nav-link"
              :class="{ active: this.$route.name === 'feed-read_later' }"
              :to="`/${this.$route.params.feed}/read_later`"
              >Read Later List</NuxtLink
            >
          </li>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input
              size="sm"
              class="mr-sm-2"
              placeholder="Search"
            ></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit"
              >Search</b-button
            >
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  mounted() {
    console.log(this.$route)
  },
}
</script>

<style></style>
