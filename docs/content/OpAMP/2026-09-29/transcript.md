SIG: OpAMP
Date: 2026-09-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan (Splunk Inc.)** 01:16 Hello.
**Israel Blancas** 01:19 8.
**Dakota Paasman** 01:57 Thanks for reviewing those PRs, Tigran.
**Tigran Najaryan (Splunk Inc.)** 02:00 Yeah, sorry about the delay.
I was kind of… On and off, out for a while.
Yeah, I think it's fine. I merged a couple.
Here and there.
And we have the big one coming with the other station and all that stuff.
So, if you haven't seen Stanley, I, I approved the spec PR for attestation.
What I'd like to do is to, Make sure that the Go implementation is ready to go.
And then we'll measure the spec PR, and then immediately after that, we'll measure the goal PR. I don't want to… Have the spec merged.
And stay unimplemented for a long time.
So, I think we have the consensus that the API, the public API, the changes you proposed on Go implementation are fine.
We just need to take a look at the implementation details now. Once that is ready, I mean, we'll need to do a thorough review of the implementation. Once that is ready, we'll merge the spec and merge the Go implementation. But I think we're… We're pretty close.
**Stanley Liu** 03:16 Awesome. Yeah, thanks so much for the reviews, and really appreciate the help. I'll just make sure to add tests and review the implementation to make sure it's good, and I'll ping you when it's ready.
**Tigran Najaryan (Splunk Inc.)** 03:26 Yeah, there's a few merge conflicts that you'll need to resolve. Once you do that, please ping me directly, tag me on the PR so that I remember to do a detailed review, and we'll probably do a couple iterations, and we'll be ready to go.
**Stanley Liu** 03:42 Okay, great. Thanks so much for all the support.
**Tigran Najaryan (Splunk Inc.)** 03:45 Yeah, sure. Sorry about the delay. I was a bit kind of.
Away for a while, so it took a bit longer than I would want it to be.
**Stanley Liu** 03:54 Yeah, thanks, no worries.
**Tigran Najaryan (Splunk Inc.)** 04:01 Okay.
I don't see anything in the agenda. Dakota, I think you have — so I merged the OpAMP Go one, which adds the support for dial context, which is what you need to implement this further.
And I think there's others that are no longer on the OpAMP goal. They are in the collector now, the implementation.
**Dakota Paasman** 04:24 Yeah, correct. I can… I should link those PRs here if I can get them pulled up, but I do have them up right now. Once OpAMP… once a new version of OpAMP Go is released, I can update The, supervisor and… extension PRs to pull in the new version of OpAmp Go. Right now, they're just replacing two the Git ref that was latest for that Pr.
**Tigran Najaryan (Splunk Inc.)** 04:53 Okay, so then I guess let's make a release in that case, if you need it.
There's a bunch of dependency updates, let me see if I can merge as many as I can quickly, if they're ready to go, and then… We'll make a release.
Let's try to do it maybe today.
**Dakota Paasman** 05:18 Yeah, I can…
**Tigran Najaryan (Splunk Inc.)** 05:18 Anything that is an open PR that you think Needs to go into the release urgently for whatever reason, or you're just dependent on this one that is already merged.
**Dakota Paasman** 05:31 Yeah, that was the only dependency on OpAMP Co.
**Tigran Najaryan (Splunk Inc.)** 05:35 Okay.
Okay.
**Dakota Paasman** 05:42 Yeah, I just added… to the… Agenda.
**Tigran Najaryan (Splunk Inc.)** 05:47 Okay, then I guess I'll take care of the release. You guys can then work on the country pieces.
**Dakota Paasman** 05:55 For sure.
**Tigran Najaryan (Splunk Inc.)** 06:00 Okay, anything else? Anyone? Any… any topics? There's nothing in the agenda.
Okay.
Thank you all.
Fine.
**Stanley Liu** 06:28 Yes.
