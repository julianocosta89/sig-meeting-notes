SIG: eBPF Instrumentation
Date: 2026-07-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Mike Dame (Odigos)** 00:26 Nikola.
**Nikola Grcevski** 00:32 This was a new experience, I had to log in.
**Mike Dame (Odigos)** 00:36 Yeah, it, like, automatically redirected me, and I don't know why it says Red Hat. Must be, like, the last time I used LFX.
login. Like, it didn't give me a chance to… Change anything.
**Nikola Grcevski** 00:47 Oh, you're still registered as a Red Hat employee, and… and Lenin's Foundation.
Look at that.
**Mike Dame (Odigos)** 00:52 Yes. Yeah. Huh.
For the record, not.
**Nikola Grcevski** 01:02 You haven't actually gone back to Red Hat?
**Mike Dame (Odigos)** 01:05 No, this isn't a big announcement call.
**Nikola Grcevski** 01:10 Not like Rafael last week, no.
**Mike Dame (Odigos)** 01:13 Yeah, oh, man.
**Mattia** 01:18 Hello!
**Tyler Yahn** 01:26 I know at the spec meeting.
People were confused by the, the meeting… Zoom meeting.
changeover, by people. I mean, I was, I just went to, like, the old meeting link. I'm trying to double-check right now.
**Nikola Grcevski** 01:48 Let me see where my colleagues are.
**Tyler Yahn** 01:51 Oh, okay.
No, it looks like the meeting link… looks like it's been updated.
On both locations on… okay.
But yeah, yeah, maybe, I'd go to the old meeting link, and see if I knew it was on that meeting, but I can't find it, so…
**Nikola Grcevski** 02:10 Hopefully they can'.
**Tyler Yahn** 02:11 find it either.
**Nikola Grcevski** 02:15 Do you think it's still live? I can go back in my calendar.
**Tyler Yahn** 02:18 I know, yeah, I know the, the specification meeting one was, and I was sitting there for, like, 5 minutes, just, like, while the meeting was going on, but I don't know, it looks like most everybody's here.
**Nikola Grcevski** 02:34 Let me… let me see if anyone's there. I'll come back.
**Tyler Yahn** 02:37 Okay. I'll also post this in, In the meeting notes, in case people… People are just sitting there.
Maybe?
There it is.
Well, cool. Alright, looks like Nikola's back. I posted the meeting notes there.
**Nikola Grcevski** 03:25 found… I found some stragglers that are coming for a new one, yeah.
**Tyler Yahn** 03:30 Okay, cool.
Yeah, good thing we did that then. Okay.
And then, if you haven't yet, please go ahead and add your name to the attendees list. If you have agenda item topics, go ahead and add them there as well. And, yeah, we can get started here in just a second.
Cool.
**Mario Macias** 04:00 Hello?
**Tyler Yahn** 04:01 Hello!
Did you get caught in the old beating link?
**Mario Macias** 04:06 Yes, and it was me who changed it in the doc, but for some reason, my local copy still holds the old one.
**Nikola Grcevski** 04:19 We're still missing Rafael and Giuseppe. I found him in the old call, but yeah.
**Tyler Yahn** 04:23 Okay.
**Nikola Grcevski** 04:23 Yeah.
**Tyler Yahn** 04:25 Yeah, they're probably trying to log into LFX.
**Nikola Grcevski** 04:28 Yeah.
**Tyler Yahn** 04:28 As long as they get, The guest thing, yeah.
**Mario Macias** 04:33 Yeah.
**Tyler Yahn** 04:35 Cool. Alright, looks like we got most people on now.
Alright, well, yeah, again, if you haven't yet, please go ahead and add your name to the attendees list. If you have agenda items you want to talk about, go ahead and add them there as well. We can, jump in here.
Cool. Mario, you wanted to start us off, talking about Grafana Hearts Hotel Community College?
**Mario Macias** 04:59 Oh, yes, just to inform you, maybe you already got the information through social networks, but tomorrow, Nikola and myself, we are talking about all we Yeah. In a Rafana.
public event.
**Tyler Yahn** 05:17 Oh, cool, nice.
Nikola, what time is this for you? Sorry, I'm not good at UTC.
**Nikola Grcevski** 05:25 Chuck, I think it's around 10?
11.
**Roy Reshef (Kubex)** 05:29 H11, it's the same time as now.
**Nikola Grcevski** 05:31 Yeah.
**Tyler Yahn** 05:32 Oh, okay, alright, cool, alright. Oh, yeah.
No, I was just wondering, I was like, that could be, like, super early, but I'll try to check it out.
**Nikola Grcevski** 05:39 It'll be 8 o'clock for you.
**Tyler Yahn** 05:41 Yeah, yeah, yeah.
Turns out, West Coast, you just have to get up early.
Well, cool, yeah, awesome. Thanks for, letting us know, Mario. I'm super excited. Yeah, I'd love a sneak peek, but I'll just have to be surprised when I join.
Yeah. Awesome. Okay.
Moving on, Nikola, you wanted to talk about, extending payload extraction to HTTP2?
**Nikola Grcevski** 06:09 Yeah, so I… I think I'm on the way with this. I just wanted to bring it up. I asked, sort of, for confirmation with Mattia and Nimrod, because, well, I'm trying to kind of create this sort of demo for GenAI, just like we have, like, a demo for regular Instrumentation. And then, obviously, I added, and I was working these days to get, Steven's PR, or Go, payload extraction, to move up to, To actually be able to do it, so now we have that, it's merged. However… As soon as I tried with HTTPS, Go immediately upgraded to HTTP2. And then, depending on the server, I tried with Anthropic, I think, and immediately, it just went, oh.
It doesn't work.
So I have a POC, I just wanted to bring a heads up. I think I found a way how to do this for HTTP2. The only thing I want to bring up is that There's no headers, so just the body. So, I have to write different kind of detectors for GenAI, because most of our detectors rely on some level of headers, like, we see the OpenAI in response, we see this in response, and so on, or in the request, but, As soon as we parse HTTP2 with the dynamic tables, headers, are unreadable. Or… these headers that the vendors will be sending will be in the dynamic table, so I can't touch them.
So I'm gonna have to add a little bit of different heuristics. If it's HTTP2, I'm gonna look at the URL, I'm gonna look at what's in the payload, like, model name mentioned, maybe, GPT, like, Gemini, things kind of like that.
But in general, it works. Like, I have something that… And then… hopefully we get that going for Go, then I was thinking of adding large buffers for HTTP2 in the… the path on the generic tracer, and then it should work for other languages, because I think things like Rust also aggressively upgrades immediately.
The client and other languages.
that's why we haven't seen it, because we have examples with Python, and do it.
But Goal, Rust, some of the more languages immediately through APL and Negotiate.
HTT2.
If it's… if it's HTTPS. Yeah.
So, I'm hoping that this week we'll have something going, and then I can write my examples.
I applied to a local Canadian conference called FOSSE, which is sort of like a Fosden equivalent. I found out that it was just started, so I was gonna talk about OB and this, so I need a demo, working demo.
So I'm really motivated.
Yeah.
**Tyler Yahn** 09:14 You don't want to write Python?
**Nikola Grcevski** 09:15 Well, I can demo with Python, but it would be cool to kind of have the… It'll be cool to have… You know, just like, goal works, Python works. This is the promise of Obi, right? You don't have to worry about the programming language, it's just there.
**Tyler Yahn** 09:34 Yeah.
**Nikola Grcevski** 09:36 And yeah, large buffers, you're right. I mean, I actually haven't checked, but I think HTTP takes a different path, and we don't push it, but I think I can just reuse the logic.
I think if we go into the protocol classifier, when we go HTTP2, I don't think there's any large buffers. It's just gonna, like, once I actually add.
the user space parsing for HTTP2, It's, it's gonna work.
In my opinion. I just need to add a little bit of code in the generic tracer to… send the HTTP2 packets, and then we'll… we'll have payload extraction everywhere for HTTP, which is going to be pretty cool.
**Tyler Yahn** 10:18 Yeah, I think so. That'd be really cool.
Yeah, I'm super excited about the POC.
**Nikola Grcevski** 10:24 Yeah, hopefully you'll see something from me today, then, sort of.
I ran into unexpected stuff, so no headers. Okay, great, but I don't know the content type.
Right? So, what's the content type? And then I'm like, oh, is it JSON? But then I'm like, great, but then they send it GZIP. So, I found out that for at least GZIP and ZSTD, I can actually peek into it and determine that it's that.
So… so I've added that kind of stuff. So, it's guessing the content type and all sorts of things.
**Tyler Yahn** 11:00 Yeah, wow.
**Nikola Grcevski** 11:04 You do what you gotta do, right?
**Tyler Yahn** 11:08 Yeah, exactly.
Well, yeah, cool. I look forward to seeing the POC, that's exciting. Always exciting to help support a talk as well, so, yeah.
Yeah. Looks great.
Okay, cool.
Moving on, it looks like I'm up next. So, one of the things we talked about last time was this decision on, unification of HTTP routing policies in the configuration.
So, this is something that, from, like, a global level down to, like, a specific service level, there was, like, an incompatibility, mainly around, like, ignore rules and unmatched rules, and then also on the egress versus ingress, like, the global didn't have the egress ingress.
The local didn't have the unmatched, in the, Yeah, so this is essentially trying to unify that based on the decision. yeah, so we have… I mean, that's the goal, at least, is to get that done.
There was some feedback, thanks Mario, for taking a look at it, about cleaning this up. I do think that there's opportunity to clean this up, definitely, but I think it's in the V1 stuff that it would be cleaned up, and how that would actually, simplify things. I'm a little hesitant to do that in this PR. I'm also a little hesitant to do it if we're gonna just throw away the V1, configuration stuff. Well, not throw away, get rid of it eventually, So, I, I asked Mario if I could just maybe put that as, like, a follow-up action item. I'll, you know, create an issue for it. But otherwise, yeah, I think that this is ready for review, is kind of where it's at.
**Nikola Grcevski** 12:48 No, sounds good. How are you there?
**Tyler Yahn** 12:50 Cool.
Okay, cool. Moving on. Next up, address context to plain text logs.
Yeah, so this is definitely something that other folks have talked about for a long time. I finally got pushed into doing this, which is exciting. I think I'm super excited about the future, it just…
**Nikola Grcevski** 13:13 Super excited about this as well.
**Tyler Yahn** 13:15 Yeah, yeah. It just, yeah, so I'm pretty, pretty pumped about it. It sounds like, Mattia, I did get an approval from you, but I did want to talk through this enable by default, question that you had here, and just make sure that we're comfortable with it. I'm a big fan of trying to make sure that we keep this on by default.
I understand there's concern, and it's valid concern, that, like, it could definitely mess things up if this thing goes out, but I think in the long haul, it's for the better. But I just wanted to, like, touch base Synchronously, and see, what yours and other folks' thoughts on this are.
**Mattia** 13:48 Yeah, from my point of view, I mean, we don't have metrics on a global scale, so we don't know how many people are using this feature, how many services are instrumented with this login reacher.
So we can't really say it's, it's very risky, or it's not risky, or whatever. We should just, make sure we… we put a big, red, text in the next changelog, so people can, Can notice that, that something is gonna change.
Yeah, yeah, that's… But I agree with you, config-wise, if we enable Login Richard, the better thing to do is to enable it for… for all formats.
**Tyler Yahn** 14:34 Yeah, okay.
Okay, alright, if that's the case, I'm gonna resolve this and, make sure to include the big warning message, in the changelog. But otherwise, I think this looks ready to merge. I don't know if there's other folks… That are looking to…
**Nikola Grcevski** 14:53 Go for it.
**Tyler Yahn** 14:55 Yeah, sweet.
Yeah, I'm really excited about this. And I guess for those that haven't taken a look, it also, just a heads up, like, adds the ability to start, configuring the keys that…
**Nikola Grcevski** 15:08 True.
**Tyler Yahn** 15:08 this shows up under, which is also super exciting, because, I think different platforms require different keys, so, like, that was also a big, big win for us.
**Nikola Grcevski** 15:18 I agree.
Cool. It's big pain for the community as well. I think this requires a blog post, honestly.
**Tyler Yahn** 15:25 Yeah, like.
**Nikola Grcevski** 15:26 Like, showing.
**Tyler Yahn** 15:26 I'm actually kind of surprised how many people that I talk to Obi-on, and they're just like, yeah, that trace log core correlation stuff is pretty amazing, and I'm like, really? You're using that? It's like, no, I didn't even realize it was going on, and it just happened for me, and I was like, that's cool, like, that's really awesome, so… Yeah. And of course, then that was immediately followed up with, why isn't just working for plain tax laws?
So, agreed, yeah, let's maybe get a blog post on this one, during the next release, yeah.
**Nikola Grcevski** 15:54 You guys had a talk proposed for KubeCon, right?
Somebody did.
**Mattia** 15:59 It's gonna… so the result is gonna come up, like, in a week, on the 1st of August, I think.
**Nikola Grcevski** 16:05 So let's wait for that then, so I don't spoil it too much.
**Tyler Yahn** 16:10 The, the blog post?
**Nikola Grcevski** 16:12 No, I mean, the KubeCon… proposal. Especially if he goes in, it's nice to have, like, a full-on.
**Tyler Yahn** 16:20 Yeah, yeah.
Well, I mean, if that's the case, Mattia, did you want to try to get the blog, together for this next release? For this, Turkish context stuff in logs, in general?
**Mattia** 16:34 Sure, I think I can do that.
**Tyler Yahn** 16:37 Okay. Yeah. I mean, I always… If I'm gonna give a talk, it's really nice to write the blog post beforehand, because it's, like, kind of like a pseudo-version of the talk that you're eventually gonna give, but, yeah.
It's up to you.
**Mattia** 16:50 Actually, yesterday, I tested your branch on a demo environment with the OpenTelemetry demo. There were some services which were not, outputting, rich logs, like the .NET one, I think, but that's because I think the trace context is missing,
**Nikola Grcevski** 17:10 Period.
**Mattia** 17:10 It's missing there.
But yeah, I can, I can put some… something up. When's the next release?
**Tyler Yahn** 17:19 I think it's, like, I had it August 11th, is what I had said. There's definitely a few more PRs, we want to try to get in.
**Mattia** 17:28 Yeah, okay, we have coming down.
**Tyler Yahn** 17:30 Yeah, I think, I think he got a few weeks, I guess it's the 22nd, so…
**Mattia** 17:37 Yep.
**Tyler Yahn** 17:37 Yeah, got a lot to do, actually, still. So, yeah, it's, August 18th is when I had the due date, so… But yeah, okay, we'll keep that in mind.
It's a great idea.
Okay, and then last, PR for me as well was this Plum the Go Auto, SDK span payloads. So this is, another step towards the full auto SDK, support for, the Go SDK, integration with manual spans. Right now, just if you, like, for context, like, we do support, like, manual spans, but in a very limited capacity. This is, like, the thing that we're migrating over from the, Go Auto package. Essentially, there's a full suite that we can actually hook into, that decodes JSON from, like, the global, API.
If nothing has already been registered. So, this is essentially, like, the hook-in. This doesn't actually run any of the probes, that would be needed here, so this is trying to, like, scope this to be something that's reasonable.
But it's more just, like, setting up the probes, and getting it ready for, like.
actually turning them on. The actually turning them on part is going to be, like, the, you know, we want to make sure that's the behavioral side of things, where… We don't turn this on if, like, you know, aBPF probe write user is not enabled, because we need to be able to, no, actually, we can still do that. We can turn this on, and get data. We can't write trace context back to the auto SDK, and… Oh, I'll… actually, no, I take that back. We do need to write a little switch into the bpfroad rep user, to turn on the… yeah, which…
**Nikola Grcevski** 19:21 a tracer.
**Tyler Yahn** 19:22 Yeah.
We talked about maybe looking at a few different ways on that one, because it's, like, literally just, like, a one-time thing, but Anyways, that's the next PR.
It can just be off by default if somebody's not running with admin as well. Like, that's also totally valid.
**Nikola Grcevski** 19:37 That's true. Yeah.
**Tyler Yahn** 19:39 But yeah, this is all the probes that will be hooked in. There's the POC as well, that you can take a look at.
that I thought I linked, yeah, I thought I linked here, yeah, and it shows a little bit more clear, like, the full setup. The linking there is also not fully feature… Fleshed out, it's still a POC, but, like, yeah, this is, I think, just ready for review, yeah.
Cool.
Alright, with that, that's the end of my topics. Looks like, Nikola, you wanted… I'm sorry, Rafael, you wanted to mention this is going to be your last CG meeting for a while?
**Rafael Roquetto** 20:14 Yeah, that's, until I figure out what's coming next, so I won't be around for the next weeks, at least.
**Tyler Yahn** 20:22 Okay, yeah, sorry to hear that, but, also, exciting, exciting future, right?
**Rafael Roquetto** 20:28 Cool.
Thanks.
**Tyler Yahn** 20:32 Okay, and then Nikola, you wanted to mention the joint blog post, proposal for OTEL, C and the OB.
**Nikola Grcevski** 20:39 Yeah, I mean, there's a proposal going on, I just wanted to let everybody know.
yeah, the folks from the, Go compile time Instrumentation are looking to kind of build up, Zero-code, sort of, blog post that demonstrates when and where you use one or the other.
Yeah, just wanted to bring it up to a residential, because something I… I got involved with.
**Tyler Yahn** 21:08 Yeah. Awesome. I'm… I'm excited about this.
If folks didn't also see, I think that the compile time Instrumentation just went stable, like at 1.0. So, I think, with that, and with Obi, going stable, which we're going to do, by Krypton, Then, I think, like, yeah, this next KubeCon, is definitely gonna have a lot of, like, excitement around the zero code, given that it's the maturity in OTEL. So, yeah, I think these kinds of blog posts and splashes are gonna be really great.
Absolutely.
So, yeah, all the maintainers, please do take a look at this, and Yeah, let's try to collaborate on this one.
**Nikola Grcevski** 21:48 Yep.
**Tyler Yahn** 21:51 Okay, cool. There's no cry fixing it.
**Nikola Grcevski** 21:57 Yeah.
**Tyler Yahn** 21:59 Awesome.
Well, okay, any other, topics from folks?
That's the end of the agenda that we've written, gotten to.
**Nikola Grcevski** 22:12 I'm away next week, so I won't be on the next sick call.
**Tyler Yahn** 22:17 Oh, cool. Is that the conference next week?
**Nikola Grcevski** 22:18 Vacation, and then I'm going to the conference, but, come back, and then I'm going to the conference. It's like Faust, I mean, it happens on a weekend.
**Tyler Yahn** 22:26 Oh, okay.
**Nikola Grcevski** 22:27 Yeah.
**Tyler Yahn** 22:28 Yeah, yeah.
Well, cool. Awesome. Well, have a good time on the vacation, for sure.
**Nikola Grcevski** 22:33 Hang here.
**Nimrod Avni** 22:39 I wanna update, I… continuing to, write and improve some of our Weaver validation stuff, and I went over to the WeaverSIG meeting, and I brought up some issues that we encountered, and they were kind of really helpful with both.
like, the… we… I've opened some issues for them, that, mainly around the parts that were manually ignoring some advisories in GoCode, and that they want to make it more, like, declarative. And also some… some stuff regarding metric… an attribute, like, refinement and expansion that we are doing, like, for example, changing a requirement level, or adding more enums, and stuff like that. And I've also opened a semantic convention issue.
for the DNS, metrics, to, like, remove the question name to opt-in, because for, like, for us, producing it, it makes sense, maybe, like, as a metric up there makes, more sense as well.
And, yeah, I just want to keep, like, just wanna update that I'm continuing doing stuff there, and… I see, I think it, like, also catches some issues, like the thing yesterday with… removing, like, sending empty HTTP methods and other stuff, I think it, like, kind of helps us, so that's… that's really cool.
**Nikola Grcevski** 24:10 Yeah, that's a… that's a real bug. It's like, I didn't realize it.
**Nimrod Avni** 24:15 Also, the internal metric stuff, the, like, exporter basically, like, you never catch exporter failures.
And stuff like that. I don't know.
**Nikola Grcevski** 24:25 I have to look into that, why the Java sometimes sends a Java agent, something sends empty methods. Something's wrong with, Some part… yeah.
Nope.
We'll have to look into it.
I wasn't able to reproduce it, I tried.
It helps the CEI, but not for me, locally. I have to try harder.
**Nimrod Avni** 24:52 Yeah, maybe with the… maybe from the CI, you can get some, debug.
**Nikola Grcevski** 24:56 Yeah, yeah.
Yeah, to look into.
**Tyler Yahn** 25:04 Yeah, cool. Thanks for the update on that. That's all really great, useful work, so I really appreciate it. Definitely the Weaver guys I've found to be pretty helpful in the past as well, so, yeah, that's awesome. They also, I think.
really love hearing from people who use it, so yeah, that's… I'm sure they're gonna be super excited about that.
**Nimrod Avni** 25:21 Yeah, I tried looking, like, around for other people who use it, and I saw the OTLC guys, like, copied a lot of our infra, I guess it's because of, yeah, like, we have some, like, shared contributors there, and I think also the Java auto-instrumentation uses Weaver for some…
**Tyler Yahn** 25:38 Oh, yeah.
**Nimrod Avni** 25:40 No.
**Tyler Yahn** 25:41 I feel like, more of people should use it for what you're… you're doing.
We've always wanted to do it, just never had the time in, like, the Go Instrumentation stuff, but yeah, like, it's… I think if you're writing Instrumentation and you don't use validation through Weaver, like, it's kind of, like, I don't know, there's, like, a huge integration path you're missing at that point, yeah.
**Nimrod Avni** 26:05 No. Yep.
**Tyler Yahn** 26:08 Well, cool. Any other updates, cool things people are working on?
Topics.
If not, We can end the meeting here. Yeah, thanks everyone for joining. It's good seeing y'all. I will, see y'all in a week's time, or asynchronously. Until then.
**Nikola Grcevski** 26:27 Bye.
**Mario Macias** 26:29 Bye, bye.
