SIG: Ruby SIG
Date: 2025-10-07
Duration: 98 minutes
============================================================

## Zoom Recording Transcript

**Wendy Smoak** 02:07 Hello, just us?
**ericmustin** 02:08 Maybe.
They don't.
**Wendy Smoak** 02:13 I think Ariel said he couldn't come.
**ericmustin** 02:15 Yeah.
I think he's unable to attend.
**Wendy Smoak** 02:19 But it's also only one minute after, so…
It's not like people are late.
**ericmustin** 02:24 I used to work for a guy who would, at the 2-minute mark, he would leave the meeting if the person he wanted to… and it was always so, like…
I was like, like…
**Wendy Smoak** 02:33 That's the way to enforce.
**ericmustin** 02:35 Yeah.
**Wendy Smoak** 02:37 I mean, we had the rule in college, right, that if the instructor didn't show up 15 minutes, then you could leave.
**ericmustin** 02:42 Oh, yeah. Oh, yeah.
**Wendy Smoak** 02:43 I've had that.
**ericmustin** 02:44 bus. In public school, or my… the one I grew up, like, the buses… there was some, like, obscure thing where it's like, if the bus was 30 minutes late, like, you know, in my third grade mind, like, legally, you didn't have to go to school, and so… but the bus was always, like, 28 minutes late.
So anyway, I.
**Wendy Smoak** 03:05 Okay. Where's…
**ericmustin** 03:06 Of course.
I've been really adamant.
Might not be a good… Driver… Today.
**Kayla Reopelle** 03:16 Yeah, I can get the notes…
But my, my computer has been slow today, so… Hopefully this doesn't impact things.
Today, October 7th.
I had some other meetings this morning, so I was not able to go to the Spec Sig, so we'll be…
Looking at that together, here's the notes in the chat if anyone has anything they want to add to the agenda.
Okay.
So… what happened today?
Early feedback for span visibility changes.
Long-running problem, huh, okay.
**ericmustin** 04:46 It's a collector? Russ? Oh, no, it's…
**Kayla Reopelle** 04:50 It's, yeah.
I guess, yeah, SDK… Changes, potentially?
**ericmustin** 04:59 The partial choice connector. What is a connector?
**Kayla Reopelle** 05:04 Thing that… So where's pain?
**Robb Kidd (he/him)** 05:08 pipelines.
**Wendy Smoak** 05:10 Yeah, you can connect two pipelines together, like, take it out of one and stick it back in.
**ericmustin** 05:13 Oh, oh, like a pro… right, right, like a collector… Connector.
**Robb Kidd (he/him)** 05:18 It's so that, it's so that an exporter doesn't have to export to itself.
**ericmustin** 05:23 Right, right, it's…
**Robb Kidd (he/him)** 05:24 tap pipelines.
**ericmustin** 05:25 Yeah, yeah, I, I'm just slow.
**Kayla Reopelle** 05:31 Okay, this is a huge proposal.
**ericmustin** 05:34 This is the most work-slop thing I've ever seen. 5'd it.
**Kayla Reopelle** 05:42 Alright, well, that's early feedback, so something to consider there. Let's look at the next one.
Introduce any value to support complex data structures.
I thought we already had that.
But, maybe it's just a wider variety of structures?
**Wendy Smoak** 06:08 for attributes?
**Kayla Reopelle** 06:10 Yeah.
**Wendy Smoak** 06:11 It complains if it's not, like, string or number. That's all you get, and it can't be null .
**Kayla Reopelle** 06:16 Right.
**ericmustin** 06:18 Relaxing that.
**Wendy Smoak** 06:20 I guess that's relaxing. That's good.
**Kayla Reopelle** 06:25 Okay, yeah, there we go.
**ericmustin** 06:27 So, end up being worked.
**Kayla Reopelle** 06:33 Seems like it would be… Not too difficult to…
**Wendy Smoak** 06:37 Does it allow null now?
I can get rid of all my OR, OR empty string, OR empty string.
**Kayla Reopelle** 06:44 Let's see…
**Wendy Smoak** 06:45 Yep, you do not understand, none of that. Yay!
**Kayla Reopelle** 06:50 Cool.
Interesting. I wonder if, since that would be a break and change, if we'd have to implement that in, like, a 2.0 version of the…
SDK.
Alright, let's see, what's next…
Oh, Hotel Community Awards are open.
If you want to submit a nomination, you have a month.
Winners will be announced at KubeCon.
Is anyone going to KubeCon this year?
**ericmustin** 07:27 I am not.
**Kayla Reopelle** 07:29 Yeah, me neither. Oh, there's also a call for sessions… At the observa… observatory booth.
And…
Time-weighted reservoir sampling for histograms.
Interesting.
**ericmustin** 08:06 Okay.
**Kayla Reopelle** 08:11 I know you've had an exemplar PR open for ages, and, I'm sorry for not taking a look at it yet.
**ericmustin** 08:21 Me? I have not.
**Kayla Reopelle** 08:22 For Wednesday? Wendy?
Schwan has had.
**ericmustin** 08:26 Oh, you're.
**Kayla Reopelle** 08:26 It's been for a long time.
Okay, interesting. Alright, so there's some… some new stuff cooking up.
to think about.
Does anyone… okay, we have a burning question, so maybe we'll just start there instead of, going to Warren Contrib, and we'll circle back.
So.
**Wendy Smoak** 08:55 Oh, that was me.
**Kayla Reopelle** 08:56 Yes.
**Wendy Smoak** 08:56 My initials by it.
Hi!
There's… I attempted to… Merge to update this, and wow, there are a lot of conflicts.
**Kayla Reopelle** 09:08 Oh, there are. Okay.
Fascinating.
**Wendy Smoak** 09:13 Is it marked? Does it say?
Oh, it's still thinking. It's thinking, yeah, it's gonna have to think hard.
**Kayla Reopelle** 09:19 I think something is, well, if there are a ton of conflicts, I can work on fixing them.
So, you've been using Mobile without this before? You might not know what they are. Yeah, I haven't… I haven't looked at this for a few weeks.
**Wendy Smoak** 09:33 What I…
**Robb Kidd (he/him)** 09:33 They've loaded on my screen, and it looks like conflicts in instrumentation All.
**Kayla Reopelle** 09:38 Okay, yeah, that makes sense.
**Robb Kidd (he/him)** 09:40 two conflicts of instrumentation All, and one in .toys.dataReleases. So I think it's.
**Kayla Reopelle** 09:46 Okay.
**Robb Kidd (he/him)** 09:47 Yeah, that…
**Wendy Smoak** 09:48 Maybe it got better. When I just tried to merge it locally, it went… it's a long list. I backed away slowly.
**Kayla Reopelle** 09:55 Oh.
**Wendy Smoak** 09:55 Oh, it was more… it was way more than that.
**Kayla Reopelle** 09:57 Oh, yeah.
**Robb Kidd (he/him)** 09:58 Seeing the conflicts, those files ought to be resolved.
**Kayla Reopelle** 10:02 Yeah.
**Robb Kidd (he/him)** 10:03 Automatically, but…
**Wendy Smoak** 10:04 This… would be useful. I have a… I have an application that makes
deep use of the Rails Tag Blogger, you know how it… you can go more than what, like, multiple levels deep with the tags?
**Kayla Reopelle** 10:16 Yeah.
**Wendy Smoak** 10:17 There's just no way to get in there with any other…
there was a… there was a thread. Like, the only appender you can add is a stream, and these aren't… the hotel's not streams.
**Kayla Reopelle** 10:27 So it's just a mess. Okay.
**Wendy Smoak** 10:29 So I… Claude, I did not do this. Claude did this. Basically, Just looked at the diff.
And implemented it for us, like, picked out the minimum necessary to make it work for a single app.
And it worked fine, so the… the concept…
I mean, I'm sure you know this, you wrote it. It worked, or you wouldn't have opened the PR.
**Kayla Reopelle** 10:52 Yeah, I'm glad.
**Wendy Smoak** 10:53 It works! We like it!
**Kayla Reopelle** 10:55 Okay, cool. Well, maybe this is a good opportunity for us to just talk through these things to see what we can do to get it out.
So… yeah, back in August,
Got some feedback about trying to move the logger instrumentation into a separate bridge. I think we might have had this conversation before, but I don't remember us making any conclusions.
So there's a lot of…
complications if we move it out of the instrumentation directory. That doesn't necessarily mean it's the wrong choice, but this is a structure that's also used by some other languages. I guess both structures are kind of present in the hotel space.
And then, yeah, one other thing to keep in mind is that we will eventually need to add…
if we, you know, choose to do… distribute instrumentation for AI libraries, we will have to have, like, an SDK logger in instrumentation base for those, because AI events are created from OTEL logs.
So it's not just spans and metrics in that case, which I think could be a good argument to keep it in instrumentation.
We could do that next week.
**Wendy Smoak** 12:13 the… Like, working with the code, it…
feels like it is instrumenting, like it's prepending methods, it's like…
**Kayla Reopelle** 12:21 Yeah.
**Wendy Smoak** 12:21 I mean, you can call it a bridge, but it's the same instrumentation that, like, the SDK is doing to fix itself for thread use, for use in threads, so, I mean…
I don't see a strong argument to name the directory something, though, unless it's…
**Robb Kidd (he/him)** 12:37 They're at the risk of…
using the word semantics. What's the semantics of calling something an instrumentation versus a bridge?
**Wendy Smoak** 12:46 Of birds.
**Kayla Reopelle** 12:48 Yeah, I think that, there is…
something… I think bridges may be used in the logs… Api… hotel…
at one point, it was maybe called the… the Logs Bridge, but I'm not seeing…
**ericmustin** 13:13 Yeah, there was…
**Wendy Smoak** 13:14 There was a PR that I just found.
Yeah, that was… that was earlier, when I was looking for this one, that is… that says you implemented a… something about a bridge.
**Kayla Reopelle** 13:25 Yeah, yeah, I forget, maybe they've changed it now, but, like, that was kind of Otel's word for…
making their logs compatible with, like, older loggers, but it doesn't seem to be as prominent in the spec anymore.
I just implemented this the way that we basically have it implemented in New Relic.
Which we've had out for a few years, and it's been fine.
But yeah, but that just does use that kind of same instrumentation prepend ideology. I'm not really sure how else you would do it.
**Robb Kidd (he/him)** 14:03 I sense that there are… there are two sort of ways to log with OTEL. There are… use the logs API and an SDK that implements it directly to make log statements, or there's… you've got a logging library already, and you want to somehow…
make it generate hotel spots.
**Kayla Reopelle** 14:22 Yeah, exactly.
**Robb Kidd (he/him)** 14:24 And I think the means by which we do that The instrument body.
**Kayla Reopelle** 14:30 Yeah, yeah.
**Robb Kidd (he/him)** 14:31 We're putting our hooks in the login libraries, and that instrumentation happens to be a logs bridge, because it is acting as a bridge, but…
**Kayla Reopelle** 14:38 Yeah.
**Robb Kidd (he/him)** 14:38 If there's no, like, hotel-specced thing called a bridge?
It's just a verb that we're using.
to describe.
**Kayla Reopelle** 14:48 Yeah.
**Robb Kidd (he/him)** 14:50 Technically, we are instrumenting how the logging library is performing.
I could get into semantics about.
We're not instrumenting the logging library's performance. We are…
Patching it like we patch other things to instrument them, but we're patching them for the purposes of…
**Kayla Reopelle** 15:09 Yeah.
Yeah, for the purposes of popping.
So…
**ericmustin** 15:16 I'm trying to do something similar.
**Wendy Smoak** 15:18 Go ahead, Eric.
**ericmustin** 15:19 I was gonna say, like, with Anthropics… instrumentation. It's, like, not… that… different…
From what we do with logging, we're just, like.
We're not adding… we're not generating spans as a result of our instrumentation, just like… Greasing the wheels on…
getting things… I don't… I think all we do at Anthropic is, like, we're just propagating over fibers, like, we just do some funkiness, so it's, like, that's technically instrumentation, but…
We're not instrumenting shit? Sorry.
**Kayla Reopelle** 15:49 Yeah.
**ericmustin** 15:49 so…
**Robb Kidd (he/him)** 15:51 What problem is solved by moving the logger instrumentation into a bridge direction?
Is that… I don't think it makes things clearer.
**Kayla Reopelle** 16:04 Yeah.
**Robb Kidd (he/him)** 16:05 defense that it does, because I'm… I'm new here.
**ericmustin** 16:18 What do you wanna do?
**Robb Kidd (he/him)** 16:20 Right?
**Kayla Reopelle** 16:20 I think I'd rather just leave it and get the gem out, and I can pull it out of instrumentation All, so that people have to install it manually, since it's not a stable SDK.
If I just remove that, then people can start using it without needing to install it from a branch, which is the way things are set up right now. And it's been open for so long, I'm not actively maintaining it well enough to make sure the instrumentation is all always synced.
So…
**ericmustin** 16:48 works for me. I mean…
I'd rather just get bonked by someone and be told we're doing it wrong, and move forward, like in, than…
Be, you know, let's just beg for forgiveness.
**Kayla Reopelle** 17:00 Okay.
**Robb Kidd (he/him)** 17:02 Like, I could see this… that semantics is like, well, it's not instrumenting the library, it's just…
It's acting as a bridge, so it ought to be called a bridge, and we can let somebody tell us that.
**ericmustin** 17:11 Yeah.
**Robb Kidd (he/him)** 17:12 It works as named, located it where it is, and it depends on instrumentation base, so it looks an awful lot like instrumentation, so…
Let's ship it and make it better.
**Kayla Reopelle** 17:21 Sweet.
I… that… that makes my day. I love that.
**Wendy Smoak** 17:26 There was another question in there, I think, that you're gonna run into when you try to… something about, like, should it do the…
There's another comment on it. It was something about, should you put the prog name in it or not?
**Kayla Reopelle** 17:40 Oh, yeah.
Yeah, that was a question.
**Wendy Smoak** 17:44 I don't know where it is. I was trying to think about it. The one question that ran through my mind that I wasn't able to, like.
What if, when I'm using the Ruby Logger, I have made very careful… I have very carefully constructed the stuff that's going out to the Ruby Logger as pure JSON, so that my logging backend can pass it… can parse it?
And I was thinking, like, my initial reaction to that was.
like, don't add anything to it, or my logger backend is not going to be able to parse it, but I also don't know exact… I haven't been able to… I haven't been able to try it yet, so I don't know if that's just irrelevant, because there's already other stuff in there.
But I do know that, like, we… and just using the plain Ruby logger, we have… we try to output only JSON.
So…
having something else added that I didn't put there seemed like my initial reaction was, let's not…
To that one.
Like, the body should just be the whatever the body that… Came from the…
You know, that was going to be output to the other log… logging system, output through RubyLogger.
**Kayla Reopelle** 18:47 Okay, so then, yeah, if it should just be whatever was going to be output, then we would want formatted message for the message, instead of…
Probably, because you don't just see message in your loggers, generally. You generally see the message with the prog name included, because I think that's what's the default in, like, Ruby's formatted message, unless maybe I missed something. Sorry, my dog has just.
**Wendy Smoak** 19:12 I wonder what we have done.
**Kayla Reopelle** 19:14 Say that again?
**Wendy Smoak** 19:18 Let me… let me play with it a little more. I don't… yeah, I don't quite know what… what we're getting now. I haven't really been that… it's wrapped so much that I don't even know what there would be.
**Kayla Reopelle** 19:28 Yeah, let's…
**Wendy Smoak** 19:29 I just know, like, what our wrapper spits out, so we might be doing something else to it.
**Kayla Reopelle** 19:33 I think this can just be something we add on later on, if people are missing the prog name, or they don't like how their messages look. I feel like it doesn't have to hold back the initial release. But Rob, what were you saying? I cut you off.
**Robb Kidd (he/him)** 19:44 I was gonna say, I'm also unaware of the details of the implementations and the wrappers, but I agree with,
What is being proposed, that the… the…
Content of what gets passed to the original logging library for…
**Kayla Reopelle** 20:01 commission.
**Robb Kidd (he/him)** 20:02 To whatever should not get mutated.
**Kayla Reopelle** 20:04 Okay.
**Wendy Smoak** 20:06 I'll leave it the way it is.
**Kayla Reopelle** 20:07 With Jeff's message.
We'll leave it like that, with just the message, and then prog name will be in there.
**Wendy Smoak** 20:13 We can always add stuff, it's much harder to remove stuff.
**Kayla Reopelle** 20:15 Yeah, yeah, if someone's ever seen…
**Wendy Smoak** 20:18 And maybe I could go into attributes, or be optional to… whatever.
**Kayla Reopelle** 20:22 Right, right. OTL has this whole attributes option that.
**Wendy Smoak** 20:27 The Ruby Logger doesn't, so…
**Robb Kidd (he/him)** 20:30 So, I mean, I… you could choose to put more stuff on the hotel.
Right.
**Kayla Reopelle** 20:35 I guess we could add an extra attribute for prog name if we wanted to pass everything from the format message call along.
Would that be preferred?
**Wendy Smoak** 20:46 I mean, this is… I think start with this, this is fine. You can always add stuff later if someone comes along and says…
**Robb Kidd (he/him)** 20:57 So, the…
**Wendy Smoak** 20:59 They're unhappy.
**Robb Kidd (he/him)** 21:01 You go.
What was that, Wendy? I think I talked to…
**Wendy Smoak** 21:07 I was just saying, if someone comes along later and wants… it's easy enough to add something later, but if you pile it all in there, you can never get rid of it, because someone… someone will be using it.
**Robb Kidd (he/him)** 21:16 It becomes load-bearing for somebody.
**Kayla Reopelle** 21:18 Yes, yes, exactly.
**Robb Kidd (he/him)** 21:20 So the, if I understand it, prognan's getting passed in, but we don't use it.
**Kayla Reopelle** 21:25 Yeah, yep, we don't use it, we're just giving the straight message. So, what we're passing along and setting as the body may not necessarily be exactly what people see in their standard output.
But.
**Robb Kidd (he/him)** 21:40 Let's find out we have a bug them later.
**Kayla Reopelle** 21:42 Yeah, exactly.
Exactly. So, formatted message is what you're used to seeing, like, in your Rails terminal, for example.
**Wendy Smoak** 21:51 I could be convinced either way, but it's already like this, so let's just keep rolling.
**Kayla Reopelle** 21:54 Let's just leave it. Yeah, it's fine.
Thank you for bringing that comment up. Seeing as I wrote it almost a year ago, I forgot
Good.
**Wendy Smoak** 22:03 I just remember reading through this and thinking about it, and then I kept going to try it out. But yeah, it…
I mean, it prepends itself, and… I mean, I'm not using this code exactly.
Copy, paste, modified, but, it did the thing.
**Kayla Reopelle** 22:20 Cool.
Cool, cool.
**Wendy Smoak** 22:21 I've just got an app that's got, like, nested tags, and I wanted… so now I'm wondering if I'm not going to get the nested tags, because we're not.
**Kayla Reopelle** 22:29 And if.
**Wendy Smoak** 22:29 I'm at a blogger!
**Kayla Reopelle** 22:31 We'll see. If not, you know, if it's easy enough to fix, we'll have code we can update, yeah.
Alright, cool. I'll… yeah, get that fixed up, and then,
Let's see, I need an official approval in order to release it, so,
I guess I'll just ping y'all since you were here today in a comment, and…
We can go from there.
**Wendy Smoak** 23:19 Thank you.
**Kayla Reopelle** 23:20 Yeah, no problem. Thank you for bringing it up.
Let's see, what have we got going on in the core repo? Bringing up the minimum Ruby version…
This is still not passing, so that's probably gonna be a little longer. I think it just needs to get added to the CI.
Speaking of the CI, for a few weeks now, we've had, we've started using OTELBOT in Contrib.
so that that way we don't have to push an empty commit in order to get the CI to run. I think that the bugs have been worked out, as long as we don't have any new surprises in terms of permissions changes. We hit some road bumps with,
EZCLA, where…
it kind of blocked us from editing PRs, but that should be resolved for both of these repos now.
So if we want to have consistency across both of the repos, this is the way, that we would do it, so…
Oh, and it looks like Arielle already approved it. But I guess, does anyone here have any concerns about that approach?
Okay, cool.
Okay.
Schwan, you've been working on more metrics stuff, and I do appreciate it, and I apologize for not having time to look at it. What to you, if I could look at one metrics PR this week, what's the one that you would want to have reviewed?
**Xuan Cao** 24:50 Oh… One… One with,
Explain to his current merge.
logic.
**Kayla Reopelle** 25:02 This one?
**Xuan Cao** 25:04 Yes, yes, yes ma'am.
**Kayla Reopelle** 25:06 Okay, sounds good.
Alright, we'll start from there. And…
I guess… yeah. Is there… is there a second one, if there were two?
I know I can get one done, but two might be more.
**Xuan Cao** 25:22 Yeah, and then…
This, test case for the machine store, and let me show you, because this is, some blood, or PR, or another
Here, that is already merged.
**Kayla Reopelle** 25:39 Okay, sweet.
Thank you.
Awesome. Alright, anything else? Any issues in core?
Batch span processor… Exporter error handling does not provide useful information. Yes, this has come up.
before.
The… the error, kind of from that failure status, doesn't really get passed down, so it just says unable to export.
And I think… Pretty much every time I…
see that personally. I, like, go into the code and then add more logging, so it might be helpful to add more logging for users as well.
Has anyone else run into this, or have any ideas about how to fix it?
**ericmustin** 26:46 We… Have that hacky… sorry, Rob, I apologize.
**Robb Kidd (he/him)** 26:53 I think… no, your intro, if we have that hacky, is probably what I was gonna say. So, keep going.
**ericmustin** 26:58 the metrics, this abomination. We have this, like…
**Robb Kidd (he/him)** 27:04 the metrics reporter. You could…
**ericmustin** 27:05 Yeah.
**Robb Kidd (he/him)** 27:06 Implement your own.
And it will increment,
error types, and in there, there are some metrics that… I… in the past, I have implemented a logger that would take the metrics reporter reports.
**ericmustin** 27:21 Yeah.
**Robb Kidd (he/him)** 27:23 As a way to choose to opt in to more things on my console, to get specifics about.
**ericmustin** 27:29 Dear.
**Robb Kidd (he/him)** 27:30 what the trouble is. I don't know what… how to better do that.
**ericmustin** 27:35 the… the Chesterton's fence is not, like, that excite… it was, like…
Shopify and GitHub, where StatsD shops maybe are, I don't know.
They quickly, you know, before anything was really spec'd out in metrics land, they're like, we just want some metrics on this, let's…
Technically correct way of shoving it in, but, like, the least spec-compliant way that while still being, like, spec-compliant, was this, like, funky…
class. So yeah, it's overdue for some holistic improvements,
**Robb Kidd (he/him)** 28:07 I mean, there is some weird meta here, how do you observe your observer?
yeah. Because if you're having trouble, if your SDK isn't configured right, and exporting, if you were to…
**ericmustin** 28:18 used.
**Robb Kidd (he/him)** 28:19 hotel metrics.
**ericmustin** 28:20 Oh my god.
Like, I.
**Robb Kidd (he/him)** 28:22 Yeah.
**ericmustin** 28:23 We… I'm happy to, on this issue, for, like, you know, productivity's sake, like, I'm happy to, point, Hazel in the direction here, and I'd be pretty sure that they're pretty…
they're pretty hands-on. But yeah, like, it's not… it's a symptom. Like, this is a code smell, I think, for sure.
**Kayla Reopelle** 28:45 And, like… Yeah.
**ericmustin** 28:46 yeah, it'd be good to, like… I… you know, I don't… I don't own Hotel Ruby, so I can't really make too many, you know, pronouncements here, but, like, this would be an area where, especially now that our metric stuff's in a better… in better shape, like.
**Kayla Reopelle** 29:00 Hmm.
**ericmustin** 29:01 we could probably revisit and think about. Is this something… yeah, how, like.
**Robb Kidd (he/him)** 29:06 export.
**ericmustin** 29:06 At the very least.
**Robb Kidd (he/him)** 29:07 If you're having export errors, and then you export your hotel metrics about them.
**ericmustin** 29:11 Yeah. Probably not gonna see.
**Kayla Reopelle** 29:13 Yeah.
I mean, I think it could also…
Maybe be just helped by having a stack trace included in the message, or, like, an option to turn that on.
**ericmustin** 29:23 Yeah.
**Kayla Reopelle** 29:24 I think that…
also, like, making sure that those metrics are compatible with the new metrics SDK, and moving out of the hacky territory now that we're getting some wider adoption would be good.
**ericmustin** 29:36 Yeah.
**Robb Kidd (he/him)** 29:36 Yes. I think that we could provide the hack, so, like.
**Kayla Reopelle** 29:39 Yeah, you can get.
**Robb Kidd (he/him)** 29:40 over this hump with this hack, and log…
Whatever this metric is to ultimately.
Or any metric is tickled. Any of the error ones.
And then
Look and see, maybe we need a logging option and a metric option for how's my exporter doing?
**Kayla Reopelle** 30:00 Yeah.
**ericmustin** 30:01 Yeah.
**Kayla Reopelle** 30:01 Good.
So, do one of you guys want to follow up with Hazel, or…
**ericmustin** 30:09 I totally can follow up with Hazel, and totally cannot do any of the good stuff that we should be doing that Rob has explained very thoughtfully. Baby steps.
**Kayla Reopelle** 30:18 I'll just work on responding for now.
**ericmustin** 30:21 Cool, just give me Amher.
just dealing with emergency… whatever. I'm dealing with work besides… on the side here, but I will… I will respond by end of day. I'll respond by end of day and try to… and try to provide, I think we also, floating around, like, we have an implementation of it somewhere, of, like, the class they wanted, or it's, like, in the code comments.
**Robb Kidd (he/him)** 30:38 It's a super easy class to do.
**ericmustin** 30:40 Yeah.
**Robb Kidd (he/him)** 30:41 Whenever… whenever a counter… whenever a metric is tickled, log it instead, and…
**Kayla Reopelle** 30:46 Mmm, okay.
**Robb Kidd (he/him)** 30:47 And then you'll have more information.
**Kayla Reopelle** 30:50 Cool.
**Robb Kidd (he/him)** 30:52 Probably not snacks.
**Kayla Reopelle** 30:52 Goodness.
**Robb Kidd (he/him)** 30:54 Get up somewhere.
**Kayla Reopelle** 30:55 Yeah, more details.
More details sound helpful, regardless.
Cool. Alright, we've got some new PRs here. One, you know, kind of similar to what we saw in Core.
Ariel has a PR to bump the minimum Ruby version to 3.2, and Rails 7.1 for the minimum Rails version.
It also adds testing for JRuby 10, and in order to do that, had to stop testing Mongo instrumentation on JRuby, because it seems like that package is currently unmaintained. There's been PRs open, including one from an OTL user, for a while, trying to
get them to accept a change for JRuby support, but that hasn't happened, so… As a workaround…
If people are comfortable, we'll just stop testing JRuby on Mongo.
For now.
But, yeah, I think…
That could use review. Looks like we had a few PRs, too, related to adding some RSpec attributes, and…
I didn't see any problems with them. I also am not an RSpec instrumentation user.
And… so I'm not sure if anyone here is and has other opinions.
This one is just to help make sure that when you're doing a one-liner test, that the description is valuable.
The other one is to add the example ID attribute, which is helpful for dynamically generated tests, so that you can identify
Which, like, which specific test failed?
So, this is adding… adding that as well.
And I think this new PR, yeah, it was open this morning to add some factory-bought instrumentation.
I'll… I was planning to check in with them to see if they would be interested in being marked as the maintainer for this.
I think that's probably contingent upon us accepting it.
But, yeah, does anyone else have any other thoughts on…
Any of these testing-related PRs right now?
Okay.
Let's see, let's see…
**ericmustin** 33:27 It would be good to get JRB10 support for my organization. I think the log stash people care about that.
**Kayla Reopelle** 33:35 Okay.
**ericmustin** 33:37 That was it. That was my comment. I… so…
**Kayla Reopelle** 33:41 Yeah.
**ericmustin** 33:41 If you find yourself stuck with… but I wasn't paying attention, where do we… so… Holy shit. So bad.
**Kayla Reopelle** 33:47 Yeah, so J4B10, we didn't actually have to make any changes, like, we've tried testing it a few times, it's just Mongo that's incompatible.
And… and that's… there's issues in the Mongo gem to try to fix that, but they.
**ericmustin** 34:02 Haven't been.
**Kayla Reopelle** 34:03 So, we're not gonna hold back our testing on JRuby10 anymore.
**ericmustin** 34:06 Yeah, we don't want to help the manga. Yeah. I don't work at a direct competitor to Mongo.
Now we're gonna ask now, Rob, for context. This is my joke. I, okay, do we… what action can I take here to be helpful, or it sounds like it's already approved, and we're just…
**Kayla Reopelle** 34:25 I think, yeah, yeah, if anyone else wants to approve it, I'm not sure why.
**ericmustin** 34:29 Fuck it.
**Kayla Reopelle** 34:29 else bleeding, but.
**ericmustin** 34:32 Okay, I will be around if something fails and he needs some yellow pearls.
**Kayla Reopelle** 34:37 Cool, sounds good.
Oh, thanks for these comments in the chat about the error handler.
I'll add those… 2…
We don't need the whole chat, but… Alright, cool.
Then… let's see, what else have we got here?
Oh, so since we… we talked about Puma a while ago now, one of our concerns was related to exporting a library, or, like, shipping a library that didn't really have instrumentation, as in it wasn't outputting spans, but since we have released the Anthropic library.
In that way, where it's just, like, a context propagation assistant. I don't think that should hold us back from the Puma library.
But we are kind of back still in that SDK…
territory of an SDK method being called in instrumentation, so you'd have to…
You'd have to have some protections for that.
Actually, wait a second, this may have changed since I… Last looked at it.
I guess not.
**Robb Kidd (he/him)** 36:01 We had… Right now, this is… okay.
Yeah, if it can avoid SDK-specific calls… I commented on this.
That's true.
**Kayla Reopelle** 36:21 Hmm.
**Robb Kidd (he/him)** 36:21 Probably reread.
**Kayla Reopelle** 36:23 They added an early return if the SDK is disabled.
Might just need to add more…
Respond to or define checks here?
**Robb Kidd (he/him)** 37:03 Treats a provider.
I don't see… tracer provider at the API level has a shutdown.
**Kayla Reopelle** 37:14 Yeah.
Okay, but…
**Robb Kidd (he/him)** 37:19 sync.
**Kayla Reopelle** 37:19 Yeah.
**Robb Kidd (he/him)** 37:19 Go ahead.
**Kayla Reopelle** 37:21 Oh, that makes it a big difference between the Anthropic. I forgot about that before I brought this up today.
**Robb Kidd (he/him)** 37:28 But I… I don't… So here's where it gets…
is it spent… is it spec'd for an SDK to provide a shutdown method?
**Kayla Reopelle** 37:38 Hmm… I believe so.
**Robb Kidd (he/him)** 37:39 If it's spec'd, you can hope that
whatever your SDK is, the tracer that the tracer provides… the…
Concrete implementation of the tracer provider, probably have a shutdown.
**Kayla Reopelle** 37:54 Yeah.
**Robb Kidd (he/him)** 37:54 the spec sense.
**Kayla Reopelle** 37:57 Where's the tracer provider?
There we go. Yeah, so it is spec'd there.
**Robb Kidd (he/him)** 38:08 Pardon me, it's like, if a tracer provider needs to shut down, then it ought to be at the API level.
**Kayla Reopelle** 38:13 Wow. Yeah. Yeah.
But that's not how it's structured here, so… So…
**Robb Kidd (he/him)** 38:20 So it's probably fine?
**Kayla Reopelle** 38:23 Yeah.
**Robb Kidd (he/him)** 38:24 probably using the official OTEL SDK, and if they're not.
and using some other SDK that doesn't have a shutdown method.
I'm a trans provider, we'll say, well.
You're using a tracer provider that doesn't follow the spec.
**Kayla Reopelle** 38:41 Yeah.
**Robb Kidd (he/him)** 38:42 You can… you can… there… Monkey Patch is your option, and time.
**Kayla Reopelle** 38:46 Yeah.
**Robb Kidd (he/him)** 38:46 And talk to your SDK.
vendor.
**Kayla Reopelle** 38:49 Distributor, yeah.
**Robb Kidd (he/him)** 38:54 It's probably fine.
**Kayla Reopelle** 38:57 Maybe I'll… Francis and Robert in here, and see if they have opinions or suggestions.
2… To avoid any, accidental API breaking change.
Problems like we did recently.
**Wendy Smoak** 39:15 As simple as using the AND dot?
It's called the shutdown, so that it fits…
**Kayla Reopelle** 39:23 Well…
**Wendy Smoak** 39:24 If you have a tracer provider… oh, no, that's for…
**Kayla Reopelle** 39:28 that. You have to do the whole if-defined thing.
**Wendy Smoak** 39:31 Yeah, something else.
Oh, no, I like that response, too.
**Kayla Reopelle** 39:36 Yeah, but before it shut down.
**Wendy Smoak** 39:38 as well.
Not… Yeah, why is that one not done the same way?
**Kayla Reopelle** 39:47 So, I think the meter provider and the logger provider were marked as optional because they're not stable yet.
**Wendy Smoak** 39:53 So, since the time.
**Kayla Reopelle** 39:54 included in the SDK, but the tracer provider is stable. They decided not to…
**Wendy Smoak** 39:58 And I was just assuming that it's there, but it might.
**Kayla Reopelle** 40:01 Yeah.
**Wendy Smoak** 40:03 It's… it's supposed to be there, but it might not have a shutdown.
**Kayla Reopelle** 40:06 Yep.
**Wendy Smoak** 40:07 Okay.
**Kayla Reopelle** 40:10 Yeah, because we're only installing the API as a dependency, and the API doesn't have a shutdown method, only the SDK does.
So…
**Robb Kidd (he/him)** 40:20 But when you're actually using it.
**Kayla Reopelle** 40:22 But when you're… right, when you're actually using it.
**Robb Kidd (he/him)** 40:25 You're gonna have an SDK, or it's not doing it.
**Kayla Reopelle** 40:28 Yeah.
**Wendy Smoak** 40:28 Which may or may not have a shutdown method, because it's not in the API.
**Kayla Reopelle** 40:32 Right.
**Wendy Smoak** 40:32 It's not…
**Kayla Reopelle** 40:33 But it is in the…
**Robb Kidd (he/him)** 40:34 it's not spec'd at the API, so the API, no op tracer provider to give you a shutdown method. Yeah. But it's spec'd for an SDK, too.
**Wendy Smoak** 40:43 Ugh.
**Robb Kidd (he/him)** 40:44 Yeah.
This is one of those that's probably fine.
**Wendy Smoak** 40:48 It's probably fine, yes.
Put a line in the… in the dogs, like, if this…
Now, if this doesn't work, here's why.
To save someone else the investigation. Yeah.
Hmm.
**Robb Kidd (he/him)** 41:06 And it's gonna… let's see here… it's gonna blow up inside trying to shut down your puma.
I don't think it's inside any of our… Error headway.
**Kayla Reopelle** 41:18 Mmm.
Yeah.
It'd be good to test it, I guess, with…
**ericmustin** 41:23 I suppose… I asked Nate, back about
this, and he said he didn't care. He just said it didn't look like anything specific to do whatever you think is best.
Yeah. Ouch. Ouch.
That's all I got.
**Robb Kidd (he/him)** 41:39 We could, we could, like Wendy mentioned it, we could rub some and dots on this, too, and just…
**Kayla Reopelle** 41:43 Like, that's…
**Robb Kidd (he/him)** 41:44 effort. We're gonna try and shut down, but if.
**Kayla Reopelle** 41:46 That stuff doesn't exist or doesn't have the same name as the spec expects.
**Wendy Smoak** 41:51 It's either the AND dot, or the, like, the respond to, or the defined, or… yeah, try and AND dot are the same, but…
**Robb Kidd (he/him)** 41:59 They behave a little differently, but…
**Wendy Smoak** 42:01 Yeah.
**Robb Kidd (he/him)** 42:02 I made a comment about it.
A month ago, I apparently remember last week.
**Kayla Reopelle** 42:06 Yeah.
**Robb Kidd (he/him)** 42:09 Hmm…
**Wendy Smoak** 42:10 So, ship it, and if someone reports a bug, then do something else.
**Kayla Reopelle** 42:16 Yeah, right, it's a zero-dot package, so as long as we're not… Including…
**Robb Kidd (he/him)** 42:23 This one is this, Puma helper.
Something that we would put in the awl.
**Kayla Reopelle** 42:30 I… don't know.
I mean, when do you…
**Robb Kidd (he/him)** 42:35 technology.
**Kayla Reopelle** 42:35 It's too, but with passenger, right?
**Wendy Smoak** 42:37 Yeah, and I just, I mean, I just put it in the… my hotel config, like, config, open telemetry, I just put it in there, so if we're getting passenger or, like.
Worker shutdown, whatever that… there's a hook.
I just stuck them in there, and it's fine.
**Robb Kidd (he/him)** 42:59 It's much like this goes back to our, historical, resistance to doing anything at exit.
**Kayla Reopelle** 43:06 Yeah.
**Robb Kidd (he/him)** 43:08 Because, that's something that application developers should control, what happens when.
As things are shutting down.
**Kayla Reopelle** 43:16 So, I guess, does this make maybe more sense not as a package, but as a document in the hotel docs for troubleshooting, for people to…
Add this manually…
**Wendy Smoak** 43:32 I mean, I don't have Jagua being in there, because I had to learn about this need to, like, I didn't… when I first started using it, like, I didn't know it was going to shut it down, it just, like, I just added the things from the example app and started using it, and it was fine, and I only learned about it
about the need to shut down from some, you know, something I read or whatever, so…
**Kayla Reopelle** 43:53 Yeah.
**Wendy Smoak** 43:53 I would not mind if it did the right thing by default when I added the instrumentation for Puma.
**Kayla Reopelle** 44:00 Okay.
**Wendy Smoak** 44:01 It's just this weirdness with the AP… with something being in the SDK, but not… the SDK is required to do something that's not in the API, that… that's just a bug in the… in the spec.
**Robb Kidd (he/him)** 44:13 Yeah.
**Kayla Reopelle** 44:14 Yeah.
Okay, I…
**Robb Kidd (he/him)** 44:19 We could always add a shutdown method.
to our API tracer provider, no op thing.
**Kayla Reopelle** 44:26 Just a matter.
**Wendy Smoak** 44:26 that wasn't allowed, because it's not in the API. I mean, it's not in the spec for the.
**Kayla Reopelle** 44:30 Yeah.
**Wendy Smoak** 44:31 We weren't supposed to.
**Kayla Reopelle** 44:32 Yeah, I got my wrist slapped for due.
**Robb Kidd (he/him)** 44:34 Really?
**Kayla Reopelle** 44:35 them recently, because of… yeah, because at.
**ericmustin** 44:38 That was my fault, sorry.
**Kayla Reopelle** 44:39 weren't… I mean, we did it together, you know? Hand in hand.
Yeah. It was like a national.
**Robb Kidd (he/him)** 44:46 or wrist lapping?
**Kayla Reopelle** 44:47 Y-yes.
**ericmustin** 44:49 Precisely.
**Kayla Reopelle** 44:51 So.
**ericmustin** 44:52 Now we know how to get friends.
attention.
**Kayla Reopelle** 44:55 Yes, yeah, he is still watching. Hi, Francis, thanks for setting us straight.
**Robb Kidd (he/him)** 45:02 And what was the issue? Putting something in the API that wasn't scripted.
**Kayla Reopelle** 45:04 Yeah, basically there wasn't an attributes method in the API, but we added one there to kind of help with a problem that was being experienced in the Lambda instrumentation, where you would call attributes, and it wouldn't be there. But there is no attributes method in the API, so…
The guidance was to remove that,
And only have the methods that are in the API in the API.
**Robb Kidd (he/him)** 45:29 Well, I guess, Puma Plugin could get some, guarded calls to, like.
**Kayla Reopelle** 45:34 Yeah. If it's there, then…
**Robb Kidd (he/him)** 45:36 So that it doesn't throw a bunch of errors.
That'd probably be my suggestion.
So that you don't screw up your PUMA shutdown.
**Kayla Reopelle** 45:44 Yeah.
I think that's reasonable, and…
I'll add that as a comment, and maybe that can unblock the PR, and…
Yeah, and then, I guess, make sure that…
Francis and Robert are aware of this, just in case they have any strong opinions before we roll it out.
I just remembered that I have a doctor's appointment I have to drive to.
So I should probably stop sharing my screen, but is there anything else that people want to talk about? I mean, someone else can also just take over, and you guys can continue the meeting without me, that's fine too.
**ericmustin** 46:26 I can share.
**Kayla Reopelle** 46:28 Okay, cool.
Alright, I'll stop my share.
**ericmustin** 46:31 Yeah, safe travels.
**Kayla Reopelle** 46:32 Thanks, yeah. Alright, I'll see you guys next week.
**ericmustin** 46:38 Okay, if anyone can't see my screen, let me know.
Okay.
we're at… Happy reports.
Yeah, what happened? Now, what other,
What other things do we want to talk about?
Okay, I saw… there was a question from the Mastodon folks in Slack around Sidekick.
Instrumentation that we could… spend a couple minutes on, if people want.
I didn't have a clear answer to it,
I don't have any happy reports, and I have no…
pressing other things to bring up. I know some folks here have outstanding PRs, though, if we wanted to go over theirs, or talk about… talk through those as well.
I would… Anyone else, sir?
Thoughts, or…
Okay, take care.
Silence is a… Tacit acknowledgement that I can do whatever I want. Okay. I, let's talk about…
I did… let me see if I can quickly find,
Oh god, I'm in the wrong browser, that's why.
Sorry. Let me at least share the thread that I was talking about in here.
Sorry, I realize I'm on.
**Wendy Smoak** 48:27 Is there a way to add Sidekick's job parameters to the hotel trace?
**ericmustin** 48:31 Yes. But I…
**Robb Kidd (he/him)** 48:35 I agree with, Mariel's first answer.
**ericmustin** 48:39 Let me pull it up.
Oh wait, you'll see all my weird side checks.
I don't know what to do.
**Wendy Smoak** 48:48 And is Ariel saying that…
it shouldn't… so we just had that… we had just had that conversation about baggage. Like, is he saying that don't put sensitive stuff in with the trace, because that might happen, and it could go everywhere, or just, like, in general?
**Robb Kidd (he/him)** 49:03 It's not as toxic as baggage. What is being… what is being requested is not as toxic. It's just the danger of, like, shoveling everything, all the information you give a job.
putting that on a… on a span in your trace, risks of, like, how much data are you putting into your job parameters? If it's just,
If you're doing the recommended sidekick of, here's an ID for a model that you, Java, are then going to go query the database to get all of the specifics to work on, instead of shoveling all of the specifics into the job parameters.
So that Ariel's like, Recommend avoiding, like, just shoveling job parameters onto a trace, because it might be leaky.
And then it's… and then you have sensitive information in your trace data, not baggage, but a span will have sensitive information.
**Wendy Smoak** 49:50 Okay.
**Robb Kidd (he/him)** 49:51 And so I'll go to yours.
observability backend, which probably isn't cleared for PII, type of thing.
So, the question would then be, like, Whit.
**Wendy Smoak** 50:06 Do you do it at all?
**Robb Kidd (he/him)** 50:07 Right, you now have to… the application developer now needs to choose which parameters of the job they want to put on.
and how to make that show up.
And I…
**ericmustin** 50:18 Yeah.
**Robb Kidd (he/him)** 50:19 off, hey, it's been a while since I looked at this academic experimentation, I don't know what sort of hooks you have.
**ericmustin** 50:23 Yeah, also, I wonder at what point they would have access to the active span within their, you know.
**Robb Kidd (he/him)** 50:30 Well, there's a job span in the… like, while the job's running, you have an active job span.
**ericmustin** 50:35 Yeah.
**Robb Kidd (he/him)** 50:36 You have a span that represents the job active.
**ericmustin** 50:41 Right. Can't say act.
**Robb Kidd (he/him)** 50:42 What does it say?
**ericmustin** 50:44 But it's.
**Wendy Smoak** 50:44 So maybe just an example in… for the… for the doc?
Maybe just a little thing?
I'll just put it here, and someone can add it to the dog.
I think they're… I think they're just asking for, like, how… how do I even…
do anything here. Example implementation.
**Robb Kidd (he/him)** 51:00 Yeah.
**ericmustin** 51:01 Yeah, I don't, I think it's… You added?
**Robb Kidd (he/him)** 51:06 Your job has parameters, and if you want them on your spans, you… do your jobs.
**Wendy Smoak** 51:12 Yeah, but how do… how do you do that? Like, what's… what do you… how do you… how do you get a hold of the… this active span that is in there? Is that in the doc?
**Robb Kidd (he/him)** 51:19 Yeah, it's a current span.
**ericmustin** 51:22 I think.
**Wendy Smoak** 51:22 Okay, that may be all they're looking for, like…
**Robb Kidd (he/him)** 51:24 That's how you would get.
**ericmustin** 51:25 No.
**Robb Kidd (he/him)** 51:26 span.
**ericmustin** 51:27 he's pretty… Rena.
**Wendy Smoak** 51:29 Who knows?
**ericmustin** 51:29 the, experienced with our SDK.
**Robb Kidd (he/him)** 51:35 I think his hope is that he doesn't have to…
**ericmustin** 51:39 ADA doesn't want.
**Robb Kidd (he/him)** 51:40 And choose what attributes.
**ericmustin** 51:41 Yeah, yeah, he'd like…
**Wendy Smoak** 51:42 Oh.
**Robb Kidd (he/him)** 51:43 That's what we're saying, oh, my job.
**ericmustin** 51:46 Yeah.
**Robb Kidd (he/him)** 51:46 on… on my…
**ericmustin** 51:48 Yeah, and just, like, grab these. He'd like, like, a config option that would allow, an array of symbols, or whatever, of parameters, or something.
**Robb Kidd (he/him)** 51:57 Which is a reasonable config option? What job parameters would you like on.
**ericmustin** 52:01 Yeah.
**Robb Kidd (he/him)** 52:01 friends.
**ericmustin** 52:02 I, I don't see the harm in it, but I can understand the footgun.
Yeah, I can undersee the Fukon, but I feel like as long as that Fukon
Is a user-configurable foot gun and not some default.
**Wendy Smoak** 52:16 He's in the hands of the…
**ericmustin** 52:17 People wanna… Default, default safety on.
Yeah. Sorry for the language, you know, but you know what I mean, is like, I… yeah, as long as I think that responsibility lies with the user, like, we don't necessarily…
need to, in the same way, DB obfuscation settings are like, you know, we give you the, you know, the fire hose if you want it, there's some, you know.
It's a buyer beware situation at that point, but
Yeah, I don't know. I mean, I…
I think it's maybe worth tagging as an issue, you know, we could see if he'd open an issue and, like, understand what the…
If there's broad interest in that, which generally they tend to be early to things that other people will find useful.
It seems like a reasonable feature request. But yeah, maybe in the…
I don't know if even we have in our,
example instrumentation, like, you know, we have, like, some sidekick sample, like, I don't think we really have…
You know, spent some quality time with Psychic Constitution a while back.
Here's, like, our example of Sidekick is pretty basic, we're just… I'll share my screen.
Is this right? Yeah.
You know, it's, it's just like.
So, like, I guess at this, you'd have to add a,
You know, within your job, you'd add… some…
you know, logic here within perform, I suppose, that grabs the active span. I'm not entirely…
Yeah, I don't know, it's…
**Wendy Smoak** 53:57 I.
**ericmustin** 53:58 Okay, I think it's valid to be raised. That being said, it's just in Slack, so I don't know what action we can really take here to advance this. We could record the issue or something as a, you know.
**Wendy Smoak** 54:09 I'll ask… yeah, ask him to open a feature request for.
**Robb Kidd (he/him)** 54:12 Well, it's, yeah, as implemented today, you'd have to go and instrument.
You instrument your jobs and say, get me the current span and add these attributes to them.
**ericmustin** 54:22 Cool. Okay.
**Wendy Smoak** 54:24 You could do an include or something, and just, like, stick it on all of your jobs or something.
**Robb Kidd (he/him)** 54:28 I don't know if there's, I forget whether Psychic has some, like, before-job hook things.
**ericmustin** 54:33 Yeah, I guess that's the…
**Wendy Smoak** 54:35 Oh, my goodness.
**ericmustin** 54:36 That's where the, that's probably where the complexity comes in. It's like, certain jobs, you want certain parameters.
**Robb Kidd (he/him)** 54:41 If they have the base job class, all the jobs descend from the base job class, the base job class does the, like, put these parameters on the span, on the current span, and continue.
**ericmustin** 54:51 Yeah.
**Wendy Smoak** 54:52 And I don't want a map.
**ericmustin** 54:54 Yeah, yeah, you cut.
**Wendy Smoak** 54:55 Like, I have… like, the parameter in the job could be something from, like, 6 years ago, and now we call it something else, and the attribute I want on my span to go into something else entirely.
**ericmustin** 55:07 config option is, like, you want it to be… you want to almost offer infinite optionality, but it's like, you need to… it's a… I can understand, actually, as I think… as we talk through more.
**Wendy Smoak** 55:18 The list would work.
**ericmustin** 55:18 Okay.
Yeah, I think some map of a dictionary is fine, but, like,
Yeah, I could see people then being like, give me a Lambda.
I want to.
**Wendy Smoak** 55:29 Oh, yeah, because…
**ericmustin** 55:30 You know?
**Wendy Smoak** 55:30 Because now I have some that are kind of nested in the job.
**ericmustin** 55:32 Yeah, yeah.
**Wendy Smoak** 55:33 I want to, like, pull that out, but call it.
**ericmustin** 55:35 Or, I don't know, they're just like, you know, I, so I can understand. It might be interesting to see…
the usual, where it's like, I could…
peek around what Elastics Tracer is doing. Like, it would be interesting to see if there's prior art here within the…
cinematic universe of, you know, tracing SDKs.
Because it feels like something that probably, at some point, somebody shipped as a… just a nice feature, because some high-priority customer wanted it, but yeah, I don't, anyway, okay, well, yeah, thank you guys for covering that all. I can Slack, I'll just add a Slack.
confirming Ariel's response and saying, like, this might be an interesting feature if you're open to creating an issue or a feature request. They're usually pretty amenable to that stuff.
As open source enthusiasts themselves.
Yeah, I don't have any more rambling, but…
**Robb Kidd (he/him)** 56:26 that other thread where, Rena's asking about…
Putting the trace ID and parent span ID into the active record query log tags.
**ericmustin** 56:39 Oh.
**Robb Kidd (he/him)** 56:39 Was that answered? It's got more replies.
And it says, let's look at what Datadog does.
**ericmustin** 56:48 Awesome. Okay… he…
See, they… he's pinged Giuliano, who's been working with the Macedon folks. He's a dev advocate… er, you know, DevRel guy from…
Datadog, and they want to… What?
And, like, as code comments? Like, as SQL comments, or, sorry.
**Robb Kidd (he/him)** 57:17 I'm not quite sure.
**ericmustin** 57:17 Oh, right, as query log tags, which is… ends up being…
Oh, Jesus, sorry, not a comma in there, it's pretty gross.
**Robb Kidd (he/him)** 57:38 This one would probably take a little bit of looking into.
And we're all at the time.
**ericmustin** 57:44 Oh, yeah.
**Robb Kidd (he/him)** 57:45 I have to… I have to drop for my next meeting.
**ericmustin** 57:47 All good, all good. Yeah, this is… let's, let's see if there's movement on this,
And it's good seeing y'all, yeah. Cheers.
**Robb Kidd (he/him)** 57:57 Hi, everyone.
