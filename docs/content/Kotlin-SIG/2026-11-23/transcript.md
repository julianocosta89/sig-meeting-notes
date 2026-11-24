SIG: Kotlin SIG
Date: 2026-11-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb (Splunk Inc.)** 01:54 Hello, Mr. Lynch, Mr. Ho.
**Hanson Ho** 01:58 Good morning, good afternoon.
**Jamie Lynch (Palo Alto Networks)** 02:18 Cool. I'll just give it a minute for folks to add things to the agenda, and then we can make a start. I've gotta drop a bit early this week.
**Hanson Ho** 02:31 Might be a slow week in America.
**Jason Plumb (Splunk Inc.)** 02:34 Yeah, while we're waiting, has there been any talk about Thursday's Android meeting?
I want to cancel it, but was it… has anybody talked about it yet?
**Hanson Ho** 02:43 No, I think we forgot that, well, I mean, we didn't discuss the fact that next week is going to be Thanksgiving, and
**Jamie Lynch (Palo Alto Networks)** 02:52 I assume we can just cancel that one.
**Jason Plumb (Splunk Inc.)** 02:54 Yeah, I think so. Okay.
**Hanson Ho** 02:55 Great.
**Jason Plumb (Splunk Inc.)** 02:57 I'll see if I can get it removed from the calendar, I don't know how to… I don't think I can do that, but I can at least put a note in the… Yeah, there is a note… In the dock, but… I think the meeting is still on the calendar. I'll look at getting it removed, though, see what I can do.
**Hanson Ho** 03:14 We can post in Slack, and if there are folks that are around that want to discuss stuff, you know, it's fine.
**Jason Plumb (Splunk Inc.)** 03:19 Let's just skip it. I'll put a note in Slack.
**Jamie Lynch (Palo Alto Networks)** 03:25 Awesome.
Cool. So, first thing I just bought.
I check if we want to release. I think our last release was about 3 weeks ago. So… I don't think there's, like, anything pressing, but it would be good to keep up a cadence.
**Hanson Ho** 03:46 Yep, sounds good.
**Jamie Lynch (Palo Alto Networks)** 03:51 We can, achieve that sometime this week.
So… Next topic, API stabilization, I assume that might be Carlos adding to the notes?
So yeah, basically the context and propagator's API changes, I think they're following what the specification wants now.
Yeah, so it'd be really great to get, feedback on whether I've got the right end of the stick or mark one.
**Jason Plumb (Splunk Inc.)** 04:40 Carlos, were those your comments?
**Carlos Alberto Cortez (Dash0)** 04:43 Yeah, on the API stabilization, yes, those are mine.
**Jason Plumb (Splunk Inc.)** 04:47 Okay.
**Jamie Lynch (Palo Alto Networks)** 04:49 Awesome.
I'm very happy to receive Feedback async, if that works a bit better for you.
**Jason Plumb (Splunk Inc.)** 05:06 Was there any more to say on that, Carlos?
**Carlos Alberto Cortez (Dash0)** 05:08 Well, I can probably go over the items. The one that I would like to double-check after the call, I had forgotten, was the part regarding coroutines, because I had to go and check how coroutines work.
in, in Kotlin, as compared to other languages, but the initial part is, like, just minor points.
I don't know if you consider that extract, for context, has the same extract name as propagators?
There's a small risk that people get confused.
If you are fine with that risk, I think we can go with it, so it's up to you. The second one is the nesting. You have an example in the docs about how it works.
And you're, like, storing something in a span and swapping that?
And, yeah, when you're creating a context from another existing context, you're inheriting the values.
But when you are… when you have two separate contexts, and you're just setting one as active instead of the other, then all the previous values get erased.
during the duration of the context, because, you know, you're swapping that. And that example probably is not… Clear enough.
And it may confuse people, thinking that… Like, let's say you have context A, which has key A, and context B, which has only key B, and then you are… they are, you know, they don't share any keys.
So, when you are, like.
When you're activating B, an R was previously said, the user will expect that you will get both keys. And that only happens when they are, like, child's, you know, parent.
**Jamie Lynch (Palo Alto Networks)** 06:44 Makes sense.
**Carlos Alberto Cortez (Dash0)** 06:47 And it's not about implementation, of course, yeah.
**Jamie Lynch (Palo Alto Networks)** 06:51 Okay, awesome. I can take a look at these. Yeah, I hand for Alto Extract, big name the same, but that sounds, like, very reasonable.
**Jason Plumb (Splunk Inc.)** 07:01 What does the context extract do?
**Carlos Alberto Cortez (Dash0)** 07:06 You get the value of… you pass a key, if I remember correctly.
And then you just get the value. Like, for example, you said context, extract.
**Jason Plumb (Splunk Inc.)** 07:15 Yeah, it gets a value from the context by key.
**Carlos Alberto Cortez (Dash0)** 07:18 Right.
**Jason Plumb (Splunk Inc.)** 07:19 Okay, okay. Yeah, and Java, it's just called GET.
**Carlos Alberto Cortez (Dash0)** 07:23 Yeah, correct. And most languages use GET, or something like that.
**Jamie Lynch (Palo Alto Networks)** 07:29 Hmm.
Okay.
**Jason Plumb (Splunk Inc.)** 07:33 Cool.
**Carlos Alberto Cortez (Dash0)** 07:35 Well, otherwise, looks good. Yeah, very nice. I will just double-check the coroutines part, if you're fine with that, after the call. Sorry, I was busy with… stop here, but I will. Yeah, I need to check that. Otherwise, looks good. Thank you.
**Jamie Lynch (Palo Alto Networks)** 07:49 Awesome. Yeah, thanks for taking a look. I know how it feels, being busy.
Cool. Hanson, should we just skip to yours? Because I think that might be quicker than… My other point.
**Hanson Ho** 08:07 Yeah, so I've been trying to, like, consume this stuff from other projects, and We have constants to find, but the version of the semantic conventions is whatever version this, particular Kotlin SDK version happens to point to, so it's not super transparent. Like, if I want, like, version 1.44 of the semantic convention, I can't get it, or… or rather, I… I can't say I want this, from the Kotlin modules.
So it makes it difficult for custom… or for folks who want to use it to kind of depend on it. They're basically depending on a Kotlin version, which exposes a certain semantic convention version. So because of that, I kind of want to… somehow figure out how to specify this as. These aren't meant to be… you know, canonical one-to-one artifacts representing, the keys for a particular semantic convention version.
if you use it, you are basically tying yourself to what Kotlin defines, or the Kotlin SDK defines, as the semantic convention version that it has.
So, if you are using, if you're a Kotlin project, and you want to use the OTL SDK, and your instrumentation wants to use a particular version of the semantic conventions, you should use Weaver to generate your own, rather than take the constants, unless you're okay with being tied to the Kotlin SDK instrumentation. So, I want to make sure this is what we all feel is… should be the case, before either making some changes to specify that.
**Jason Plumb (Splunk Inc.)** 09:52 I think this is a real problem. I don't… what do you propose we do about it, though?
**Hanson Ho** 09:57 Basically define in the, in our repo, and say… and say as much. If you want to use this, if, sorry, if you want to use, Kotlin semantic invention, keys, use Weaver to generate your own, because there isn't a… OpenTelemetry, Kotlin, sorry, sorry, Semantic Conventions, Kotlin, equivalent of Semantic Conventions, Java.
This is… this is not even about the client side, any of that stuff, it's just the canonical core semantic conventions.
we have shared packages now in Weaver, in terms of templates for, READMEs and things like that. So if we want to share our templates so that folks can basically build their own, source code, from kind of, like, validated Kotlin templates, we could think about doing that. But it… Yeah, we just don't… we don't have… we just don't have modules that map 121 to semantic conventions, and we should state that, because it's very easy to say, hey, oh yeah, look, it's there, and depend on it, and we end up.
**Jason Plumb (Splunk Inc.)** 11:05 Sorry, man, I think I'm getting myself confused here. So, I was thinking more about the versioning mismatch, but you're saying that we shouldn't even use the generated classes?
Is that what you're saying?
**Hanson Ho** 11:16 We should, but some random OpenTelemetry project, or rather instrumentation, shouldn't shouldn't take the files that we generate, because if eventually they want to publish things like, schema, then what they publish should point to the semantic convention version.
And not, like, the hotel Kotlin version, which is what they would be tying themselves to if they consume our, artifacts that we produce.
**Jason Plumb (Splunk Inc.)** 11:49 Yeah, I see what you're saying.
**Hanson Ho** 11:53 So, like, a random Java instrumentation
**Jason Plumb (Splunk Inc.)** 11:56 I mean, that's also… sorry, that's also then, I think, suggesting that we shouldn't publish these.
If they're intended to only… if they should only be used inside the project, and using them outside the project introduces this weird versioning problem.
Then it kind of suggests that maybe we shouldn't be publishing them.
**Hanson Ho** 12:19 Well, I think, unfortunately with Gradle, anybody can depend on any Gradle module, so… Just because we have to have internal modules that depend on that means that that has to be a public module that has a public surface, but we.
**Jason Plumb (Splunk Inc.)** 12:33 So I say…
**Hanson Ho** 12:34 and it's.
**Jason Plumb (Splunk Inc.)** 12:34 I just mean, like, publishing it to Maven Central or some other place where someone could take a dependency on it.
**Hanson Ho** 12:42 I don't think we can avoid that, I guess, what I'm saying.
**Jason Plumb (Splunk Inc.)** 12:44 You certainly can, yeah, you can flag certain modules in Gradle and tell them not to be published.
**Hanson Ho** 12:51 Oh, and just have it as internal, kind of?
**Jason Plumb (Splunk Inc.)** 12:54 Yeah.
You can still build them, and other modules in the same project can take a dependency, but the publishing task can skip over publishing certain modules.
But I'm… I think, presently, we take a dependency on them from Android.
Unless that's been changed. I think there… I mean, I went through a bunch of hoo-ha at some point to actually set that up.
But I see this problem.
**Hanson Ho** 13:22 Yeah, I mean, Embrace takes a dependency on that as well.
**Jason Plumb (Splunk Inc.)** 13:26 On the Kotlin SunConf?
**Hanson Ho** 13:27 Yeah, it's public and it's there, and we're like, well, we depend on Kotlin SDK version anyway, so we just take that. But this.
**Jason Plumb (Splunk Inc.)** 13:35 Yeah, and you kind of hate to reinvent the wheel, like, even publishing your own… You know, even running your own Weaver jobs is kind of like reinventing the thing that exists somewhere else.
Right?
**Hanson Ho** 13:46 But that's… that's kind of like the Weaver, convention. It's like.
**Jason Plumb (Splunk Inc.)** 13:50 Yeah.
**Hanson Ho** 13:51 you should generate from… like, the artifact is actually not the dependency. It's kind of like translating the dependency into a platform-specific set of source code that you can use. So it's… it is confusing in that way, so unless the dependencies are reified, as actual source code modules, and then we'll need it for every, repository, basically, so client… the client-side conventions will have to publish.
Something like that. It just becomes one of these explosions, and… taking a dependency… it's almost like taking a dependency on, like, YAML, and then basically turning… well, it is, actually, literally, taking a dependency on a specific version, a piece of YAML, and then turning that into source code. So, I mean, I found this because I was trying to port the Embrace stuff over, and I'm like, oh… Yeah, I forgot about this. Ashley thought about it earlier, but haven't really done anything with it, and it's… Yeah.
Yeah.
**Jason Plumb (Splunk Inc.)** 14:54 Hmm.
**Hanson Ho** 14:57 Like, it's relatively easy generating this stuff, like… for Android, we are… we are doing that, and we're generating specific classes, that emit logs, right? So, we are actually adding value, to the semantic conventions, versus, The idea of having, like, you know, a set of binaries that anybody can just use that define constants, it's very attractive, but it also brings into mind the… The whole dependency issue, and the fact that we have to maintain something.
**Jason Plumb (Splunk Inc.)** 15:28 Yeah, so let me… let me just… I'm… I'm… I'm solving this problem kind of out loud, and I may be way off base here.
the… the rude problem is that if… I'm just gonna say Android, but if any project that wanted to take it… both take a dependency and publish their own schema.
Semantic convention schema.
And there's a… and it's a dependency, right, because of the way this federated semantic conventions work. When you… Android would declare, it would say, here's Android version 1.2.3 of our semantic conventions, here's a URL, we also take a dependency on this version of… The client-side conventions, and this version of the upstream conventions, right?
The version that's declared as an upstream dependency would then have to match the exact version That was used when Kotlin had published. And as long as those were correct, then Android could produce a schema that is valid and not problematic. It's just the ensuring That the version you declared in your schema is the same version that was published from the upstream… repository, whichever one that is. Keeping those aligned is what's challenging.
**Hanson Ho** 16:41 Yeah, you're basically saying, you know, you have a version that you are depending on, that you are saying you subscribe to, and then you have these artifacts that, that you're publishing, where… You know, the version isn't necessarily the version you might be actually using internally.
**Jason Plumb (Splunk Inc.)** 17:01 You could kick that can down the road and say, look, if you're gonna go through the effort of publishing a schema, you have to make sure that you're declaring it accurately.
Right?
**Hanson Ho** 17:13 Yes.
**Jason Plumb (Splunk Inc.)** 17:13 Okay.
**Hanson Ho** 17:15 there's a lot of can-kicking that could be done here, is the thing. It's… every time I look at it, it's like, hey, we should deal with it, and then every time I'm like, ugh… I don't kick it out.
**Jason Plumb (Splunk Inc.)** 17:24 know of a great way to solve this. I wonder if they're thinking about this in… Java at all, because they definitely, for years, have been publishing semantic conventions out of the Java repo, I… Bet you they switched… to Weaver 2 by now, but let's… let me do a fact check on that one.
**Hanson Ho** 17:44 But the… Semantic conventions Java is a whole different repo, though. It is. So whether they use Weaver to generate Excuse me.
witnessing canonically, the Science Conventions repo updates to 1.45, Java publishes 1.45, and there's alignment and inversion.
**Jason Plumb (Splunk Inc.)** 18:06 Oh, oh, oh, yeah, okay, so that…
**Hanson Ho** 18:11 We can take that entire… like, we talked about… we've definitely talked about this a couple times before, taking that entire model and replicating it, or we say… generate your own, and we kind of went halfway and say, here's some artifacts that are tied to an Android version, or a Kotlin version that… that you can look for, the semantic convention version, which is…
**Jason Plumb (Splunk Inc.)** 18:35 What if we… what if we match the version that we publish?
With the semantic conventions.
It would mean that we're producing two artifacts with two different versions during a publication… during a publish… during a release.
The normal release version for all the normal artifacts, and then the semantic conventions would just match their upstream… Version?
I guess the problem with that is if you publish more than once, like, if we published before Upstream, we'd have to skip over publishing the semantic conventions that we had already published, right?
**Hanson Ho** 19:10 Yeah, it's basically… it's basically two… two things in one repo. I mean, at that point.
**Jason Plumb (Splunk Inc.)** 19:15 It is.
**Hanson Ho** 19:16 Another repo.
**Jason Plumb (Splunk Inc.)** 19:16 Totally is, yeah.
**Hanson Ho** 19:18 This is absolutely kick can down the road a bowl, but every few months, I think about it, and…
**Jason Plumb (Splunk Inc.)** 19:25 Yeah.
**Hanson Ho** 19:25 I'll trip on, I think about it, so…
**Jason Plumb (Splunk Inc.)** 19:28 Damn.
Okay.
**Hanson Ho** 19:33 maybe… I mean, I'm not saying we kick the can down the road some more, but maybe we look at how we want to solve this for the Embrace use case, and then Android would probably want to solve it, or, you know, do it in the same way.
And we can see how we could do a sort of detachment, or if it's easy enough for Kotlin, or for the registry to be just… to use Weaver to generate. Because Kotlin really doesn't… or sorry, Android doesn't need to depend on Kotlin for this stuff. Android… Android generates it anyway. And for Embrace, we generate it anyway, but not that repo, we generate it for other ones. So… You know, Android, we don't even check in the generated source, which is… which is another… another option we could do, is… is, we generate, and then consume, and then don't export a module.
But, might break other people is, is… now, so… Yeah, I don't know…
**Jason Plumb (Splunk Inc.)** 20:40 Do you have any… do you have any thoughts on this, Jamie?
**Jamie Lynch (Palo Alto Networks)** 20:44 I have no strong opinions. I mean, I'm fine with just shipping… a lot of strings in a module, and if that doesn't work for people, I think they can build their own.
**Jason Plumb (Splunk Inc.)** 20:54 Yeah.
Okay.
**Hanson Ho** 20:58 I just want to clarify the, the, the, the version export dependency, so, you know.
it, it's, it's… Yeah, maybe I should have a solution before I bring this up again, because… I think I feel like I've talked about this several times with the same conclusions. We should figure it out, and then we don't figure it out, and it's fine.
**Jason Plumb (Splunk Inc.)** 21:22 to get people's gears turning about it, you know, that's reasonable, and there isn't always, like, a trivial or an obvious answer sometimes.
**Hanson Ho** 21:31 Well, there are trade-offs, right? I mean, the trivial answer is copy what Java does, but do we want to have that maintenance? You know, it's… I'd rather push up standard templates to the OpenTelemetry package project. Folks can then take those templates and generate the classes based on, you know, something in their project, and they can consume it themselves.
**Jason Plumb (Splunk Inc.)** 21:54 What if we put the Kotlin conventions inside of Java?
Just to riff on ideas here.
**Hanson Ho** 22:01 Oh, so… so turn… So have… have the Java repo generate Kotlin?
**Jason Plumb (Splunk Inc.)** 22:08 Yep.
It's a thought. I don't know that I love it.
anyone else would love it, but there is some amount of Kotlin support in other Java repos, so… It's, you know, it's maybe not the worst idea I've… well, it's the worst idea I've had today, but maybe not the worst idea I will have this week.
**Hanson Ho** 22:30 I mean, if we want to kind of… Oh, man.
**Jason Plumb (Splunk Inc.)** 22:37 Yeah.
**Hanson Ho** 22:37 It's not the worst idea.
Because I'll… it's not the worst idea.
**Jason Plumb (Splunk Inc.)** 22:44 Yeah.
**Hanson Ho** 22:50 Alright, let's… I'll think about it.
Yeah, think about it.
**Jason Plumb (Splunk Inc.)** 23:00 Yeah.
**Jamie Lynch (Palo Alto Networks)** 23:01 Cool.
**Jason Plumb (Splunk Inc.)** 23:02 Cool.
**Hanson Ho** 23:02 Alright.
**Jamie Lynch (Palo Alto Networks)** 23:04 I've probably got a minute or two. I just wanted to kind of go over this as a proposed workflow for reviewing the API, as we kind of work towards stability. So I thought what I'd suggest is I'll just create, like.
two to three items each week. I, like, create an issue with a link to the code and the spec, and then we can kind of compare What the actual API looks like, and then, like, compare it against what the spec says.
With the end goal being to remove that annotation.
**Jason Plumb (Splunk Inc.)** 23:51 Yeah.
**Jamie Lynch (Palo Alto Networks)** 23:51 And I think removing that annotation doesn't mean we can't change it until… Yeah, thanks.
But we're not stable yet. I think it just signifies that we're happy with it.
**Jason Plumb (Splunk Inc.)** 24:05 It's a step toward stability.
Cool.
**Jamie Lynch (Palo Alto Networks)** 24:10 Okay, cool.
**Jason Plumb (Splunk Inc.)** 24:11 Yeah, Jamie, I missed… I missed… so before you drop, you know, I missed… I missed an Android call because of KubeCon, then I had a medical thing last week, and then this week's gonna be Thanksgiving, so I'm missing, like, an entire month of Android, but I want you to know that I have… and I don't know if this was even discussed, I haven't watched the recording, but I've seen some of your issues around API surface stability and being normalized on Kotlin, and I definitely appreciate that, so just wanted to say that before you drop.
**Jamie Lynch (Palo Alto Networks)** 24:37 Awesome, no problem. Yeah, I think… yeah, it was good.
Talking it through last week, yeah, and… Kind of… Yeah, figuring out. There isn't really any good reason why we can't be thinking about 2.0.
**Jason Plumb (Splunk Inc.)** 24:51 Yeah, for sure.
**Jamie Lynch (Palo Alto Networks)** 24:53 Okay, thanks everyone.
**Jason Plumb (Splunk Inc.)** 24:55 Alright, thanks.
**Hanson Ho** 24:56 Thanks, bye.
**Jason Plumb (Splunk Inc.)** 25:00 See ya, Carlos.
