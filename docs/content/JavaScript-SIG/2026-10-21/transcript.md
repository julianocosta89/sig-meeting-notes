SIG: JavaScript SIG
Date: 2026-10-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler** 01:14 Hello?
Or you're in a different, different place today.
**Marylia Gutierrez** 01:30 Yeah, that is what I have been for the past couple of weeks.
Yeah, I had a surgery, so I'm pretty much in recovery. So this is why I'm, like, I'm lying down, because I didn't get the.
**Marc Pichler** 01:46 Go ahead.
**Marylia Gutierrez** 01:47 to sit normally yet, so it's still pretty weird, because I can only go to, like, 45, and I was like, I know, I know that, like, I go to the meeting, I went back to work this week, and I have, like, all these pillows near me. I was like, it looks like I'm in bed, like, sleeping, and I just woke up for the meeting. I was like, no, trust me, I'm working, but it just… looks, because I didn't get the clear to set.
**Marc Pichler** 02:12 Oh, no Well, I hope it's, hope recovery, goes quickly for you.
**Marylia Gutierrez** 02:19 Thank you.
**Marc Pichler** 03:00 One second, I'm still looking for the correct browser window to share. I'm, like, furiously closing all of the… other ones.
It looks like it's the right one.
Alright.
Welcome, everybody.
Let's get started with the topics here, I'm not sure if… Shengshuang will join today.
Or not, but he… Put this issue here as a topic to discuss.
Node.js is, adding, like, a small hotel-like thing to their, like, two node shares itself. And they're looking for collaborators.
This is one of the, offshoots of… the previous proposed PRs that would add it directly to Node.js, and apparently it's gonna be in this, separate repo, if I understand correctly.
Yeah, I think, yeah, I'm not sure I have a lot to say about this.
Right now, I just encourage everybody to head on over and see what the plan there is.
Oh, weird.
**Trent Mick** 04:42 looks like they're gonna do it like they do for Ndichi and… Amaro is another one, but So, development goes there, but periodically it gets… Basically, a tarball gets… or a bundle gets built into Node, so it gets… Loaded internally.
Yeah, yeah, yes, another SDK. It's, I mean, RTML, it's kind of cool. It's… Without anything you can get.
OTLP output for HTTP, in Node.
And right now, there's no… there's no… There's nothing other than turn it on.
I guess a follow-up question, if people are keen and want to be involved.
Is whether that can expose… API, so that there can be instrumentations, or one can… or whether one could hook into… Those instrumentations and have, like, a mix.
of external instrumentations and this built-in SDK working together.
Right now it's not configurable at all, so, like, you can't do sampling, or control sampling, any… any of those kind of things, but… Anyway… Yeah.
Certainly something to be aware of if it's released, and then… Users come asking about, well, this isn't working for me, that kind of thing. Well, are you trying to use both? Because it'll override.
The… the trace… parent trace state headers, if it's turned on.
**Marc Pichler** 06:16 Yeah, we'll, probably at least have to… add something to the park report template in the future, to make sure.
**Trent Mick** 06:26 Hmm.
**Marc Pichler** 06:28 We… we know where issues are supposed to go.
But, yeah.
I guess if there's no comments or other thoughts yet, We can move on to the next topic.
Maybe if, agenticus translator, we… Can pick up discussion on this again.
Moving on to the next topic, Marylia.
**Marylia Gutierrez** 07:10 Yeah, so I just put it there in case people miss. We… the GC election is happening next week. We do have the final list of candidates. It is official, the list now. The election is happening next week, from the 26th to the 20… 9?
Okay, it's gonna open here, and then I say… no, 28, because he has 29, like, because it's anywhere on Earth, so that goes up to, like, later, like, 29.
But yeah, and then the results will come out on the 30. So, don't forget to vote, it's next week. I'm gonna send reminders again on Slack and things like that, but just a chance for you to look at the candidates beforehand.
**Trent Mick** 07:54 This is refilling 4 of 9 seats, is that right?
**Marylia Gutierrez** 07:58 Yeah, correct.
**Marc Pichler** 08:04 Yeah, thanks for… Bringing it up, I think.
**Trent Mick** 08:12 Longer terms? Are they… are they 2 years?
Absolutely.
**Marylia Gutierrez** 08:16 Yeah, it's 2-year terms, always.
So this one, the term from, Trask, Pablo, Morgan, and Alolita is ending in October, so there… that is the… the four seats that will be up for… Yeah, this election.
**Marc Pichler** 08:40 Right, thanks for bringing that up.
I guess everybody here is familiar with the GC election, process anyway.
make sure you can log in so that you don't end up in the same situation as me last time around, where I tried to log in and had to jump through a bunch of hoops to get my boat in, so, yeah.
**Marylia Gutierrez** 09:06 Yeah, if you don't know how it works, or you have questions, feel free to ping me. I'm always happy to… to explain.
**Marc Pichler** 09:14 We're still using the Helios voting thing, right? Yeah, there's a button that says Cast Vote. You have to, click that.
**Marylia Gutierrez** 09:22 Actually, yeah, actually.
**Marc Pichler** 09:26 That was, something that I did wrong the first time around, so… Just saying it so that everybody's aware.
right?
there's no questions around the GC election, and we can move on to the next topic. This is the announcement for SDK 3.0 and the new API version. The packages are live now. We released that yesterday, along with A new version of each of the contrib packages.
Some of the highlights are stable logs, API and SDK, the valid ESM output that we now have in the packages.
And… The widened attributes type that's now spec compliant as well.
And, we consolidated the SDK trace packages into one, so that there's not multiple ones anymore. A huge thank you to everyone who contributed.
Yeah, thanks for working on that. It's good to have that.
Hefted out.
And… yep.
**Trent Mick** 10:46 And Mark, for others, by the way, Marc was up until almost midnight, his midnight last night driving us, so thanks.
**Jackson Weber** 10:53 Yeah, thank you, Marc.
**Marc Pichler** 10:57 Yeah, thank you, everyone who worked on that.
Right.
Moving on to… first, is there any question around… Read it all.
**Jared Freeze (Palo Alto Networks)** 11:13 I was just gonna mention, so thanks for the dock migration. There was… There… there were a lot more breaking changes that it found.
for authors?
So I think this is a good summary, but I wasn't sure if it was overkill, so… I appreciate the merge, but it seemed like, you know, Claude wanted to add.
the little explosion to, like, every line. It's like there's something breaking in all of these things, so if it went a little too far, I mean, I think it was nice that it's accurate, but if it went a little too far, we can… Yank that back a little bit, if you want, so…
**Trent Mick** 11:52 No, I think your update was good. I had planned… I still hadn't made a first pass through the whole thing, and I'm not surprised that there's some missing stuff. So no, that's definitely good. I think… Yeah, it looks big to people, so I guess… I don't know, can ask questions… answer questions for people, and… or maybe… like, there's a… the Slack post that I did, I wanted to point out, like, some people won't need to adjust at all, right? If they're using Auto Instrumentation's node, then… Basically, nothing broke there, so at least that's… That's good. It's gotta be… I'm sure it's daunting, but I'm not sure how to fix that. It's gotta be daunting for some people coming that are just kind of casually using.
OpenTelemaryLink, oh my god. There's a 7-page document on breaking changes, but I'm not sure how to deal with that, so… No, I think it's better to have them all mentioned in there.
**Jamie Danielson** 12:40 I would rather have the extra detail, because again, I think most people, similarly to how it was probably written, right, most people are still going to feed it to their local agent, or whatever, and say.
does this concern me? Do I care? One question I have is, last year we did a blog post on SDK 2.0.
do we want to do one for 3.02? It more or less contained, like, the same stuff from the release notes, if I remember correctly, just kind of, like, more… Coverage, maybe?
**Trent Mick** 13:15 Yeah, I think that's a good idea.
I'm happy to… Try that. Anyone else wanna… I'm happy if someone else wants to tag team on that, too.
**Marylia Gutierrez** 13:26 Yeah, I can help, because then I can be your sponsor, because you're gonna need a sponsor to do this.
**Trent Mick** 13:31 Okay.
Great.
**Jamie Danielson** 13:33 I think that's a good idea. And you can probably do a similar thing on that, like what you had, Trent, of the highlights, a few bullet points, so it's kind of like, yeah, here's the TLDR for the people who don't want all the stuff, and then here's a bunch more. I mean, I guess there was also a limit to how much we want to write in the post compared to how much we want to point to the repo document.
But, obviously, you know, use judgment. I think the biggest thing is just making sure people see it.
**Marc Pichler** 14:11 I think also blog post sounds, sounds like a good idea.
Probably also… I'm not sure if we want to have a separate blog post for the log stabilization announcement.
I've seen… some other SIGs or so announced it separately, so I think it would be worth… Corning that out as well.
**Marylia Gutierrez** 14:41 And we are doing… giving, like, priority for, like.
blogs made by, like, maintainers with, like, major milestones. Those are the ones we are approving, like, usually earlier and stuff like that.
So yeah, it'll be good to create those things, because yeah, those are the important things.
**Marc Pichler** 15:05 Right?
There's no more.
Things to talk about for 3.0, I guess we could also move on to the next topic.
**Marylia Gutierrez** 15:18 The next one I put it there is not related to, like, our SDK, like, at all, but might be affecting your own personal development.
Sorry, I just put it here in case people missed.
**Marc Pichler** 15:31 Yeah, this is blocked, I cannot click this, for me.
But you can probably have a look for yourself as well. It's the certificate thing. I was also kind of busy all day today because of that.
fun.
**Trent Mick** 15:55 You… Sorry, you can't even click the thing that tells you about… worry about.
**Marc Pichler** 16:00 Huh?
**Trent Mick** 16:01 It's… that's kind of ironic.
**Marc Pichler** 16:04 And try… oh, no, now it works again. I had tried to… Click it earlier, and it was… filtered, somehow.
**Trent Mick** 16:19 So, has the world ended? Like, I helped with the release, and then I went to a… concert last night, I haven't been watching the world.
Get a guest on. Everyone's here, so…
**Marylia Gutierrez** 16:30 Yeah, I like the… like, there's a kind of like a meme saying, like, how, like, millennials react when people tell, like, oh, the word is ending. Okay, cool. Whatever. Continue doing, like, whatever you're doing, just like… cool. Anyway…
**Trent Mick** 16:47 Unbelievable.
Then I have to educate on what my… or educate myself on what my generation is supposed to do to react. I'm not sure how to react properly.
**Jackson Weber** 16:55 I like to think that even if the world was ending, we'd all still show up to the JS SIG. It's just that important.
**Marc Pichler** 17:11 And,
**Trent Mick** 17:14 Okay, so I think I'm behind on this one. There's a… there's a PR, and I think the author is here in the call, but I think, Marylia, you closed the PR already? I see.
**Marylia Gutierrez** 17:25 Yeah.
Well, the owner closed it because, after the other PR got merged, Would that change?
**Trent Mick** 17:33 Oh, is it at… okay, was it out? Yeah, okay. So,
**Marylia Gutierrez** 17:36 there was, like, two changes here. One of them recommended his own tool, and then the other, some changes on the migration, but when the other PR got merged, all of those other stuff got fixed already, so the only thing from this PR was this line, which I don't think we should be doing, so I commented there, so they closed the PR.
**Trent Mick** 17:56 Yeah, I was coming to discuss the same thing. I agree with that. I think we get in a difficult security position if we're recommending people use other third-party tools. So, Aditya, I noticed you're on the call, I hope I pronounced your name right there.
Cool if there's tooling out there, but, unless it's something that's merged and gone through our, like, regular review process and something that is in our repos, we probably can't recommend, like, A here, people go to this site and download and run… run some script. That puts us.
**Aditya Reddy** 18:30 Yeah, I just joined this because I think it was 7. He said, like, if it really helps people, maybe you should join the JSIG and…
**Trent Mick** 18:41 Talk about it, yeah.
**Aditya Reddy** 18:42 Talk about it, like, propose it, that… it'll be part of hotel tools, not your tool? Like, I was like, yeah, I'll just put it there, see what they think.
**Trent Mick** 18:53 Yeah, okay, I mean, we don't have any history in providing migration tooling. I think, like, in general, sure, it sounds like a great idea. If… if a reasonable job can be done, there's a balance there between maintenance or having something that is as meaningfully useful.
Yeah, if it's something that you think that fits that build, then maybe you could submit it as a… an issue for discussion on how we do it, or a PR, like, here's an idea of something that we could do, and then we could review and make a decision on that. Sorry, Marylia, I spoke over you.
**Marylia Gutierrez** 19:25 No, yeah, because I was gonna say, like, Severin's point is more, like, not necessarily, like.
put your tool here and tell us to use is, like, your tool should exist in Hotel if you think that is a good tool, because then it's under the hotel umbrella. But then at the same time, we need to make sure we have people to maintain this, Because just pointing to something is actually something that we are stopping doing, even, like, we are… we froze in, like, registry, for example. That is one of the reasons, because we cannot, like, validate the things that we are telling people to, like, go and click here, but we don't have the bandwidth to actually validate.
And even if it is valid now, nothing's stopping from somebody going and changing completely the tool. So that is why we are not pointing to other tools as well.
**Jamie Danielson** 20:14 it could still be something that's worth, you know, you can still post it in, like, CNCF or something like that, of, hey, this was sort of useful for… Slack, CNCF Slack, of, hey, I found this useful, if you do too, feel free to use it.
you know, for folks to see, but yeah, I think the main thing is, if we are specifically recommending it, we will have to maintain it and review it and all of that, so… Yeah. Yeah.
**Aditya Reddy** 20:42 I understand, yeah, that was the pitch, was like, yeah, it can be part of Hotel, and I will be responsible for maintaining it, but I understand it.
what if I'm not available, or some… so, yeah.
**Trent Mick** 20:57 I mean, I'm curious, and I'll probably take a look. I… for… for the JS SDK2 release, I had a tool that I built for helping do migrations and pointing out, like, here are all the places you need to edit and do. It didn't… But I was considering upstreaming it, but I just gave up, because it's… this is a hard maintenance problem, is like, I can't promise that I can upgrade any codebase to do the right thing, it's… yeah.
I suppose one could build a skill these days and just kind of pray.
But don'.
**Jamie Danielson** 21:28 Yeah.
**Trent Mick** 21:29 Do the right thing for people, but it might…
**Marylia Gutierrez** 21:34 Again, the word is the ending, so…
**Jamie Danielson** 21:37 Nothing matters.
**Marylia Gutierrez** 21:39 matter, just if the italic upgrade doesn't work, like, okay then, move on.
**Jamie Danielson** 21:45 Next.
**Marc Pichler** 21:50 I did find it a really cool idea, the migration.
being, heavy. I think some other projects, provide that.
And… I've had mixed experiences with, using them in my own codebase. Sometimes it worked, sometimes it didn't.
but, yeah, I think the idea itself is really cool.
And… yeah, I'm still hoping that, some people use it and, hopefully find, Find that it works well for them.
But when I first saw it, I was also, concerned about the security implications of it.
So… Still, thank you for working on this. I think it's very valuable.
**Aditya Reddy** 22:43 Cool.
**Trent Mick** 22:54 Maybe not today, but at some point now, we should talk about what Or… priorities for the group are. We have the… the issue that Mark started way back, even when we were doing 2.0, to try to get some focus in there, I imagine we'll be picking off one or two of the things that are there.
Stabilizing exporters, I'm sure, is there, and something something instrumentations, ESM.
**Marc Pichler** 23:21 I will update the issue, to remove the stuff that is done, or at least move it.
Down here into completed topics.
We had this upcoming thing, which was… filter PX Sporters.
Didn't I update this to also include declarative config? No, it's in the backlog down here. That's probably also a big one to look into.
And then also instrumentation stability.
Back to the instrumentation-based package.
I see you're laughing.
**Trent Mick** 24:05 to the back 40. Oh, wow.
Jared probably has feelings too, but yeah, instrumentation base is a problem.
**Marc Pichler** 24:12 Yeah, it… I think, ins… like, sorting out… the situation with OpenTelemetry instrumentation will… reduce some of the maintenance burden that we have across all three repos, actually, or all three repos, including browser. So, there's… a lot of… Upside that can be had from stabilizing the instrumentation package.
Also with, like, third-party instrumentations that live in other repos.
Having a stable one might, Help the ecosystem quite a bit.
**Jared Freeze (Palo Alto Networks)** 24:58 That's our next major project, is figuring out I mean, what I'd like to recommend is that nobody use Instrumentation Base from Core. Well, only because OTEL Browser Is almost at a point where it has no dependencies.
Like, for interfaces, I should say.
And so, the PR I have out now that David reviewed and everyone's looked at, got massively simplified, so we're actually gonna have like, it's just much smaller, you know, for us, and we also have a commitment to never unpatch, because multiple vendors will take over certain parts of the system. Less of a problem, I think, for backends. But, because of those two things.
**Trent Mick** 25:44 You know, it's a problem for back hence, too.
**Jared Freeze (Palo Alto Networks)** 25:46 Oh, is it? Okay, yeah.
**Trent Mick** 25:47 Not because multiple, it's just because the whole idea is in sync.
But, yeah.
With import in the middle and other things, it's just, it's, yeah, it's unnecessary.
**Jared Freeze (Palo Alto Networks)** 25:59 Did I tell you right?
**Trent Mick** 25:59 But anyway, sorry, I spoke over it.
**Jared Freeze (Palo Alto Networks)** 26:01 No, no, no, I went to the W3C meeting and was like, hey, you know, we do this crazy monkey patch thing, like… it'd be cool if we had a real way to do it, and they're like, it's never going away, just keep doing it. Like, we can't… we could never undo it. It's the basis of the web, is people overriding defaults, you know, within the browser, internals. I was like, alright, fair enough. I mean, we already do it, so… But, but yeah, no, I think, having that… It creates a lot of issues, though, because if we do have a new instrumentation base, anything that's third-party that's relying on this.
I don't know exactly what happens when you import both.
Into the same project.
or what it looks like, or, you know, how the dependencies work. So that's… we have a ticket out now, which actually David just commented on, that I took ownership of, just to do research, just to find out. I'm just gonna grab stuff from all the vendors and see if… what instrumentation… browser instrumentation's out there, and just jam them all together in one massive SDK End-to-end tests and just see what happens.
So, if there's a mix of OpenTelemetry slash instrumentation, I'll have an answer for you pretty quick. And then hopefully we can take whatever that end-to-end test is and sort of port it back to Otel.js.
Okay.
**Trent Mick** 27:17 Every time I've… I mean, I don't even know if I want to start discussing it, because it's a big topic, but, every time I've… looked at it, I've wanted to… get to an instrumentation interface rather than a base class. I hate the base classes adding, kind of, default implementation details that we really don't need. It's probably getting into areas that we shouldn't, so, like, the setConfig, get config is confusing the enabled Disabled state is not really clear, and it's mixing… there's an isEnabled function, and the enabled flag gets merged in with the config, and it's all just kind of a… kind of a mess there.
Bye.
I was hoping that we could… Back off to just have the… some order of operations with SK getting set up, and when the instrumentation's… just having, like, a promise of what the… I guess it's the interface, is what the interface for an instrumentation is, and what can I expect to get called, and what does it have to do, and at what time. So, like, right now, the… the mess of… whether you're enabled or not, and when that happens at construction time, and construction time's too early in the back end, I don't know if things are different for the web, but you talked about I don't know. Anyway, reviewing your thing, some of the… that's helped clarify some of the usages, so, like, you said that enable-disabled state is used for GDPR compliance. I was like, oh god, that's… That's a use case I didn't think of in the back end, but… yeah.
**Jared Freeze (Palo Alto Networks)** 28:53 Yeah, the problem for us was, like, what… I don't know that EU laws, I actually need to look it up, but, like, can we hijack everything and then not export? Like, is that good enough? Or is it, like, don't do any work? Or is it you can set everything up and you can even export as long as it doesn't actually go on the network?
So those things determine, kind of, how much work we do before, you know, enable, like, what is construction, what is enable, because those things are not super obvious once you get into patching.
Because if you, like, XHR is a good example, you have to patch two things. So, am I enabled if I get halfway there?
Right? So, you're right, the implementation cannot be in the base class. Like, we need to just have the interface, because that is up to every author.
So, just saying, you know, I'm enabled Complex on its own.
**Trent Mick** 29:44 Yep.
**Jared Freeze (Palo Alto Networks)** 29:44 Anyways, that's how it's designed now, so I can send that over, too. I mean, you guys aren't, approvers of anything in our repo, but I can post a link so you can take a peek at what we're thinking.
**Trent Mick** 29:54 I've seen the PR, I looked at the complex one, so I'm happy to hear that it got… simplified a little bit, because you're trying to deal with any kind of instrumentation out there, and any weird path, and… is… is handled by the state machine doing things, but yeah, I don't know if we can…
**Jared Freeze (Palo Alto Networks)** 30:09 We had 14 cases for what people might want, and so that was the wrong place to start. It was a good place to start, it was the wrong place to stay.
So…
**Trent Mick** 30:27 Yeah. Every time I started in there, I've always ended up with an instrumentation 2.
interface, like another one, and it just kind of… I don't know how much of a migration pain… we're in, but I don't know if that's better, like, we start with a simple, or… Instrumentation interface, and we find a way that the SDK, at least on the node side, or maybe both browser and node SDK, can deal with both types of instrumentations coming in, so third-party ones that are using the old.
Class set, and then do a long, over a year or two-year migration process where all instrumentation's out in the in the world, I've moved over to this new, simpler thing, and then… I don't know if life's better after that or what, but…
**Marc Pichler** 31:14 I think at least simplifying the instrumentation interface, and just having that instead of the base class is already Quite an improvement.
**Trent Mick** 31:27 If we can get there again.
**Marc Pichler** 31:29 Yeah. Many of the things that are now in the instrumentation base can just be utilities that people can use if it's necessary to have that be shared code anyway.
So… they don't have to be part of the base class. I think that that's just how it grew, over time, and then we got stuck at some point when we crossed over a specific number of instrumentations in Contrip. So… I just realized that this is actually also done. So thank you, Jared, for working on that.
**Trent Mick** 32:16 Yeah, no kidding.
**Marc Pichler** 32:17 balance.
**Trent Mick** 32:17 Cool.
**Marc Pichler** 32:24 So, I'll update the issue here. Maybe we can discuss next week, what to prioritize next.
Is there anything… It's… Any of you would like to see that is not in this list right now?
I guess there's no need to answer right now, but if you have a look later at this issue, and you find something that isn't in there that you think should be in there, please feel free to just write in one of the Other.js channels in Slack, and I see to have that added there, or just open an issue, and let us know in the next SIG meeting.
And eventually we can…
**Jared Freeze (Palo Alto Networks)** 33:22 Yeah, I do have a question. What's the last item? Can you just give an overview real quick?
**Marc Pichler** 33:28 Yeah, so, one of the main issues that we're having right now is that everything kind of lands in contrib.
And the reason why everything lands in Contrib is because we have no way of dynamically loading, plugins from elsewhere. So that would be exporters or, Thank you.
Instrumentations, for example.
The idea here is that it would be nice to, just… say, these are the packages that I want to load, and it just loads them dynamically without you having to build, like, a metaph package.
What we have now with auto-instrumentations node.
Where everybody wants to get their stuff in. This way, people could Maintain the instrumentations in separate repos.
One of the prerequisites for that would be stable instrumentation package, or, like, some sort of interface.
And we would just load that instead. So there's a bit more flexibility where things are.
That's, like, kind of the gist of it.
instrumentations is the first thing that comes to mind, but it's really everything that's, like, an SDK plugin interface. So, span processors, for example, or metric readers.
export us, samplers.
Anything that you could think of, basically.
**Trent Mick** 34:58 I sent a link in chat. I had a… I had a run at a design idea for this, because it… it… Yeah, there was the… before declarative config existed, and the idea there was… mostly we were talking about instrumentations, and how, like, to get something for users, we always run into this problem, is people wanting contrib, because they wanted an auto-instrumentations node, because that's the only way that it's really exposed as a… as an easy way to instrument things.
With declarative config, they added this concept of a plugin component provider, so that with stock declarative config, and if we would do… I think we're close to a first release where we have declarative config support, but that's only with the built-in classes. So, for example, Spanic… span process is just the batch span processor or the simple span processor, those are the only ones that are supported. The declarative config allows you to define additional ones.
a name other than batch or simple for span processor, for example. But how to resolve that name in a YAML config file to an implementation is… something that the SDK code has to have loaded, some extension from a user, or something that defines that thing. As far as I know, Java is the only language in OTEL that supports this. They have Java extensions.
And in Java, life is a little bit easier, because Java, the platform, has this thing called Service Provider Interface, so that you can just load a jar, and it makes available implementation classes for a particular interface. So they define this interface of what a span processor is, and you can define JARS that define these other ones, and then it… it says, here it is with a name, and then that name gets mapped to declarative config, and they can… they can hook that stuff up. So, for us to do something similar, there's a proposal for something. The main problem that you're gonna run into first is for… Us to dynamically load stuff.
we need… basically, SDKs start to be async.
Because we have to go dynamically.
we have to read a file and then go dynamically load some things. There's… maybe you can get away from it if we only ever support, at least this is for backend stuff, using top-level await, and have it be in a, like, node dash dash import, my bootstrap script, whatever, and that… that thing can have top-level async await.
To solve some of those problems. Anyway, yeah.
It's a big… big-ish topic, but I think it's fairly important, or it'd be quite useful if we got there and had something.
**Marc Pichler** 37:53 Right?
Any other questions?
If not, then I guess we can proceed, async on, selecting the topics, and… Yeah, if anything comes up, please feel free to let me know.
Looks like we don't have any topics anymore.
To discuss?
Does anybody have anything you would like to bring up?
**Jared Freeze (Palo Alto Networks)** 38:33 What happens next for 3.1?
Like, I assume… Not everything is perfect, so… I mean, is it just gonna be regular issues, or are we just keeping an eye on… Things that apply to 3.0 specifically, and then try to… Quickly do another release, or… Yeah.
**Marc Pichler** 38:56 Yeah, so… plan is, always to look out for park tickets, anything that comes up that was introduced through the 3.0 release, if we see something, we should fix it, as soon as possible.
And, there's quite a few bug atoms that are currently in progress anyway in contract. We have a bunch of instrumentations there. SDK-wise, I don't think there's anything… Anything major planned right now with SDK logs out, that was, like, the last SDK thing, that we had there.
The next thing that's coming up for Node.js is definitely a declarative config.
Which has a spec.
Already, so, and we also have, like, experimental, implementation of it.
I saw a request for the file exporters, the file OTLP exporters is also more of a Node.js thing, We also have… An issue still about, performance improvements?
So that's something we might want to look into. And going forward, I think bundle size is also something we could take another look at.
Our in-store size in general, across all, packages.
Because that's also something that was brought up very frequently, is that, like, we just ship too many, like.
We ship a lot of stuff that people might not necessarily want.
So, that might also be something to look into.
**Jackson Weber** 40:51 Yeah, if anyone's interested in the bundle size optimizations, definitely key me in on that. That's pretty important for us as well.
**Trent Mick** 41:00 Does the ESMing, the great ESMing, solve a lot of that? We can… One hopes, bundlers can tree shake A lot better now?
But I don't know.
**Jared Freeze (Palo Alto Networks)** 41:13 I don't successful.
Balls got added to a bunch of stuff, so they'll be better behaved, even though it was possible to do that before.
So my understanding is that the very smart bundlers were already doing this, and the kind of not modern ones were not.
So, I'm not sure, Jackson, what your stack is in your particular product, but… That'd be interesting to see. I think ours, you know, vendor-wise, we have a lot of instrumentation, but we're running at, like, 180K. I think half of that is OTEL.
So, I am obsessive about this as well, but, haven't found anything obvious besides side effects false. And also…
**Trent Mick** 41:52 What are you doing with 90K for the rest of your SDK? Sorry.
**Jared Freeze (Palo Alto Networks)** 41:56 Session management, thank you very much. Because we don't have that at all.
Yeah, pages and sessions, basically.
And Web Vitals is bigger than it should be.
another conversation.
But, no.
**Trent Mick** 42:13 An overview from those of you that have more experience there.
Here, for what the big… culprits are for bundle size would be interesting to me, because I don't… I wouldn't… I wouldn't know where to start right now, and presumably we should start from These are the components taking up a lot of the space in the bundle.
**Jared Freeze (Palo Alto Networks)** 42:34 Yeah, so the, tool I use, I'll just call… I'll post a link somewhere, but it's called Sonda, S-O-N-D-A. There may be a better tool, but you… it's a plugin for Vite, and all these other things, and it creates JSON. It also has a nice HTML interface that you can launch every time you run a build, and it will… you can, like, click around to see… All the source code.
you know, all the sizes of everything. I use that pretty frequently. We don't have anything automated with it yet. We do check file size of our CDN bundle.
as part of CI, but it's not actually, like, it doesn't dig in, it doesn't show, like, a list of components, but if you want to see what is in your bundle, that is the way to do it. So, yeah, we could plug that in. It's already in our repo, so I can port it over for the browser bundles.
I don't know what the output might be. We may want to just spit it out in CI, just to start.
like, parse the JSON and spit it out.
But it'll give you an idea. I do recommend the HTML and auto-launch.
For whatever product you've got, if it's supported. But, yeah, definitely VEET. That's what we use.
**Trent Mick** 43:46 Okay, thanks.
**Marc Pichler** 44:07 As if there's no more topics, we can have a quick look at, untriaged bugs.
Looks like there's nothing new in the core repo, and… in-contrip… We have one that already has a pull requests.
Probably still needs triaging, so… I'll have a look at that async after the call.
**Trent Mick** 44:45 22.0.0 being used there, it's not supported anymore.
I just solved it.
**Marc Pichler** 44:52 Sorry?
Sweet.
**Trent Mick** 44:54 I'm being self-deprecating and unhelpful.
Or collectively self-deprecating, I guess, but…
**Marc Pichler** 45:02 You mean, because of the…
**Trent Mick** 45:04 The node version used was under our now-supported ones. Upgrade closed as resolved.
I'm joking, by the way.
**Marc Pichler** 45:16 Right. I guess if there's no more topics, and thank you everybody for joining.
Have a nice week, and see you next week.
**Jared Freeze (Palo Alto Networks)** 45:26 Yep. Cool, thanks.
**Trent Mick** 45:28 Bye. Thanks.
**Marc Pichler** 45:30 Thank you, bye.
