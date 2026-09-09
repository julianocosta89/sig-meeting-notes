SIG: Ruby SIG
Date: 2026-09-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matthew Wear (Dash0)** 00:48 Hey, how's it going?
**Xuan Cao** 00:53 Hi.
**Matthew Wear (Dash0)** 00:57 Thank you.
Kayla's saying on Slack that she's sick today.
She probably won't be here.
We can wait a few minutes, see if anybody else shows up. If not, we can just chat through whatever we have to talk about.
**Xuan Cao** 01:13 Okay.
**Matthew Wear (Dash0)** 02:57 I'm guessing it's… it's just us. There is… an agenda put up by James. I'm not sure if we have enough enough opinions to answer everything, so we can look at that. Can also just look briefly at the spec SIG.
I think the… The biggest thing is the span event API deprecation plan, so that's something that we'll have to deal with one way or another, but I think the idea is that we use the… logging SDK to, to admit them, so… Yeah, I know if Cao was around, she was gonna go over, kind of, the roadmap to stability for these things.
But… So that's one thing on my mind, just for being able to make this switch over officially.
Boom.
But…
**Xuan Cao** 04:06 This… this, switching from span event to the log, that will require a lot of changes, right? Like, also, I have to… like, depends, does the SDK… Need to depend on the log has decay in the future.
**Matthew Wear (Dash0)** 04:27 I don't know. I think, ultimately, let's see… Yeah, yeah, I think that is the case, because, like, span events, like, if they were just things that we were making in instrumentation, then I think we could get away with maybe some other strategy, but since this is, like, a user-facing API, then it really needs to be… Boom.
And I think it really needs to be part of the, Part of, kind of, the stable tracing, or at least needs to be available in the same way.
Or… I guess technically not, it's just, like, if… Ultimately, yeah, you will have to delete all the lines that record a span event and replace them with some equivalent, you know, logger line.
So… Oh, yeah, are using that, you know, extensively, then they will have to depend on the log's SDK some way. Either they will have to, like, depend on the unstable one to make the transition.
Or a stable one. For instrumentation, I think I have some ideas of how we can work around this. I was gonna look into that a little bit more this week.
Kind of for both metrics, and… And logs for instrumentation.
Okay.
**Xuan Cao** 06:12 Jessica?
**Matthew Wear (Dash0)** 06:15 Yeah, hopefully I'll have more to say about that next week.
But I think that was, like, kind of the biggest issue in Spec SIG that… Relates to us.
Alright.
maintaining the OTLP prototypes. Are we okay to switch to the new code generation style C diff in action?
Is he saying that the… Generated code is a… different style.
**Xuan Cao** 07:23 Hmm.
**Matthew Wear (Dash0)** 07:29 Hello, Josef.
**Josef Šimánek** 07:32 Hello, hello, everyone.
**Matthew Wear (Dash0)** 07:36 We're missing Kayla today, she's sick, so we're just kind of going through… I think James has some questions, and I'm… I'm not sure we have all the answers, but we're at least looking at them on the… On the agenda.
**Josef Šimánek** 07:49 Yeah, no worries, I will smoothly blend in.
**Xuan Cao** 07:57 Do you know which PPR he has this? Like… It's, it's already merged.
**Matthew Wear (Dash0)** 08:29 Is it this?
**Xuan Cao** 08:34 Oh, I see, thanks.
**Matthew Wear (Dash0)** 09:35 We're gonna be able to digest a 77th file.
Diff, but…
**Xuan Cao** 09:44 Yeah, at this point, I pushed that, AI and so, review it.
**Matthew Wear (Dash0)** 09:50 Yeah, yeah, I think we should review this, Generally, I think it's probably a good idea, and for the most part, these things that James has been suggesting do work out, but I think we should just… take a look at this with AI, and And try to move this forward, because I guess it has been open for… for a while now.
So, I don't know. Am I promising too much if… if I say that you and I will look at this this week, or…
**Xuan Cao** 10:36 Oh, I can spend some time to look at the CI, particularly, that How it generated those, product, the portal.
But I probably won't take a look at other, like, Arts.
**Matthew Wear (Dash0)** 10:53 Hmm.
Can I say this?
Am I over-promising?
**Xuan Cao** 11:18 Not to me. Good.
**Matthew Wear (Dash0)** 11:21 I said try, so… So, failure is an option, and yeah, I'll… I'll definitely try to look at it.
Right.
He has a question about… which Ruby version, Release toys that you'd be using.
Do you know much about toys, and which version we should be using?
**Xuan Cao** 13:03 No.
Actually, you know, for the, OpenTelemetry, like, Ruby implementation, the one, the repo we created, we… Would you say not to use the toys? Because, I don't, I don't know… How the toys work internally, So… Because it was… has… yeah, has a lot of, release issues, and we decided, you know, to not use interiors at all, but… So… Yeah, but to some of it, I don't know much about the toys. Is there any, like, minimum… Would be a version requirement for toys.
**Josef Šimánek** 13:57 I'm not a toys expert as well.
But from my understanding, the toys in… the toys is separate, even if it's like a Ruby tool, it's not running the codebase itself, it's just managing the projects.
So there's no need to couple with the… project Ruby Runtime versions?
So that can be independent, causing no harm.
So then the question is indeed… what is the latest supported, right? And I think… There's no constraint from the… Right side, on a versioning… on those itself.
**Matthew Wear (Dash0)** 14:41 It just looks like he's trying to consolidate some of his YAML and some of the Ruby versions, kind of like… Some are 406, some are 3… That he has this…
**Josef Šimánek** 14:57 Yes, the inside, Ruby.
From my understanding, the install Ruby, gitHub action… it defaults… there are some specifications how it defaults. It's using the Ruby version, file, indeed.
If there's, I think, nothing set, you just do the latest one.
And the latest one is Paradore Action itself.
So, to upgrade to newer Ruby, you need to move the action version, and the action version has already been paid by Renovate, I think, so that will be the way how to… Remove one versioning… And rely on the other, with optional… Hard coding version, but not in a… YAML files, but in the directories itself, using the .ruby file.
Makes sense to me, that's… I think, so… Speaking now about this, I think the whole effort is to remove the hard-coded versions from the YAML files… from the GitHub files.
**Matthew Wear (Dash0)** 15:57 Yeah, it looks like he's removing these hard-coded versions, and then he has…
**Josef Šimánek** 16:02 Yeah, indeed.
**Matthew Wear (Dash0)** 16:03 Referencing the toys working directory, which has a Ruby version in it.
**Josef Šimánek** 16:07 Hmm.
**Matthew Wear (Dash0)** 16:08 Nobody has… looks fine to me.
**Josef Šimánek** 16:12 Yeah, because it's… I think it's a good pattern to not… to not let GitHub files decide on version, but keep it project-related.
And the GitHub Actions can just follow what's in the project setup.
So now there's one place we can control it from.
Which to me makes total sense.
**Matthew Wear (Dash0)** 16:30 Yeah, I think TLDR, I think what he's doing here looks good to me, and as long as it works, Then it should be fine.
**Josef Šimánek** 16:40 And it's something I see really often, like, even tiny change.
can exceed into massive diff, because a lot of those are packages, right? So… This can be one of those, and…
**Matthew Wear (Dash0)** 16:55 Alright, let's… let's look at this next one.
Because I'm glad, yeah, So he's asking if we're ready to switch, to only emitting stable from HTTP, And… I'm seeing a bunch emerge by all these.
I think this makes sense to me. If we've given 12 months, I don't know if you… maybe we want to, just consult Kayla before we give that go.
Complete thumbs up to it.
**Xuan Cao** 18:04 As long as it doesn't introduce some breaking changes, like, I think it should be good.
**Matthew Wear (Dash0)** 18:17 Yeah, I think it should be fine. I think we should confirm next week when more people are here, though.
So that… Mainly is the agenda.
I'll just make a note here.
Oh.
I feel like… I feel like I want to say latest, if it works.
**Josef Šimánek** 19:29 would be the best. I think the best would be if they're… But I'm not sure how much… That's actually related to OpenTelemetry at all.
if the toys would provide custom GitHub action, which decides actually what's the best version for toys itself, right? So he doesn't need to decide this on the project side, because the project has no idea what's the best version for those to work.
**Matthew Wear (Dash0)** 19:55 Say, if we have questions… You should…
**Josef Šimánek** 20:04 I can open issue to toys, if there would be interest into maintaining our own GitHub action, which can do the setup, right? So that will be the best. We can be just passenger of this.
**Matthew Wear (Dash0)** 20:17 So… The person who wrote that is Daniel Azuma, and he is… I think he's a maintainer on the repo. He's not a router.
**Josef Šimánek** 20:25 Yeah.
**Matthew Wear (Dash0)** 20:26 But… But he does answer us, like, if we ping him on Slack or other places,
**Josef Šimánek** 20:34 Okay, I can try open maybe on a select thread, maybe we can, reach him there.
**Matthew Wear (Dash0)** 20:39 And, yeah, I… I think he used to work at Google, and they had a lot of things they were releasing into the Ruby ecosystem, so I think he created toys for that.
And then, early on in OTEL, he was the one that kind of set up our release process, so he kind of ported that over. It's kind of… The why, the why we're using toys for everything.
But… But yeah, I think he understands that he's the one who understands this better than anybody else, so he usually tries to help us when we have questions.
So… I think that's what… I don't know, anything else we should chat about while we're here, or, If there's nothing else, then, yeah, maybe we'll just see everyone next week, and be a little more organized.
**Josef Šimánek** 21:51 All good from my side.
**Matthew Wear (Dash0)** 21:53 Cool, alright, yeah, have a good week, and I'll see you all next week. Reach out on Slack if anything comes up in the meantime.
**Josef Šimánek** 22:01 Thanks for working. Thank you, guys. Bye-bye.
