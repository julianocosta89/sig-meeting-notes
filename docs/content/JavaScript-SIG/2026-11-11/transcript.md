SIG: JavaScript SIG
Date: 2026-11-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:46 Hello?
**Trent Mick** 00:52 Yo.
How you doing?
**Marc Pichler (Dynatrace)** 00:58 Brad, thank you, how are you?
**Trent Mick** 01:00 Alright.
On vacation, so maybe that's…
**Marc Pichler (Dynatrace)** 01:07 You're… you're joining the SIG meeting on vacation?
**Trent Mick** 01:12 I want to get my two agenda items out, I could… I guess I could just pull the ripcord right now, but anyway. Doesn't look like it's gonna be busy, I imagine some are at… Not many, but… is Jamie probably a… KupCon right now.
**Marc Pichler (Dynatrace)** 01:26 I think so, yeah.
Let's see if, anybody else joins.
It's 2 minutes past the hour.
Already, so… Maybe it's just us two.
Okay.
Right.
I guess, We can get started. Just to not keep you for too long, on the call anyway.
So… the first thing, everybody on the call is aware anyway, but in case somebody's watching the recording, new security advisories are… are out now. We fixed That on… Through the decks, and backported the fixed tool.
Gulodex, so… any of the supported version ranges, or any of the supported versions have the fix. And then there's also something that was fixed a while ago, but the advisory is published now, so that's also fixed in both 2Directs and 3-directs.
Yep.
**Trent Mick** 02:55 To talk about the first one a little bit, a question I had is that the severity for that one comes out high.
But… like… Doesn't the attacker already effectively have to have some measure of control over the running system here?
**Marc Pichler (Dynatrace)** 03:11 I…
**Trent Mick** 03:12 One, changing environment variables, which I think we've dismissed once before, is saying that's not in our, maybe this one's a little bit more subtle in that… I don't know. Someone can convince a deployer to put something on the path before that, and they know that there's a KNV Utility there, and, like, he can be a little bit subtle about it, but yeah.
Seems crazy.
**Marc Pichler (Dynatrace)** 03:35 I think, from reading this here, I found… oh, no, wait, that wasn't it.
Where does it link to the… Description here, maybe.
There's a lot of text there.
But in essence, what I found was that… the main… Issue with this is when you… Have somebody started with a different user, and that user has more privileges than you, and you override the thing.
then somehow it could execute that binary that you put there, and do some… Not-so-nice things, but… I agree that high seems a bit…
**Trent Mick** 04:34 Anyway… Yeah, it was high for the equivalent in the other languages, so fine. I didn't challenge that at all, but yeah.
**Marc Pichler (Dynatrace)** 04:40 I also saw the high end, was like, I'm not… I'm not so sure about that, but
**Trent Mick** 04:45 Oh my god, everyone stop everything and patch your BST machines. Yeah.
Anyway, okay, that's all I had on that one.
Maybe touches on the… the last item that I added to skip over once.
A little while ago, Curl, that project is obviously a bigger deal in the open source community, in terms of… Or at least from my perspective, the visibility is quite high in them handling their, security advisories and stuff. They changed recently to have a policy to any… Vulnerability… rated lower than high, they would just deal with in public. They wouldn't do a, like, a… secret disclosure and all that kind of stuff policy, I wonder.
Anyway, like I was gonna say, maybe we do the same, but I think if we get an advisory coming in through the reporting system, it would probably be more work to ignore… the private fork mechanism that's given there and doing that work, rather than just going and doing that, but yeah.
Because there's a little bit of pain in the ass, because the checks don't run, but I guess it's not a big deal.
**Marc Pichler (Dynatrace)** 06:03 Yeah, I… I usually… I… I have to say, I also would prefer Dealing with anything that's not, hybrid.
Like, rated as high, to just deal with it out in the open, because… as you said, it's a bit easier. I think working around the… private fork thing, is worthwhile in these cases, because one of the things in CONTRIP we'll also have to deal with is that the commit will just say, something along the lines of.
-Oh.
Merged fix from a fork or something, and that's not… gonna be picked up by a release, please, so we'll have to… I have to fight.
**Trent Mick** 06:50 Yep, yep.
**Marc Pichler (Dynatrace)** 06:51 Yeah, I think we would have to do another PR somewhere that just changes some… Changes, really.
**Trent Mick** 06:58 Oh, I seem to even bothered picking up to do a release, yeah.
**Marc Pichler (Dynatrace)** 07:03 Yeah, so, for these cases, I think not having to do that workaround and just having the fix.
Merged in the open, or maybe doing the review first on the private fork.
And then just opening the PR and merging it from there.
is gonna be The more efficient way of doing it.
**Trent Mick** 07:27 Were you gonna create an advisory for that, do you think? Like, ahead of time, to have the ability for this private fork to do it? I guess, maybe.
Yeah. Like, before preparing this… mythical vulnerability that no one knows about right now, that Marc and I are talking about.
Yeah, okay.
Sorry, that wasn't clear. I was gonna ask, so are you, like, we're talking about doing a contribib fix?
If you're considering doing it a private fork, or the mechanism to get that is if you go report.
the issue through the security system? Yeah, okay.
**Marc Pichler (Dynatrace)** 08:04 No.
Probably wouldn't, do that, I would just open the PRs.
If we had a vulnerability that was not a high vulnerability, but a… lower one.
I would…
**Trent Mick** 08:18 I mean, you could create your own private fork, and then if you wanted to have some private, you could create your own…
**Marc Pichler (Dynatrace)** 08:24 Yeah. There's…
**Trent Mick** 08:26 Actually, not a fork, if you can't do a fork. Forks… if you push a commit to a… I don't… actually, I'm not even sure of the mechanisms of this.
Because I'd thought internally in GitHub.
if, like, if you actually care about keeping that thing secret so other people can't see it, if I create a fork, so forget private for a second, if I create a fork on my GitHub account of OpenTelemetry.js contrib trip.
And I commit a push of feature brands to that thing.
Anyone can see… Sorry, that commit, Shaw shows up.
On, like, the main repo.
Even though it's so on a fork. I don't know about doing private. Can you do… can you fork something and create a private thing, or would you just pull it.
**Marc Pichler (Dynatrace)** 09:14 I cannot push it.
**Trent Mick** 09:14 as a disconnected repo, I guess, is what…
**Marc Pichler (Dynatrace)** 09:18 Yeah.
**Trent Mick** 09:18 private, but yeah, okay.
**Marc Pichler (Dynatrace)** 09:19 I think you would have to do it on a disconnected repo, and for that, the security advisory flow is… Better, in a sense, because you can just… like, do it from the UI there, you don't need to… Yep.
**Trent Mick** 09:35 Yep, yep. And then if you wanted review from me, for example, you'd add me as collaborator, and then…
**Marc Pichler (Dynatrace)** 09:40 Hmm.
I still haven't… I don't have a concrete plan yet how to do it, for… that case, but whenever it comes up, I would say we just… try it out once, and then later we can see what works and what doesn't work well, and then we,
**Trent Mick** 10:02 This is a good one to explore.
This is less than high, so it's… To do whatever, to try it out, yeah.
Okay.
**Marc Pichler (Dynatrace)** 10:16 weird.
**Trent Mick** 10:21 Okay, so this one, this is a PR that Matt Ware started a long time ago, and I'd… Been doing some reviews, and we went back and forth, and… It changed over its lifetime. I'm not sure if he's had a chance to update the description.
Because the way it's implemented has changed a little bit, but… so I just wanted to socialize this a little bit for other maintainers and approvers to get their sanity check before I merge this. I would either merge this later this week or early next week.
So this… okay, the problem that's being solved here is, in declarative config, there's an instrumentation slash development top-level node.
That has some structure in there. And, kind of an afterthought to the declarative config work was to… add that and provide a mechanism for instrumentations to get config out of a declared config file, and this adds support for that. So, what the spec describes as a config provider in the API alongside tracer provider, meter provider, those things. This adds an API config package in experimental to add support for that.
And it adds… support to, the instrumentation base class now gets a setConfigP provider, besides set tracer provider, setMeterProvider.
That is… The mechanism that we're suggesting instrumentations use to Know when they can get their config from the system, because the only way an instrumentation can get config is after the SDK has wired it up. The SDK has to provide a config provider that has read this declarative config.yaml file and provided a config, so… Right now, we don't have a clean mechanism for instrumentations to know when the SDK is ready and it's good to go. The… for Trace Provider, Logger Provider, we do that by having a, what's called this proxying implementation, so you can get a logger or a tracer, and if the SDK later registers the thing, then it's fine, it gets proxied through from either provider. We don't have that, but we hack it with this update metric instruments.
method in things that surplass instrumentation-based, so that's a little bit of a hack in the meter side. In config, there's… we haven't gotten into something fancy for proxying, for the order of things. So… the proposed mechanism here is that setConfig… config provider is a way that an instrumentation can know. If you're some instrumentation that's, like, a native instrumentation that's not associated with the SDK or anything like that, right now there isn't a good promise, other than you have to know that Hopefully, your instrumentation starts up after after the SDK is up and ready and going. So, the only example I know in the wild is the… the Elasticsearch client.
If you use a JavaScript Elasticsearch client, it has native hotel instrumentation in there, so it will… it built into the library itself, so it'll use the OpenTelemetry API and look for a registered trace provider and do tracing stuff. It doesn't, obviously, doesn't do anything with config yet, because Because that isn't a thing yet. But, so that's a case where the order of SDK startup and instrumentation, so looking for config isn't well-defined right now. This is… Somewhat part of this… project that I wanted to define. There is… actually, there is… in general, there's no mechanism there, because the SDK doesn't know anything about this.
native instrumentation and Elasticsearch client. So, that's a bit of digression. There isn't really an answer here, so… The answer for instrumentations that are provided to start Node SDK is that They will be… registered.
And setConfigProvider will be called after the SDK is started up doing its thing. So that's kind of the one thing I wanted to socialize, and then the other one is… Heads up, we're adding an API config, is that something you guys want to take a look at before we merge this?
I think… That's a question.
**Marc Pichler (Dynatrace)** 14:39 Yeah.
I… I think we can just go ahead and, merge the API config and then see what works for us and what doesn't. One of the things that, Might be… Good to think about once we edit would be, the way to stabilizing debt?
because the instrumentation package is gonna depend on it, I think it would be good to, have, like, a clear path to… or, like, a possible path to stabilizing the API there.
One of the benefits that we had with actually stabilizing logs is now that… now we have, like, a bunch of stuff In the instrumentation package that would is stable.
and adding this… changes the shape of,
**Trent Mick** 15:46 Somewhat a blocker on stabilizing instrumentations, you mean?
**Marc Pichler (Dynatrace)** 15:49 Yeah.
**Trent Mick** 15:50 Do you think it is? Like, could we not have… so say… say instrumentation was stable right now, and we wanted to add this.
**Marc Pichler (Dynatrace)** 15:58 We would… we wouldn't be able to do it, because, if we add this.
Then, like, whenever there's a breaking change to… Api config.
Then the shape of the instrumentation changes and isn't assignable anymore to other versions of it.
**Trent Mick** 16:22 There's no way to do that.
**Marc Pichler (Dynatrace)** 16:25 One way to work around that would be to have a separate type called, I don't know, experimental instrumentation.
that… Has this, it's okay to break it, every once in a while.
**Trent Mick** 16:41 And any instrumentation that wants to use config would…
**Marc Pichler (Dynatrace)** 16:43 Yep.
**Trent Mick** 16:44 Would implement that interface instead of the other one, yeah, okay.
**Marc Pichler (Dynatrace)** 16:48 And then it's kind of clear also that the thing is experimental.
And it might break.
Yeah. But since the package is experimental anyway, we're in this weird state where if we were to add, like, experimental instrumentation, then the other instrumentation is also… Experimental, so why have two of them?
So I get the point, to just edit like this.
It's just something to be aware of, that it might block us from doing things with instrumentation if we are adding that now.
**Trent Mick** 17:25 Okay.
**Marc Pichler (Dynatrace)** 17:31 But I wouldn't block this, as it stands right now. I think it's, Good to have something in… in… that… I have something in the core package that implements that, and then we can figure out what to do with it later.
**Trent Mick** 17:49 Okay, so, great. Cool. I'll point to a couple of things that maybe people want to take a look at if they want to venture an opinion. One is the comment that's up just a little bit at the bottom half of your screen there.
So the config provider… Spec talks about… Like, as the spec does, it says a provider should provide methods for doing the following, and the thing that it's meant to provide is access to this instrumentation slash development node.
But if you go look at the Java implementation, what they've done is a method that does that, but then also access to… the, is this a job one?
**Marc Pichler (Dynatrace)** 18:27 Is it a child.
**Trent Mick** 18:28 This is the Java one. So yeah, so they have a Git Instrumentation config at the top, and that just gives you access to the top-level instrumentation development node in declarative config file.
And then they have another… the second method there is get instrumentation config with a name, so using, method overloading.
That one provides instrumentation slash development dot java, so, because this is Java land.
whatever name's being passed in. So we've done the equivalent, but we use different function names, because I didn't want to get into method overloading in JavaScript, because it's actually not really a thing.
And if you accidentally pass in an undefined for name, then you get some totally different note than what you expected, so… Also… oh, and then we have, get… general instrumentation config. So, a part of the instrumentation node in declarative config has a .js.java.whatever for all the different languages, but also has a .general that does have a bunch of config underneath that are specified in the schema, as opposed to being unspecified.
And so there's some things in there for common things like HTTP and which headers to capture and stuff like that. So that's why the general thing exists.
So that's one thing, if you guys are cool with the names that have been chosen, if you go back to the comment.
that we have different names from what Java is using there. The spec does not specify what the name should be at all. So I… I suggested this git instrumentation config root as that last one, which is the root thing. Most instrumentations should never need to go there. They just want to access git instrumentation config with a name.
Where that name is Instrumentationscope.name. So, we're setting a pattern, which isn't required, but we're suggesting a pattern that… The instrumentation scope name be used as a place where an instrumentation gets its own config.
And then the general area, if… they're an HTTP instrumentation that can access general.http or care, but… config this term.
So that's one thing, if the names there make sense. The other thing to look at is if you go look at the changes… And look for… where is it?
Let's scroll down.
Read declarative configuring near the bottom.
There.
Okay, so there's a convenience method, you scroll down to the bottom, I think, or near the bottom for where the… oh, no, sorry. In that file, up a little bit… this function. Okay, so there… no, down a little bit, line 250, I think, about that 225, yeah.
242. So this is a convenience method added in the instrumentation package for… So an instrumentation that wants to get config has to implement the setConfig provider, and that's when they know the SK has provided it, so they can use this method as a convenience for Reading a declarative config… properties into… Their typed config parameters.
And so if you scroll up a little bit, I think it shows kind of an example.
And so this is an example. The guinea pig that we have right now is instrumentation HTTP is using this. And so, what this thing is saying is, okay, config provider's ready.
call this method that will call the config provider to read the instrumentation.general area and the instrumentation.js.instrumentation spoke name area.
And map those… And that's that reader function that you pass in, which basically describes the shape of the instrumentation's config.
And then… What types the types of things to read. Anyway, you guys can… take a look, maybe look at instrumentation HTT as the best example. If you ever happen to be working on an instrumentation adding support for declarative config, then this will be the method. So, a lot of the time, back and forth with Matt and I was on… what the shape of this convenience function should be. Sorry, I'm wasting too much time. Anyway.
Something else to look at, if you're curious.
**Marc Pichler (Dynatrace)** 22:47 Thanks for, walking us through the changes there.
One thing that I just saw when… We were talking about the previous thing, which was… Boom.
The naming of these… I guess this is the file… To look at here… One thing I noticed is that, like, all of these return config properties, so I wonder if it would be possible to just collapse these into one Get instrumentation, or… yeah, get instrumentation config and having options there.
To select which one you want to get.
So that we… Don't end up with multiple of these that… where we… Later on, might have to add more of them.
**Trent Mick** 23:47 Oh, I can't imagine we ever would.
**Marc Pichler (Dynatrace)** 23:49 more.
**Trent Mick** 23:50 Is one… counter-argument for that. There, so instrumentation… The node is… A language-specific area.
And a general area. I think… I can't imagine when would we have a different area.
possibly… Like, there's this thing, so it's infantation.js.
And for a while, I was thinking, like.
you know, WebJS versus Node.js versus something, we might want to switch there, but if we're setting this pattern of using instrumentationScope.name, then I think that that separates those things.
sufficiently in that Node.js and different runtimes can coexist.
In that area.
I can't think of it, I mean… whatever. The Java API example kind of… gives me some encouragement that there's, like, thought to the design there, because that was done by Jagberg, who's doing most of the declarative config work.
Okay.
**Marc Pichler (Dynatrace)** 24:50 I think this is more of a, like, unique thing that's different between Java and us, where Java can only have one version of the API.
In a given app, and we can have multiple versions.
So in terms of compatibility, I think having the options is going to be a bit easier.
Because then we can just make anything that's unsupported a no-ob.
Instead of actually… Breaking on compile.
**Trent Mick** 25:32 Oh, you mean if you wanted to add a new thing? Yeah.
**Marc Pichler (Dynatrace)** 25:34 Yeah, if we want to add a new thing, the SDK has to implement it, whereas if we have options here, the SDK can just return An empty object or something like that.
**Trent Mick** 25:47 That is… so that is the no-op behaviors and empty config properties, which is…
**Marc Pichler (Dynatrace)** 25:52 Yeah.
**Trent Mick** 25:52 object, yeah.
**Marc Pichler (Dynatrace)** 25:57 in any case, I think that's something that, like, if we ever need it, we can just add a single, A single method there that… Does it with the options, and then it's a break once.
And… We can model everything on top of that.
**Trent Mick** 26:19 Well, it's not a break to be additive, right, if you add a new method.
**Marc Pichler (Dynatrace)** 26:22 Yeah, it's… it's not a brake according to the spec, but it's still breaking too.
**Trent Mick** 26:26 In terms of us having to.
**Marc Pichler (Dynatrace)** 26:28 Yeah. Gate on everything.
**Trent Mick** 26:29 Maximum minor version, yeah.
**Marc Pichler (Dynatrace)** 26:31 Okay.
**Trent Mick** 26:32 Not a break, but pain.
Personally.
**Marc Pichler (Dynatrace)** 26:35 For implementing it, it might be a bit easier for us to… Do it with the options here.
But…
**Trent Mick** 26:46 So, okay, so, right, I can't… one, so two arguments against. One, I can't think of when we would need another one, and… Two, like, this is just personal preference on API design.
a rule of thumb I'd had before is if you have This method that you call it in… Always one way, and always another way, and, like.
like, get foo, which takes an argument bar that's either… spam or eggs. It's… it's a bad example, but… the rule of thumb API design for me is just have two separate methods, because if you're calling one one way and calling one another way, but, like, I can understand there are probably examples the other way, especially if that enum gets to be larger than two, then… then sometimes it makes sense to have this single method, but…
**Marc Pichler (Dynatrace)** 27:32 And I agree with that.
that, like, having the different methods is nicer in terms of API design.
**Trent Mick** 27:42 Yeah, you're, you're thinking.
**Marc Pichler (Dynatrace)** 27:43 Maybe, maybe that's true.
**Trent Mick** 27:44 Future.
**Marc Pichler (Dynatrace)** 27:45 I've just been looking at… at these, maybe for a bit too long, that I'm, like, always, I hope this doesn't, doesn't cause us problems, but it's probably gonna fine… gonna be fine. And if we ever need to do something else, we can just do what I, suggested now for any of the future things. If there's… if we know that there's gonna be… 10 new ones, then we can go that route. Otherwise… This is probably fine. I just wanted.
**Trent Mick** 28:18 And this is… and this is experimental for now, so there's that, though I guess the pain still exists for us, because… Experimental quickly means de facto standard for us.
**Marc Pichler (Dynatrace)** 28:31 Alright.
**Trent Mick** 28:33 Oh, wait, second one, so component provider, I've done some more work on that, Mark, so, agreed with that thing that you said, so I, with your feedback from earlier, I dropped having a single generic component provider interface. I went a bit, I haven't replied on this thread at all, but if you go look at the changes… Com- Yeah, the top file.
So, right now, okay, The main thing is the component provider registry, which is just below this block.
So this is, I think, like you had, And that we have a… a string mapping to the component provider type for each one of those things. And here the registry is… this is the three-level mapping, where it's the type of thing mapping to the name.
So, for example, a span exporter, the record string would be… Otlp underscore HTTP, console, and OTLP underscore gRPC are the different names. Anyway, the… If you scroll back up to that first block, of things… I've now defined the type to be a function instead of an interface that has a get or createComponent method.
And I thought that's kind of interesting. If you go look at the create from config, the next file, right near the bottom of that.
And the bottom of that file.
as… As the built-in Provider registry.
So, boy, it's nice and tight. I like it.
And that if you do a create function for something that does any interesting work, but the other ones that are just one-offs.
are just returning and don't take any ARGs. So… Anyway, yeah.
**Marc Pichler (Dynatrace)** 30:36 Nice.
**Trent Mick** 30:38 See, I wouldn't mind you taking a sanity check, because you're my TypeScript future backwards compatibility issue guru.
That one.
**Marc Pichler (Dynatrace)** 30:47 Yeah, I'll have a look. But I think it looks… like, from… Just looking at it briefly, it looks, really good already. And this is not, changing any of the public interface right now, right?
**Trent Mick** 31:07 Okay, so the only thing, if you go to types.ts.
So, the design is that a user can pass in those. I don't have any tests for that, and nothing's using that. So, yeah, if I commented that single line out, then this would be a refactor instead of a feature, like you had it. So we could do that, and then the next thing, add support for others using it, but… So that is the thing… that auto-instrumentations node would use to pass in its own propagators and resource detectors.
**Marc Pichler (Dynatrace)** 31:36 Yeah.
**Trent Mick** 31:38 And so, the only work remaining is the XXX is at the bottom of create from config. I need to work through all the various different types. Actually, can you go back to that? No, component provider, go to componentprovider.ts.
And then scroll down a little bit… oh yeah, up, there's an XXX about 20 lines up.
I'm gonna need to take a look, but I may be asking for your help again. The difference in shape of metric readers in our implementation, versus what the spec is doing is a thing that messes me up again, because…
**Marc Pichler (Dynatrace)** 32:11 Yeah, because of the pull metric export, push metric exporter, all of that stuff.
Perfect.
**Trent Mick** 32:20 order shape matches what the spec has, and hence what declarative config stuff has. But anyway, like, I've kind of already dealt with this in the create from config stuff before Component Provider, but I need to… it's not as straightforward.
**Marc Pichler (Dynatrace)** 32:34 Yeah, I'll have a look at that. Matching it to whatever the spec prescribes can be a bit of a pain, because we are doing it differently.
I might also look into just changing the… SDK tool.
Was it Free Auto, or was it?
**Trent Mick** 32:56 the… Yeah, okay, yeah.
**Marc Pichler (Dynatrace)** 32:58 Yeah, maybe we change the SDK to conform what the spec wants us to do, and then our lives will be easier.
**Trent Mick** 33:04 If it makes this easier? Yeah, we'll see.
**Marc Pichler (Dynatrace)** 33:06 Yeah.
**Trent Mick** 33:07 This may be okay now, as functions, I have to go back again.
**Marc Pichler (Dynatrace)** 33:11 I can work around it now, it's probably fine, but Maybe there's also some other improvements that we could make to that part of the code, to… Get some performance improvements and stuff.
**Trent Mick** 33:27 Okay.
**Marc Pichler (Dynatrace)** 33:30 And if we can combine that work with Which is making it easier to use for declarative config and aligning it with other implementations, then, maybe that's a good… Starting point to actually change things there.
But I'll have a look at, your comment here.
And the comment that you… mentioned on… dysfunction,
**Trent Mick** 34:00 So that's when I had dealt with it before, yeah.
Because there's a comment there saying… I think explaining some… that's the thing that explains what the… what the state is, yeah. Anyway, yeah, if you're able to take a look, that'd be great.
**Marc Pichler (Dynatrace)** 34:14 Yeah, we do.
Right?
Thanks for working on that. I think this is the thing that will tie everything together, kind of, dead and the, The work that, link here.
**Trent Mick** 34:38 Yeah, and then… then there are just a few to-dos to be picking up edge cases, but otherwise, I think we support declarative config. After those go in, and then, I want to s… Then we can consider, marking Start Node SDK as the blessed replacement for the new Node SDK class.
Because that thing's a lot more capable. It will be a breaking change for people, because the options have changed a little bit, but yeah.
**Marc Pichler (Dynatrace)** 35:09 Alright.
One question kind of adjacent to that is.
Where is the spec at right now with stabilizing all of that?
declarative config thing.
**Trent Mick** 35:27 I haven't been following closely, but I haven't seen Well, okay, so it's at version 1.2, so it's considered… the stable parts are considered stable. What's up in the air is all these ones that have slash development on them, so that includes resource… Detectors, the resource detection area, which is a little bit more in resource detectors, and… instrumentation config, and then also little bits and bobs here. That's still up in the air, as far as I knew. There had been some issues that were discussing how to model those, because if you stabilize instrumentation.
Slash development, all of a sudden, the node name changes to instrumentation, and, like, what are implementations meant to do when… They get a config file that has instrumentation slash development.
And then a different configurable that has instrumentation.
As the node, so that stuff's not really well defined yet.
And, sorry, is the whole thing still experimental?
**Marc Pichler (Dynatrace)** 36:32 It seems to be a mix of all of that.
**Trent Mick** 36:34 Yeah, so there you go. So, yeah, it's considered.
**Marc Pichler (Dynatrace)** 36:36 Yes, they would accept… Or were otherwise specified, and then there's…
**Trent Mick** 36:45 A config provider, for example, is development.
**Marc Pichler (Dynatrace)** 36:47 Yeah.
config provider…
**Trent Mick** 36:52 So I don't think we would ever stabilize API config until… That stable here.
**Marc Pichler (Dynatrace)** 37:00 Yeah, unless we… Find some way to work around that. Maybe via having… Maybe we are omitting some of these from a staber type and having, like, a separate experimental Thing for that.
I don't think we've ever done that, but… It might be one way to… to do it.
**Trent Mick** 37:33 do that.
**Marc Pichler (Dynatrace)** 37:33 But we just…
**Trent Mick** 37:35 So that one that you have been looking… this one, for example, we don't do this right now, so… but this would be changing start node SDK function to return an object that has all of these things on it. Right now, the only thing we return is a shutdown function.
But how would you… so we could have one right now that returns tracer meter par… the stable ones there.
But if we wanted to add… The two development ones, Resource and Config Provider.
**Marc Pichler (Dynatrace)** 38:07 So, yeah, if we want to do that, we would have to have two separate functions.
one that's…
**Trent Mick** 38:15 Experimental start notice decay.
**Marc Pichler (Dynatrace)** 38:17 Yeah, I think this is the create function, right? So, we don't expose that, Actually, right now, I think it's internal. But we would have, maybe create from an experimental entry point.
And you could get it from there, and then that returns… All of these, and extends these two.
**Trent Mick** 38:42 I was considering getting StartNode SDK to return these things as well, because they are, in general, useful for something that's trying to build on that SDK.
But you're right, it is just the create method that's internal currently, so, yeah.
Okay.
**Marc Pichler (Dynatrace)** 39:03 Yeah. I think…
**Trent Mick** 39:04 Okay, I got you. It just means…
**Marc Pichler (Dynatrace)** 39:06 What about…
**Trent Mick** 39:07 Exposed data.
**Marc Pichler (Dynatrace)** 39:07 Yes.
I think at some point, we would want to, also make Create.
public.
Because then you can also… piece together a distro that maybe does less of what Start Node SDK does, in terms of, like, what's registered by default.
**Trent Mick** 39:31 So… Right, I have a follow-up to do that I was gonna add, is saying that the Java SDK has.
Sorry, I hesitate on Java SDK, because I'm not sure what Java SDK and the Java agent, and where the… what's called what there, but they have this thing called, Give me a sec.
I'll customize config, so they pass in… So when you're basically… when you're saying, okay, start an SDK and use a config file.
they have this, callback called Customize Config that gets used so that the caller can Tweak the post.
YAML config file before the SDK goes over it and does stuff, and that covers at least the cases that I can think of of what you're talking about. So I wanted to provide the same thing, so that a distro can, for example… the best use case I have, and I've seen this in two distros, ours is one, and I think Matt's is another one, where they want to… add a resource provider… a resource detector always that adds the telemetry.sdk.star attributes, which… Or sorry, telemetry.distro.star, which is what distros are meant to do, but… To get that automatically without the user having to specify some distro-specific thing in the config file, that's the natural way to do it.
So, yeah, I wanted to do that. Another alternative would be to expose both the parse And the config step separately, and then… But then, that feels a little bit onerous, because then the whole start node SDK method has to be reproduced by the distros, so this customized config sounded a bit more handy, especially seeing it in the Java site, so that's an alternative.
Yeah. That's not to say that we don't expose all these methods. So when I was writing all those create… from config methods in the, create from config file. I was thinking about eventually exporting some of those so that this SDK becomes a… kind of an SDK lib, a library for people to build SDKs. Obviously, I didn't want to go there yet, because this all needs to… Sit and settle for a while before we promise a whole bunch of interfaces there, but… Yeah.
Anyway, that had been my thought, customized config.
I'll see tonight.
**Marc Pichler (Dynatrace)** 42:08 Customized config plus, A reduced set of… Plugin component providers.
wood.
Be interesting, maybe.
**Trent Mick** 42:20 A reduced set.
**Marc Pichler (Dynatrace)** 42:22 Yeah, because, if you want to still use declarative config, but you want to Make sure that, like, all of the… Or some of the packages that… you don't need aren't loaded.
For example, if you know you're not gonna use the Prometized exporter.
you know, you're not gonna use certain of the other experts. You wanna just drop them, you wanna build your own Distro.
That isn't affected by whatever security, advisories come out.
You can do this.
**Trent Mick** 42:59 So to do that, you'd have to reproduce a bunch of the built-in… so what we have is this Git built-in component providers, right?
You'd have to reproduce the whole… Subtree of… there's a subset of that that you care about.
**Marc Pichler (Dynatrace)** 43:14 Right? Yeah.
**Trent Mick** 43:15 So we.
**Marc Pichler (Dynatrace)** 43:16 I want to export.
**Trent Mick** 43:17 all the base methods for it, because they couldn't… they couldn't just call get Built-in component provider registry, and then.
**Marc Pichler (Dynatrace)** 43:22 Yeah.
**Trent Mick** 43:23 prune it, because that's too late, then they will have already included Prometheus.
Interesting. Yeah. Okay.
**Marc Pichler (Dynatrace)** 43:29 it's just something that I've been thinking about, because that's one of the things, collector distro.
people do a lot.
It's, like, one of the reasons why you would build your own collector destroyer is to, like, strip out all the stuff that you don't need.
Yep. So that… You're not affected by security advisories for components that are just sitting unused in your collector.
**Trent Mick** 44:00 So we could… so if… this is future… if we exported all the methods from create from config, so all of the component pieces of the create step.
then… Users could relatively easily rebuild they're… Component provider registry that they want this reduced set one.
Without having to rewrite any code. And then we would rely on tree shaking to shake out… do you think that's sufficient to shake out those other bits? Like, we don't need to put them in separate files with separate… entry points.
**Marc Pichler (Dynatrace)** 44:35 Yeah.
**Trent Mick** 44:35 We can avoid the actual imports, right?
**Marc Pichler (Dynatrace)** 44:38 Yeah, I think tree shaking and, like, bundling it up into one Script is probably what people would want to do there.
**Trent Mick** 44:46 Okay, so one thing that.
**Marc Pichler (Dynatrace)** 44:47 Actually.
**Trent Mick** 44:49 Good.
**Marc Pichler (Dynatrace)** 44:50 I don't know, I just wanted to say, you would essentially be able to build your own Little distro thing.
**Trent Mick** 44:57 Let me go back to my PR.
The one… the types.ts?
**Marc Pichler (Dynatrace)** 45:03 This was…
**Trent Mick** 45:05 Second one, yeah.
**Marc Pichler (Dynatrace)** 45:06 Good one here, yeah.
**Trent Mick** 45:14 It didn't jump to the… you have to click it twice sometimes.
Oh, no, it is, sorry. So that one… so… the way that's implemented right now in start.ts, the file above, Is it… uses those as… Registries to add… Add to the built-in one to support what you're… suggesting we'd want to change that API, so…
**Marc Pichler (Dynatrace)** 45:42 I guess if create from config?
exists.
**Trent Mick** 45:47 Right, okay, so then they wouldn't reuse… they wouldn't reuse our node SDK, then.
**Marc Pichler (Dynatrace)** 45:52 Yeah, they wouldn't… Yeah, dude, it's far enough off…
**Trent Mick** 45:54 the reservation that they do parse and create themselves, and use the utility, etc. Okay, I'm cool with that then.
**Marc Pichler (Dynatrace)** 46:01 I think that's also, I don't know if that's the intention of the spec to allow for something like that.
But it kind of… like, when I read the spec, it kind of felt to me like this was one of the goals.
**Trent Mick** 46:20 Okay, yeah, interesting. I don't know that… Java, at least, doesn't implement, like, a built-in component provider, so… because they had the existing path that was just coded up, and then if it's not a well-known built-in one, then they go to the component provider, so they don't have the easy ability to do what you're describing.
Maybe it's less of a concern in JavaLin, just gets compiled out. I don't know.
**Marc Pichler (Dynatrace)** 46:45 One of the interesting things is also you can get a smaller, smaller version of Oter that you can include in your apps, if you're doing… Fear in… in… A constrained environment where you don't… Have the space for all the other components, you can just strip it out.
**Trent Mick** 47:10 Being of Browserland, David, did you want to show your… well, you probably don't have already this. This is something that you were playing around with a while ago. Do you want to mention it or not?
**David Luna Bistuer** 47:20 Do you mean the builder?
**Trent Mick** 47:23 Yeah.
**David Luna Bistuer** 47:25 Okay.
**Trent Mick** 47:27 You don't have to show it, do you want me to just…
**David Luna Bistuer** 47:28 I don't have this right. No, basically, no, I can show you later. Long story short, it's like, since the… an NPM package that actually reads the configuration, and then… For browser, the concern on browser detects, we don't… we want to ship only what we… What we are using.
So, that's what it does. So, it creates the configuration. If the threshold provided is configured, then it adds the code from the SDK trace.
and configures it. If not, the code is gone. There is no imports, there is no code at all, so that's not… that's not ending in the final bundle.
And actually, it works, also we did, kind of, similar things with the, With the instrumentations. Instrumentations are bundled in or out, so they're filtering a lot with that.
Yeah.
kind of the idea is it's similar to this, so we have kind of conversations with Trent about how.
**Trent Mick** 48:26 But it was.
**David Luna Bistuer** 48:26 We're… yeah.
**Trent Mick** 48:28 Yeah. The big difference is it's build time instead of runtime, so it reads the config and it emits boilerplate.
**Marc Pichler (Dynatrace)** 48:34 Yep.
**Trent Mick** 48:35 Setup, SDK setup code, yeah.
Which minimizes. So, I mean, that could be something that could be… Theoretically used on the node side, too, if people want to have small boilerplate, instead of using Node SDK, they can use the level below where they're using SDK Trace directly and have it read from config, yeah.
**Marc Pichler (Dynatrace)** 48:58 That's pretty cool. Having it… like, having it do that statically is a nice way of also having declarative config work for the browser. I like it.
**Trent Mick** 49:11 Yeah, that's the idea. That was, I guess… well, I guess that was David's idea. Yeah, it's looking at this declarative config work for… because the browser SDK right now, they're going through defining their own interface for config again, which is just a pain in the ass, but…
**Marc Pichler (Dynatrace)** 49:26 Correct.
**Trent Mick** 49:43 How many issues in Paris coming in?
**Marc Pichler (Dynatrace)** 49:46 Yeah.
I guess we could skip, triage for today.
I guess if we don't have any more topics to discuss… We can… Audit a meeting.
**Trent Mick** 50:04 Sounds good.
**Marc Pichler (Dynatrace)** 50:07 Alright.
Dan, thank you all for training.
**David Luna Bistuer** 50:10 Okay.
**Marc Pichler (Dynatrace)** 50:11 Have a nice week, and see you around.
**Trent Mick** 50:14 Okay, same word, same day.
**Marc Pichler (Dynatrace)** 50:15 See you.
