<template>
  <div class="col col-12 col-lg-8">
    <Alert v-if="error" class="col col-12" type="danger">{{ error }}</Alert>
    <FeedList
      v-else-if="entries !== '__LOADING__' && entries.length"
      :entries="entries"
    />
    <div
      v-else-if="entries === '__LOADING__'"
      class="row justify-content-center"
    >
      <Spinner :size="3" class="mt-4" />
    </div>
    <Alert
      v-else-if="entries !== '__LOADING__' && entries.length === 0"
      type="info"
      class="col col-12"
      >No entries for {{ $route.params.feed }} found</Alert
    >
  </div>
</template>

<script>
import FeedList from './feed_list'
import Spinner from './spinner'
import Alert from './alert'
export default {
  name: 'Feed',
  components: { FeedList, Spinner, Alert },
  props: {
    readLater: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      error: null,
    }
  },
  computed: {
    entries() {
      return this.$store.getters.entries
    },
  },
  async mounted() {
    try {
      await this.$store.dispatch('fetchEntries', {
        handle: this.$route.params.feed,
        readLater: this.readLater,
      })
    } catch (e) {
      this.error = 'User Not Found'
    }
  },
}
</script>

<style></style>
