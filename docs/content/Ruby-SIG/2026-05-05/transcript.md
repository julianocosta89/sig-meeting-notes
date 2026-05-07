SIG: Ruby SIG
Date: 2026-05-05
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:50 Hello.
It's 2 after, let's see… Arielle… can't make it, Rob might join late.
So I think it's fine for us to go ahead and get started.
I will share my screen.
Okay, here… It's a link to the notes, in case anyone wants to add anything to the agenda.
I… had something come up at home today, so I wasn't able to attend the Specsig.
It does seem like context-scoped attributes are continuing to be discussed, and, that's a spec I haven't reviewed yet, but I think would be… Helpful for us to understand.
Looks like GenAI conventions have a new home that is separate from the rest of the semantic conventions.
What else do we have on here?
Stable by default, conversation continues.
And… Let's see, just some recommendations for review… JSON object encoding for… Non-OTLP… Interesting.
Okay, so some… some things going on in spec land.
I think for us.
Getting a handle on the context, scoped, attributes, specification, and, stable date by default.
Those are the two things that I'll… Plan to look into after this meeting.
Is there anything else related to the specifications?
SIG that people want to talk about before we continue?
**Hannah Ramadan** 04:02 No, not for me.
**Kayla Reopelle** 04:06 Sounds good. Okay. We don't have anything on the agenda right now. Before I start diving into the links, is there anything that the people here want to call out?
That we should take a look at, or talk about?
**Hannah Ramadan** 04:26 I have, one thing. So, in our last meeting, we discussed a series of opened PRs from contributors, people who were fixing, some of those HTTP library test coverage.
We added a PR that basically fixed everything, so I'm going to go through and look at all of those PRs and probably end up Unfortunately, closing a good few of them, since these aren't… issues any longer. So to make that known, that that's something, I plan to go do, and I'll definitely, like, you know, apologize to the contributors and thank them for their time, working on that issue.
So… so, like, I think there's maybe 5 or 6 of them that… that we'll go ahead and we'll close out. I think, James made a comment about wanting to see if any of those… PRs added tests that could improve coverage, even though I think most of them are at, at least 94%. So I can… I can go look at those and see if there's anything worth, like, adding from those PRs, but that would, you know, ask the contributor to, like, do more work and change.
their PR, yeah, I think that's probably the best way to… manage… But if anyone has any other thoughts on that, I do feel kind of bad about, asking contributors to, like, redo a lot of their PIs, for… a small percentage bump, but I'm not sure if that is, like, respecting the contributors.
efforts, and am I asking them to do a little bit more so that we can include something from them, or just closing them because they're all well above, are, are… Test percentage, passing rates.
**Kayla Reopelle** 06:29 Yes, yeah, if you… if you were in their shoes, what do you… how would you think, you'd want to handle it? Would you rather have an opportunity to improve your PR so that it could be included? Or, I guess just, like, acknowledge that it wouldn't work out, so then that way you could maybe focus on something else.
**Hannah Ramadan** 06:50 Yeah, that's a really good question. I guess it depends on… My… my goals of… of… I just… yeah.
I… I don't really know. I do feel like it's asking folks to do something that maybe isn't necessary, although it does improve cover… it could improve coverage by a small percentage.
Yeah, I mean… Yeah, I'm not too sure.
If anyone has opinions on that, would love to hear it. If not, I'll probably just kind of go with what James suggested, which is seeing if any of those tests can bump up coverage.
**Kayla Reopelle** 07:45 Yeah, I think if you see any of the tests.
That are helpful, and that we'd want to preserve, and it would be more of, like, a matter of just them removing other tests or content from the PR that… That isn't, you know, as beneficial anymore.
I think that makes sense, but otherwise, just communicating clearly what happened and apologizing is probably what I would do.
**Hannah Ramadan** 08:13 Okay.
Awesome, thank you. I'll go ahead and do that later.
**Kayla Reopelle** 08:18 Okay, thanks, Hannah.
Alright, anyone else before we continue?
**Xuan Cao** 08:32 Hello?
I have a couple of peers, and then, MEB merge, they're not really, related to any production. Well, it's just a test, the benchmark.
**Kayla Reopelle** 08:48 Okay. Are those in the core repo?
**Xuan Cao** 08:52 Can you say hello?
**Kayla Reopelle** 08:55 In this… in this one?
**Xuan Cao** 08:57 Yeah, in the court, yeah.
**Kayla Reopelle** 08:59 Okay, oh, these benchmarks here?
**Xuan Cao** 09:02 Yeah, yeah, they're not, really related to the… any production code, just.
**Kayla Reopelle** 09:09 Okay, yeah, I, I haven't taken a look at them, but I will…
**Xuan Cao** 09:13 Oh, there's one related to bench, related to production code, related to production code, which is, the matrix SDK that… there's, one issue I found during running the benchmark, which is, to fix, no op reserver.
That costs a lot of resource, so…
**Kayla Reopelle** 09:39 Okay, so hold off on this one until you can… Or I guess the benchmarks don't really change the functionality, so it's okay to merge this, and then you'll address that separately.
**Xuan Cao** 09:50 Yeah, I already just… I already have PR for that.
**Kayla Reopelle** 09:53 Oh, cool.
**Xuan Cao** 09:54 Stories, sink is… Yeah, return false if it, if, if it is, no, no example observer.
2 by 04?
**Kayla Reopelle** 10:07 Oh, okay, right there. Got it.
**Xuan Cao** 10:09 Yeah, yeah.
**Kayla Reopelle** 10:12 Sounds good.
**Xuan Cao** 10:17 And I didn't add anything to the log, but, I mean, if you wanted to have some benchmark below, then we're also happy to do that.
**Kayla Reopelle** 10:28 Okay, yeah, I think if that's something you're interested in, that would be helpful for, just making sure all our bases are covered. Do, I haven't looked at these yet. Is there, like, anything we want to do… Related to, like, running these benchmarks regularly, or… Another way to, like, bring them into our workflow to make sure we're not losing performance.
**Xuan Cao** 10:57 I don't really know, because, to be honest, whenever something is running for the CICD, I… what I care about is if it's passed or not.
So, somebody… I don't think people will look at… it's up to this arrow, they will look at, but if it's, like, pass, then… So maybe, I mean, for some users who is interested in, like, what is performance, what is overhead, if they use the SDK, I mean, they… we can put somewhere, like, README to say, You know, but the sense that, if I run in my end trip, it will be different stars, and… I'll Trip, so I can provide those, what I… what is running in my… Set up.
could be a… could be a reference, or I can run it in some, like, Ubuntu… from AWS as, like, a general… Reference guideline to say.
However, I mean, I can do it, to add a README.
**Kayla Reopelle** 12:08 For sure what it's…
**Xuan Cao** 12:09 Exactly, difference, yeah.
**Kayla Reopelle** 12:13 Nice. I think, I think that would be helpful just as, like, an initial pass, and, you know, maybe we check in on it, like, annually or something like that, to see how the numbers look.
**Xuan Cao** 12:26 Yeah, yeah, I can, I can. I'll update the PR, with those, data.
**Kayla Reopelle** 12:34 Sounds good.
Okay, nice.
Alright… As you can tell by my blue lines, there's a lot of PRs that I need to review. Arjun, I know there's a couple of PRs that you have down here. I'm sorry, I haven't taken a look at them yet.
But I will… I will try this week.
For other things, it looks like we have… Another… we have a PR from Bart. This hotel bot PR opened up automatically… There's some other cleanup things, pop over to issues… Looks like… Telemetry SDK attributes are missing… New benchmarking tool recommended.
Is there… Anything else in core that people want to look at before we move over to Contrib?
Okay.
Alright, and then in contribib… actually, I'm gonna move Hannah here.
Commit to that section.
So, looks like we have some renovate… Yeah, I guess there's… there's so many possible options. Is there anything that people want to look at specifically together?
Right, well, oh, did I… did I hear a noise?
No.
**Hannah Ramadan** 15:28 No, I was gonna remark that I don't have anything specifically. I do have one PR up for a bug fix, but I'm kind of going back and forth with Ariel on that.
**Kayla Reopelle** 15:38 Okay.
Do you want more, insight? Like, more reviews on it, or do you want to wait until you're done with Ariel before continuing?
**Hannah Ramadan** 15:47 You know, it is, reviewable now. I think we're just kind of going back and forth on… on which approach to take, so if anyone has opinions on it, I think… This is… So… so the bug that somebody reported is basically saying that a no method error gets raised? Yeah, this one. When the SDK is disabled, and that's because our instrumentation gets initialized, so we're getting, Like, a config value that… It exists, but it's… if someone calls, like, tries to get something from it, there… there's no… no method error. And… I think that… I mean… because it's a change to base, I just wanted to be, like, very careful, with what we're doing here. And if you scroll down a little bit, Arielle and I are kind of having a conversation in the GRPC.
comment, yeah, with kind of, like, what to do, and I think the initial approach would change it so that the config value is never empty. It's always populated with defaults, even if the instrumentation is never installed. And… There's a new suggestion I made a little bit ago about, keeping it so that if… we are checking for an empty config, that is still a, like, valid thing to do, because some of our instrumentations do that, so… I kind of feel like this is probably the least, downstream impact approach, so I wanted to hear what Arielle thought of it, but if anybody else has thoughts on that, this initial these initial changes that I made in this PR, would make it so that a config would never be empty, and maybe that's not the best thing to do, so… I think this… this preserves, like, initial… like, existing behavior, so we don't have to change any… any libraries or anything, so…
**Kayla Reopelle** 18:04 Okay Interesting.
Yeah, I think I'll have to read through it before I have any opinions, but, this is a good bug to catch, because I think this is relatively new for an environment variable.
Okay, well, if there isn't anything else that people want to chat about synchronously.
Maybe we call it here, and… I can just start diving into the pull requests.
Last call if there's any other discussion topics.
**Hannah Ramadan** 19:02 Yep, all good here.
**Kayla Reopelle** 19:07 Great, okay. Well, thank you everyone for coming. It's a little bit of a shorter one today. Appreciate all the work that you're doing, and I'm sorry that I haven't really been around lately, but, this week is looking clear for OTEL, so hoping to get a lot of stuff done.
**Hannah Ramadan** 19:22 Nice.
**Kayla Reopelle** 19:25 Alright, I will see you all next week, then. Take care.
**Hannah Ramadan** 19:29 Oh, thanks, everyone.
**Arjun Rajappa** 19:32 Thank you.
**Kayla Reopelle** 19:33 Thanks.
**Xuan Cao** 19:33 Bye.
**Kayla Reopelle** 19:35 Pete.
