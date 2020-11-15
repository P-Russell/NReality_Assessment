<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-12 text-center py-3">
        <h3 class="text-muted">{{ $route.params.feed }}'s Current Feed</h3>
      </div>
      <Alert v-if="error" type="danger">{{ error }}</Alert>
      <FeedList
        v-else-if="entries !== '__LOADING__' && entries.length"
        :entries="entries"
        class="col col-12 col-lg-8"
      />
      <Spinner v-else-if="entries === '__LOADING__'" :size="3" class="mt-4" />
      <Alert
        v-else-if="entries !== '__LOADING__' && entries.length === 0"
        type="info"
        >No entries for {{ $route.params.feed }} found</Alert
      >
    </div>
  </div>
</template>

<script>
import FeedList from '~/components/feed_list'
import Spinner from '~/components/spinner'
import Alert from '~/components/alert'

export default {
  name: 'ReadCurrent',
  layout: 'results',
  components: { FeedList, Spinner, Alert },
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
        readLater: false,
      })
    } catch (e) {
      this.error = 'User Not Found'
    }
  },
}
</script>
