SIG: JavaScript SIG
Date: 2026-07-08
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:01:43 Hello.
Matt Wear 00:01:47 Hello?
Marylia Gutierrez 00:01:48 Hello?
Trent Mick 00:01:49 Hey, y'all You're not sadly just biking around your house or something like a week.
Marc Pichler (Dynatrace) 00:01:57 No, this is my partner's bike. We don't have a spot for it, so it's sitting here. We might hang it on the wall or something.
Trent Mick 00:02:09 Actually, I didn't even notice the bike over your shoulder. I was just referring to your.
Marc Pichler (Dynatrace) 00:02:13 Yeah.
All right, I'll share my screen and then we can get started.
Daniel Dyla (Dynatrace) 00:02:29 Mark, are you riding without bar tape?
Marc Pichler (Dynatrace) 00:02:33 Oh, no, this.
Trent Mick 00:02:34 Here it comes.
Marc Pichler (Dynatrace) 00:02:35 This is my partner's bike and it does have bar tape on it. It's just black bar tape.
I can't move it closer now, but…
Daniel Dyla (Dynatrace) 00:02:46 Yeah, no, you get that.
Marc Pichler (Dynatrace) 00:02:47 I can send you proof, later.
Daniel Dyla (Dynatrace) 00:02:53 I'm riding without bar tape right now.
I'm playing with my… I'm playing with my bike fit, and I don't want to keep having to, like, re-wrap every time I change… Handlebars and stuff.
Trent Mick 00:03:05 They just ride on the horns all the time then or That's fine.
Daniel Dyla (Dynatrace) 00:03:09 Yes.
Trent Mick 00:03:09 That's fair. Yeah, okay.
Daniel Dyla (Dynatrace) 00:03:10 Yeah, and even on the carbon, it's not that big of a deal.
Marc Pichler (Dynatrace) 00:03:22 All right, let's get started.
On.
The first topic here is, just a follow-up to what we talked about last week.
here, I'd been looking into the difference, that it would make to use enter with and with scope.
on the… Async local storage to make, context attach work.
I did run some benchmarks and try some stuff out, and it seems that Both of these approaches are fairly similar. It seems that enter with and with scope just completely dominate in terms of allocations. So in the end, there's little difference. So I'm now looking into making the token that's returned by context attach.
Disposable?
There's still some unknowns that I have to work through, I did merge, TypeScript bump to 5.2, because that's, Less than… or, like, more than 2 years old at this point, and within the range of what we support.
And now I'm looking into if it could cause problems with browsers, If somebody has to implement, A disposable… Oh.
on… The token that's returned by context attach.
Because Simber Dispose is not baseline widely available, it's mostly a problem with Safari at the moment.
So that's just an update of what's happening there.
Daniel Dyla (Dynatrace) 00:05:15 Yeah, but we should be able to check if dispose is there or not. And if it's not, you just don't.
Attach it, as long as there's some other way to… Dispose of the context as well.
Marc Pichler (Dynatrace) 00:05:29 Yeah, so the plan is to have a normal dispose method on there that's just called dispose.
Daniel Dyla (Dynatrace) 00:05:36 Yeah.
Marc Pichler (Dynatrace) 00:05:36 I have the disposable, or like the symbol dispose as well.
Umm.
might get finicky with, types, and I'm not sure if any build tooling complains about it. So that's what I'm looking into right now.
Daniel Dyla (Dynatrace) 00:05:52 Well, we could probably just assert that it's disposable. Do it in an if else, and then at the end say.
like, return it and assert that it's disposable. If they use a version of… TypeScript, that's… older than… That assert… that assertion would probably…
Marc Pichler (Dynatrace) 00:06:16 Yeah, it's, I tested it with older TypeScript versions, so with, 504, that's the one that we had before.
And with that one, it actually doesn't compile, so you need to install at least 5.2.
To get it to work.
So for TypeScript, I know that it's a problem, but, we specifically state that we… will bump TypeScript versions, in minor version updates.
So that's one of the changes that we made with 2.0.
So, yeah.
Would be okay for us to do it.
For the browser stuff, it's a bit more difficult to figure out because of the many different bundles, and not sure if they complain even about the usage of SimberDispose somewhere that doesn't exist.
But I continue looking into that,
Daniel Dyla (Dynatrace) 00:07:17 Mmhm.
Marc Pichler (Dynatrace) 00:07:18 Yeah, it's just making Making it work that way is just a little bit more work, so… That's the update on context attach and detach.
Alright, Moving on.
I did create this pull request about the announcement for SDK 3.0, so if anybody, has some time, or, wants to give some feedback on on this here. I would appreciate that the idea is to have that be a pinned issue.
It's easier to discuss on the contents of the issue on a pull request, rather than just opening the issue and then having a bunch of discussion and editing stuff.
So I'm looking to go that route. It follows a similar structure to what we had with 2.0.
In 2024.
So… Thanks, Trent, for already having a look there.
I guess I'll keep that open for a bit, and once it's approved, I will also open the issue.
for it.
Trent Mick 00:08:46 I'll look again today. I assume I'll approve it. Just the only thing was the Jaeger package name.
Marc Pichler (Dynatrace) 00:08:51 Thanks. Yeah, on that, I think… I did put a comment here already.
the propagator is actually also, deprecated. It kind of went under my radar, and I just recently noticed it, when working on the… Security advisory that was recently published.
That… The spec actually says… Umm.
Additional propagators may be maintained and distributed as OpenTelemetry core packages, and then there's Jaeger status deprecated.
So…
Trent Mick 00:09:32 Cool. I hadn't known that. I trolled the OpenTelemetry blog posts looking for something about the Jaeger Propagator, but didn't see that because they'd had one for the exporter being deprecated. But yeah, cool.
That's easier.
Marc Pichler (Dynatrace) 00:09:46 Yep.
I also opened a PR already to deprecate the… Oh.
Propagator itself, and, emit a warning in… Where is it now?
emit a warning in SDK Node to let people know that, they should.
Switch over.
In case they're using it. Didn't remove it quite yet, because, that would probably be… A breaking change that would hit a bunch of people that are using that.
All right.
keeping on the SDK 3.0 topic, I created this tracking issue, for stuff that needs to be done before we can start working on it. It's mostly getting the release set up, In order, and then also the 3.0 announcement, if there's anything, we should do.
In addition to that, feel free to just link the issues here as sub-issues.
So that we can track it separately from the SDK milestone.
There's probably a bunch of things that we can do before, Starting with the feature freeze on 2.x.
Trent Mick 00:11:26 I was kidding.
Marc Pichler (Dynatrace) 00:11:27 Alright, then let's move on to the next topic, Marilia.
Marylia Gutierrez 00:11:34 So yeah, we have a… Well, in case people don't know, we have a new repo that is, like, for shared workflows, and we have been adding a couple of things there that are helpful for different repos, so one of the workflows now is, like, first-time contributors, so if it is your first time opening a PR, you get a message basically saying things like.
look at our, like, GenAI policy, wait a little before, like, starting tagging people, and give, like, time to review. So there's, like, basically generic message, but if there is anything specific for repos, there is, a parameter that we can add more stuff.
So I was just wondering if there is anything that we want to add here. For example, one thing that I could think of is for the core one, we can point to say like the focus topic saying like if you are not open a PR that is not a focus topic might take longer for review or something on along those lines. But I just wanted to check before adding that.
Marc Pichler (Dynatrace) 00:12:32 Yeah, I think, the… just the GenAI and, the CLA info is… already very helpful.
I think we haven't really, had a bunch of delays for stuff that wasn't, focus topic related in the last, in the last few months, so… I'm not sure how much of an issue it is. Okay.
Marylia Gutierrez 00:13:02 Yeah, but yeah, just keep in mind, I can keep it as is, and then we can always add stuff in the future.
Marc Pichler (Dynatrace) 00:13:09 Yeah, one thing that I see happen a lot is the changelog entry.
which sometimes is missing, and then we have to poke people to do it, though with.
Marylia Gutierrez 00:13:22 I know.
Marc Pichler (Dynatrace) 00:13:23 contributions, it's gotten a little bit better, including these.
Marylia Gutierrez 00:13:29 Yeah, I can add a message for, like.
Make sure you're added a changelog. Well, again, that is only on the court, right? Not on the contract.
Marc Pichler (Dynatrace) 00:13:36 Yeah, it's just a core repo.
Marylia Gutierrez 00:13:39 Okay, yeah, I can make that addition.
Marc Pichler (Dynatrace) 00:13:42 Yeah, thank you.
Yeah, but I think, like, all of these… Like, the contributing guidelines and the… CLA and stuff, this, Are already very helpful, something that we run into all the time.
Marylia Gutierrez 00:14:03 Okay.
Next one is also mine. So, this… So basically, like, on the, like, GC side, we got a message saying, like, we're gonna basically deactivate all of our Zoom accounts.
And we have until the end of the month to use the… account from like CNSF and like LFX. So basically we have to migrate everything to the new accounts. We have been trying, like we already tested that like as a trial for the like GC calls, GCC, TC calls and it's.
basically, like, okay, use this new link instead. So we are looking for, like, volunteers. So… but there are, like, a few things still figuring out.
So I just want to see if, like, for example, I can use this one… we want a few SIGs to test it out, because the… for the people joining the call is now… I'm gonna just update the link on the calendar, but if somebody has copy, like, the event, it's gonna point to the odd one, so my… ideas also update the doc itself in the top, put something a little more, like, calling out, hey, there's a new link, make sure you're using this link, but that is pretty much it. The only issue right now is that The workflow for the recorder to be added to that spreadsheet is not working with the new ones, and we don't know how to make it work.
Because the problem is that we don't have… because the existing ones, we have access to the Zoom accounts, so when you, like, the workflow, we have to, like.
basically enable by logging into the account, but the new ones, the portal only give us the link. They don't give us access to the actual account, so we still haven't figured out a way to the… the meetings are being recorded, it's just the flow to put them there that is not working. So there is, like, a default flow to put, like, on YouTube, so we might consider that one, but So it's gonna be a little, like… weird for a little while for all the SIGs until we figured that out, but I just want to see if I can use this SIG as one of the examples to try it out with just a new link.
Daniel Dyla (Dynatrace) 00:16:15 So we lose the recording.
like, spreadsheet stuff, people will not be able to access the recording until we figure that out. Correct. And we… we probably also lose any moderation capabilities, if anybody… Is joining and and.
Marylia Gutierrez 00:16:31 So we do have that bit.
Daniel Dyla (Dynatrace) 00:16:33 Just like that.
Marylia Gutierrez 00:16:33 So, we do have access, there is a code for, like, Become, like, a host, then…
Daniel Dyla (Dynatrace) 00:16:39 Host keys are still available.
Marylia Gutierrez 00:16:41 So it's still available for us. And our idea is actually we're going to share like the maintainers for all the SIG, their respective keys. So they have access. They don't need like a GC member to join and kick them out. So we want to share with those.
But for now, if you… if you make the change now, the only thing is that the recordings will not be available on the spreadsheet.
Trent Mick 00:17:10 Or… Maybe this is then for a question. Are you volunteering to go update the spreadsheet, then, or while we figure that out, or like it. It sounds that you're.
Daniel Dyla (Dynatrace) 00:17:22 Well, the reporting…
Trent Mick 00:17:23 Involved in trying to figure this out.
Sorry?
Daniel Dyla (Dynatrace) 00:17:26 The recordings are not going to be available at all while we work on this. Like, you can't even manually get the recording.
Trent Mick 00:17:32 Oh, I thought you said we got a link, but we couldn't.
I have a flow to put that in the spreadsheet.
Daniel Dyla (Dynatrace) 00:17:39 Not a link to the recording, we just get a meeting link and a host key.
Trent Mick 00:17:43 Okay. I misunderstood.
I mean, it kind of sucked not having recordings. Not like I go back and look at them very frequently. I have.
Daniel Dyla (Dynatrace) 00:17:53 Yes.
Trent Mick 00:17:53 But… Oh.
Daniel Dyla (Dynatrace) 00:17:56 You never know when.
But if it's only a month, like, we don't have the choice to keep the old account.
Marylia Gutierrez 00:18:02 So, yeah, it's gonna be great either way.
Marc Pichler (Dynatrace) 00:18:06 Yeah. Might as well.
Trent Mick 00:18:08 Did… how are… I haven't followed that at all. Where are the recordings kept? Like, were we extracting them from Zoom and putting them somewhere on storage that Hotel owns?
Or CNCF phones.
Marylia Gutierrez 00:18:21 You mean the the current ones or the new ones here?
Trent Mick 00:18:24 Yeah, the current one. So if we're switching accounts, we're not losing access to your old recordings.
Marylia Gutierrez 00:18:29 So, that is also… we will, so we are trying to find out a way to also… like, migrate those recordings to someone else, someplace else.
Trent Mick 00:18:42 Okay.
Daniel Dyla (Dynatrace) 00:18:43 Yeah, we originally removed them from YouTube to stop people from, like… Scanning them and generating, like, deepfakes of maintainers. That was the original, like, Fear, when we did that.
But now they're on… a, you know.
Locked platform. That was the risk.
Okay. Yeah. To be completely honest, I think it's… it's now so easy to generate deepfakes that I don't think you would even need to bother pulling a bunch of videos off of YouTube. I think you could join one meeting, record locally.
And generate a deepfake, and it would take one day.
Marylia Gutierrez 00:19:28 See, this is why you have to use my approach. I keep changing my hair color. So if you see something from like two months ago, like, no, it's not new. Right now it's green, it's blue. Yeah, just keep changing.
Trent Mick 00:19:39 You're just training the world to accept any color. So.
Marylia Gutierrez 00:19:42 Yeah, I don't know.
Daniel Dyla (Dynatrace) 00:19:47 I was not one of the ones that was super worried about the deepfakes, but I was on the GC at the time, so I do remember all the discussions. There were a few people who were very worried about it.
to be determined, if we end up putting all the videos back on YouTube, what will happen?
Trent Mick 00:20:10 Well, I'm leaning towards the YOLO side of things, like fine, go for it If he needed getting paid, but I'm not the only person here.
Daniel Dyla (Dynatrace) 00:20:19 Yeah, if we need a guinea pig and we have to, like, by the end of the month, they're changing us either way. So this is only really affecting, like, three meetings I just don't think… It's fine, I think.
Marc Pichler (Dynatrace) 00:20:32 Yeah, I think also it, like it happens at at some point that if you just figure out that it's breaking later, then.
Marylia Gutierrez 00:20:42 And we can be like more dealing for like for the next recall. Make sure that we really take notes like very detailed notes.
So in case people wanna look back, they have the notes for them. The next we want until we figure this out.
Okay, yeah, gonna let's… Gonna tell them that we I volunteered this sake.
Marc Pichler (Dynatrace) 00:21:12 All right.
Daniel Dyla (Dynatrace) 00:21:13 You're watching the recording of this video and have massive objections to this.
What do you do? Do you reach out to Mary Leah.
Marylia Gutierrez 00:21:23 Yeah?
Daniel Dyla (Dynatrace) 00:21:24 Okay.
Because all the people joining the call are probably the people least likely to object.
Marylia Gutierrez 00:21:34 So.
Marc Pichler (Dynatrace) 00:21:37 All right.
Yeah, I guess let's move on to the next topic then. Matt,
Matt Wear 00:21:46 Yeah. So next topic is is me. Maybe I'll share my screen and Yeah, I was just thinking, I opened this PR for declarative config for instrumentation. It's a little biggish, so I thought maybe I could just give, like, a quick, like, 5-minute Tour of it, and then discuss how we want to proceed. Like, I can break it up into smaller… smaller pieces, whatever… Whatever will make this easier.
Does that sound reasonable?
Marc Pichler (Dynatrace) 00:22:16 Yeah, sounds good.
Trent Mick 00:22:17 I'm sure, yeah, as an early intro, like, I reviewed your earlier one, and this is the next bullet on my… set of to-do lists, so I do plan to get to this. I just haven't yet. So, like, the week delay in reviewing, sorry, is not because, oh my god, this is too big, it's because I just… I haven't gotten there yet, but… Anyway, go for it. Thanks for working on this.
Matt Wear 00:22:39 Yeah. And if it turns out that it's not too big, and we want to review it as as 1 1 thing, I think that's fine, too.
So, yeah, I think most people know what declarative config is, but there's this instrumentation development section, and then each language gets its own key underneath it.
This is kind of how I'm proposing it should look. The key would be the NPM package name for the instrumentation, and then we have the config below it.
Config would be in, kind of, snake case to match the rest of declarative config.
There is another, field under instrumentation development called general. I didn't put it in this example, but that would be a next kind of follow-up after this, is to implement general.
in general, I don't know, there's kind of, like, config for, like, HTTP libraries generally, like, which headers to include or exclude, for example, and… Those should apply to all instrumentation that kind of have that setting. But I'm kind of getting ahead of myself because that that is not yet implemented.
So, yeah. And I guess just as a just as background. There is some spec around this, and you're supposed to provide a config provider. It's kind of one of these top-level globals that lives alongside, like, tracer provider, logger provider, all of that. And then config properties.
Oh.
So In terms of what we should look at, I'll probably start with how this looks from from SDK Node, and then kind of dive into it from there.
So this is start SDK node.
So… We set up our config provider.
And we want to be able to set up our config provider before instrumentation is constructed, so that you can use it from, like, the constructor of your instrumentation to map the config.
There were some wrinkles with that, and mainly, As we pass in instrumentations today, they all come in already constructed.
And that's yeah. That's how it works works everywhere. The In the, auto instrumentation nodes package. There's like a get instrumentations function, and those are already constructed.
So the thing that I did was Introduce a, a registry type, which is a I think it is right here.
Trent Mick 00:25:36 Just, yeah, click it again.
Matt Wear 00:25:38 Yeah, no.
Trent Mick 00:25:39 I broke the table contents.
Matt Wear 00:25:41 So it's just the NPM package name to a kind of factory that gives you an instrumentation. It's just a function that returns an instrumentation.
And my thought was that we would just update, like, Auto Instrumentation's node to have, like, a Git registry function that kind of returns all the instrumentation in this format. And the other reason for this format is that for declarative config like We can't support, like, function-valued configuration options, like, you know, hooks.
But you can still provide them, in your, in your factory, and then we will kind of layer the declarative config over that, so it's still kind of, it still works. It just… for anything that's function-valued, it's gonna have to be in code. That's one of the… One of the, kind of, I I guess.
caveats to to things.
So… so that's what we're doing here. We're setting up the config provider, and then I have this resolve instrumentations, which, basically enforces that you only pass in either of the registry or the instrumentations, not not both. And then we'll figure out which ones are enabled. And then return a list of enabled instrumentations.
And then, I was gonna move on and Just show you what this looks like from the instrumentation's perspective.
So I updated Http to use this.
And, so basically, in the constructor, I added this utility function, which I'll talk about a little bit more, but, Mainly, you're just kind of mapping, your, the config of the instrumentation to the declarative config keys, and we're using this, It's config properties, and config properties, it has these kind of typed accessors to, Retrieve these properties from the, From the config, it will warn you if, the… Type of the property was… that was provided was the wrong type.
It will never fail, it'll just return undefined if, Worst case scenario. If there's nothing there and Oh.
And then… yeah, so this is kind of what it looks like from the instrumentation perspective, and then this Apply Declarative Config, look at that, because it's kind of… it's doing some, it's doing some Hold on.
some things behind the scenes that are nice. It's actually you pass in this read function, and then it will yield the config properties for own, which is the instrumentation itself, and then general. So you can get access to both of those. So it's kind of doing the work of Getting those from the provider, And then it's calling that read function, and as I mentioned, like, a lot of things will come back, or they will come back undefined if the property was didn't exist, or if If it was the wrong type, so then we could kind of filter out all the things that were undefined.
and then we set the config, and then The config properties actually tracks all the properties that were read by the instrumentation, and we could compare that with the properties that were passed in. And if there were any properties that were passed in that were not read by the instrumentation, those are invalid in some way. It's like a typo, or they're just not supported.
So we we warn on those that there was, you know, properties that we didn't understand, and they were not applied.
So, there's that. And then I think the rest of this should go pretty quickly. There's API config, it's a new package, and that is the thing that, holds like the config provider kind of the no op implementation. And then the config properties.
interfaces. It has an implementation which doubles as the no op implementation. We pass in just like an empty block to it, and it becomes like a no op implementation.
And then in the configuration package, there's just kind of like the glue that is actually like the operational config provider.
and Yeah, I've been talking a lot. I think I've introduced mainly what I have to introduce any Questions, comments, concerns about things thus far.
Trent Mick 00:30:55 I think, well, as I said, I'll look in more detail. Mostly, I like where this is going, so I think… Alright.
Yeah, I think mostly this is good, but I mean I'll I'll go through it with a Or the finer cone.
Matt Wear 00:31:10 Cool, awesome. Yeah. So if anybody wants to review this as is, if this is a reasonable size. Pr, let's just go with that. If people would like it broken up, let me know and.
Trent Mick 00:31:21 So the… okay, yeah, the only… I think the main part of friction that I'm gonna have is anything touching the… instrumentation interface.
Which… is long term problematic.
the… Well, yeah, I'll see if there's some alternative to propose, or something like that. But, like, whether I guess what I'll Drive forward and reviews to see if I can.
have a reasonable alternative proposal for having the Separate Instrumentations Factory thing. I think it's an array of factories, I assume, or it's a mapping of factories or something.
And instead of… to see if… I don't know if this will work out well, but to see if… the… interface to instrumentations could be that they only access the Config provider when they're enabled, rather than when They're created.
I think one of the problems, and, like, you haven't been around for the history of this in OTelJS, but I think one of the pain points in the instrumentation interface is that too much stuff is done in construction. So, like, the… Changing that might be difficult, though, because that would effectively be a breaking change. So, for example, the instrumentations that use require in the middle or import in the middle to do monkey patching, they are doing their thing when they're constructed, instead of when in my preference, and I think it would solve some problems, is if that doing their thing was only happened when they were enabled, when register instrumentations was called from the instrumentation package. But, anyway, that's not something that this PR… Should have had to deal with, but, like, obviously you ran into that, so… Anyway, I'll see if there's a potential proposal there.
Matt Wear 00:33:14 It's a funny thing that you mentioned this because like my original implementation.
Did not have a factory, and, like, I kind of… thought that I didn't like that, and I want, and it will.
and I was applying the config at enable time.
so, that is a viable option. It does require, like, adding a method to was actually called apply declarative, apply declarative config on on instrumentation itself, and it looks a lot like the one that I currently have. So it is possible to move those around, and I still… I think I have my… I think I have a branch, a backup branch of what that looked like, so I can, like.
I can either paste that on on the Pr. If you want to look at what this looked like without the factory, just as a as another option. But yeah, this is like an iteration beyond that one. So.
Trent Mick 00:34:23 OK, if you have a link to that branch, maybe you can throw that on the PR comment or something. You don't need to go set up anything more than that. But yeah, if — yeah.
Matt Wear 00:34:34 I will turn this over.
to.
Trent Mick 00:34:39 Yeah, Mark, Dan, I don't know, or others, if you had other comments on.
structure there, or…
Marc Pichler (Dynatrace) 00:34:44 I have one question around returning the instrumentation.
Umm.
From… from that factory, I'm wondering if we even need to do that?
Because I suppose what happens once the instrumentation is returned, we then register it at some point.
Umm.
I'm wondering if, instead of… Returning the instrumentation itself, we just register it immediately and return void.
Umm.
Because if we're… if we know we're gonna register it anyway… Then it kind of leaves, or it leaves the shape of the instrumentation open.
It doesn't have to adhere to the instrumentation interface. It just needs to be something that instruments, right?
Umm.
And by configuring it, you're saying, I want to have this.
Instrumentation enabled and registered, and all of that.
Matt Wear 00:35:46 Yeah, I mean, all of this was to be able to kind of move up applying declarative config into the constructor, kind of like the way it works.
the way it was kind of working the way that S. That start Sdk node already works.
Which is… It, you know, it receives already, you know, a list of instrumentation that has been constructed, and then, there's still this possibility that some have been disabled. So I think there's like some checking to kind of prune the list to what actually, this user wants to use. And then that ends up being what's registered, I guess.
So, it's totally possible to push this to to enable time and and use constructed instances, which is what I was saying. I I have a branch where where that actually already happens and can can show that. But.
Marc Pichler (Dynatrace) 00:36:50 Yeah, so what I meant was actually not pushing it to a neighbor time, but Still taking the non-constructed factory things.
And… Instead of, Instead of, like, doing it on enable time, still, like, configure it through the constructor, but then just enable it, like, immediately, so that it doesn't need to be registered with this register, instrumentations thing.
Because if we don't need to take that instrumentation later and register it, there's no need to return the instrumentation interface, and there's also no need for, the factory to know that it's configuring an instrumentation. It's just saying.
You're configuring that go, and then it does it, and everything's set up already after that.
Matt Wear 00:37:51 Got it, so you're talking about a Avoid, that refunction, more or less.
Marc Pichler (Dynatrace) 00:37:57 Yes.
Matt Wear 00:37:57 Everything up.
Marc Pichler (Dynatrace) 00:37:59 Because if we don't need what's coming out of there, there's no point in holding onto it, and then we have less API surface to deal with.
Matt Wear 00:38:08 Yeah, that's… Ryan Miller, That's something that we can look into if if we want to keep the factories in the 1st place, because it sounds like maybe those are questionable.
Trent Mick 00:38:21 I may be missing something, but don't we still need the reference to the instrumentations in the SDK? That's the thing that calls set tracer provider, set meter provider, et cetera, on each of the instrumentations.
To the providers that were just created by the SDK.
Marc Pichler (Dynatrace) 00:38:39 I'm.
You're right.
Though, I would say… Umm.
The only important thing is set meter provider, because logger and trace are both proxying implementations right now.
Trent Mick 00:39:03 Oh, no, they have to get it somewhere. There's not… Well, I thought there was a thing in the spec saying that instrumentations… should use a given tracer, or given provider, tracer provider, other ones.
but can fall back to the globally registered one. Like, if you don't set that on Eastern Instrumentation, you're basically baking in the assumption that we're always using the global, which is maybe fine, I think the spec may allow that, so I don't know.
Marc Pichler (Dynatrace) 00:39:27 I'm not even sure if the spec says anything about instrumentations in particular.
Daniel Dyla (Dynatrace) 00:39:35 I think if you're using the config to… The global one is… Kind of the assumption, right?
Trent Mick 00:39:47 Thank you.
Daniel Dyla (Dynatrace) 00:39:48 There's no way, as far as I know, in the declarative config to configure a different one.
Marc Pichler (Dynatrace) 00:39:55 Yeah, I think there's no way… there might be, like, some sort of, like, reconfiguration thing coming down the pipeline via OpAmp.
Umm.
Trent Mick 00:40:06 That's the policy work. Yeah.
Marc Pichler (Dynatrace) 00:40:08 Oh.
But one of the things that we could do to work around that is we could pass in an event emitter that just emits, like… I don't know Oh.
change… Tracer provider, change meter provider, event.
That the instrumentation can then subscribe to, and the thing would just forward that to set meter provider, set tracer provider.
So you would get… A similar, You would get similar functionality via that.
Would be up to the instrumentation to subscribe to it, though.
Daniel Dyla (Dynatrace) 00:40:50 I'm about to increment my diagnostic channel counter.
Trent Mick 00:40:59 And then there's like browser support too.
But I don't know if we talked about This shim.
That. Yeah. Just waving. Yeah.
Daniel Dyla (Dynatrace) 00:41:07 Yeah. I mean, for… is… Declarative config… Relevant.
For the browser?
Trent Mick 00:41:16 I think probably not.
Daniel Dyla (Dynatrace) 00:41:19 It might be.
Trent Mick 00:41:20 Browser SDK stuff that they're working on, they're doing like SDK config stuff, but I don't see them discussing. I could ask Jared straight up, but there's no way they're gonna put a YAML parser in the browser. So from YAML, not maybe using the config types.
Daniel Dyla (Dynatrace) 00:41:37 Maybe using the config types and maybe, a build time.
Yeah. Configurator.
Trent Mick 00:41:45 Right, that puts it into a plain old JavaScript object, I mean, or from Yamo. Yeah, that's possible.
If so, then the config provider stuff in the API is relevant to the browser. So need to think about that.
Yeah.
Daniel Dyla (Dynatrace) 00:42:03 Well, it's The build time stuff would all run in Node, anyway.
Marc Pichler (Dynatrace) 00:42:10 Yeah, I wonder if at build time you would also… Just select which packages you need based on… Based on what's configured. So you would, for example, not even include, praise SDK if all you're emitting is events. You wouldn't…
Daniel Dyla (Dynatrace) 00:42:32 100% you would do something like that. I think we're, we don't need to talk too much about it because it's a maybe they will eventually do this. It's not like something they're working on right now, but.
Trent Mick 00:42:42 I think they are the… Fledgling not yet published, but has commits to it. Browser SDK.
thing.
has mechanisms to try to do that. So you can… East me, I'll get each of the signals.
so that you can, like, totally exclude all the tracer stuff if you're not doing… Spans.
Sorry, I'm not even sure if that's what you're asking.
Matt Wear 00:43:22 Anything else.
Marc Pichler (Dynatrace) 00:43:22 So I guess we went off topic here for a bit.
One thing that I also was wondering about is, How does that interact with the component provider?
specification.
Because it seems it does something somewhat similar.
In terms of it creates the instrumentations themselves, and the component providers just create plugin interfaces.
Umm.
So I'm wondering if the mechanism for that should be the same in the in the future.
so that instrumentations are just another component provider that's being registered, which would then also have an influence on the shape of the factory that's being used to construct that instrumentation.
Trent Mick 00:44:16 So… I might be wrong here, but my impression is that instrumentations are not SDK components. Yeah. So, the original plugin component provider thing was not… a component did not include instrumentation, so they… they basically didn't overlap. That said, I think my guess is the Java extension system which… provides plugin components.
or component providers, can also provide instrumentations, I'm guessing. I don't know that for sure, though. So, I… I think there may be mostly orthogonal, but I'm not sure.
Marc Pichler (Dynatrace) 00:45:03 Yeah, so the reason why I'm asking is, If we're gonna move forward with, having… Instrumentations… B.
Provided by… Some mechanism, And then we're gonna have plugins provided by some mechanism. It would be good to, like, consolidate these early.
Umm.
To make sure that for a user.
Or for somebody developing these, it's a similar way of like, providing these.
And for a user, it's a similar way of registering these.
what I've seen in the past is that users usually don't make a lot of distinction between instrumentations and plugin components. They see these as, like, or part of, like, the SDK.
Yep.
So… Having them registered through a similar.
Interface and through a similar mechanism would make sense, in my opinion.
Trent Mick 00:46:12 Remind me again what the mechanism was in your.
POC.
Marc Pichler (Dynatrace) 00:46:18 It was just providing the providers through the create method. So it was just passing a list of these, to the create method, and then create would go in and just apply these Umm.
The, the coffee.
Trent Mick 00:46:34 Okay, so we… you hadn't gotten to the point of defining how… Somewhere.
Marc Pichler (Dynatrace) 00:46:40 How d.
Trent Mick 00:46:40 Provide an alternative.
Like…
Marc Pichler (Dynatrace) 00:46:44 Yeah, I haven't gone through the process of having someone provide something different.
but what even that would allow you already to do is to have, like, one JavaScript file where you just say, like, you're creating an… an area of component providers.
And that's what's being used by Create.
So if you don't need a bunch of stuff, you don't need to include it And then build, essentially, distros from it, which would be interesting for a contrip.
Umm.
And, like, actually providing a contrib and a core distro.
Where we… From core, just include what's in core, and in contrip, just include what's in contrip.
And then third parties can build on top of that as well if they want.
Trent Mick 00:47:56 Thanks, man.
Matt Wear 00:47:58 Yeah, no problem.
Marc Pichler (Dynatrace) 00:48:01 Yeah, thanks for.
Working on that. I'll also try to have a look. It looks… Very interesting, the whore.
like, adding another API is, I don't know, I didn't read that much into the configuration spec to, To see that yet, so that's interesting.
Trent Mick 00:48:29 for me, the thing that gave me the history is when you're following some of the issues that Jackbird was… mostly Jackbird was doing for the declarative config stuff, and then it got to a point, there's one comment and one Java issue that said, well, we have all this infrastructure for configuring or for users to provide YAML configuration for SDK components.
it would be a shame to not reuse some of that for configuring instrumentations. And then the config provider Part of the spec was born.
100% from that comment. And so it's like there's this YAML and there's structure for doing all these things. And then they just like added this side thing for instrumentations and it's a wide open spec. And we have to provide some way that instrumentations can do it without taking a dependency on SDK components. So it has to be an API config provider.
Marc Pichler (Dynatrace) 00:49:19 Right, Yeah, it makes sense, actually, because one of the things that I was concerned about was also having everything in the configuration package would mean that, like, if you want to provide configuration from your instrumentation, you would have to depend on that package, and that package might get larger and larger over time. It's more and more Config options are added.
Umm.
Trent Mick 00:49:44 Right, and so this is supposed to break that so that you don't have, yeah, so none of these, no types for instrumentation stuff will live in the configuration package. It's just… Right. And in fact, this, this generic config properties thing, which is meant to be like a node in the parse. Yaml configuration, I guess, can live in the Api, or maybe you have it.
living in the instrumentation package here. Maybe that makes sense, too.
Yes.
So, yeah, there's nothing here that's going to add another STK dependency on instrumentations. They still only need… dependency instrumentation package. And I know, I think we've talked about it, maybe even breaking that.
Limitations so that there's just an interface.
And no actual runtime code in instrumentations that an instrumentation needs to depend on.
But anyway, that's… Maybe that's future work.
Marc Pichler (Dynatrace) 00:50:44 Alright.
That was, I think, the last topic for today.
Anything… else we want to talk about.
Trent Mick 00:51:06 Are we gonna try to stabilize logs before SK 3.0 or as part of 3.0?
Marc Pichler (Dynatrace) 00:51:12 I think at least as part of 3.0 would be, Good.
timeline to look into Having, like, a new feature with 3.0, It's always helpful to get people to migrate.
Sdk logs would be a perfect… Thing to do it with.
That also gives us some… extra stuff to do until SDK 3.0 work starts.
I haven't done a lot of, work on that recently.
We can have a look at the… I'll just share my screen real quick, we can have a look at the milestone and see what's missing.
Trent Mick 00:51:59 I think I have to get back on the any value.
Marc Pichler (Dynatrace) 00:52:05 Yeah, it's the trickiest one
Trent Mick 00:52:16 It's on the left side for now.
Marc Pichler (Dynatrace) 00:52:21 We have this any value thing that we just talked about.
Umm.
I looked into this one.
And… looks that everything here is, properly marked as experimental. I guess one of the things that we can discuss is if we wanna have, like, an experimental entry point for these things.
Or if we're fine with just experimental annotations on it.
Umm.
I think in the past, in other SDKs, we've just done experimental annotations in the JS doc, and We barely ever have to change anything.
Daniel Dyla (Dynatrace) 00:53:08 It hasn't been a massive problem.
Marc Pichler (Dynatrace) 00:53:11 Yep.
So I would be inclined to just go with the annotations for this one as well.
Trent Mick 00:53:18 Sounds good to me.
Marc Pichler (Dynatrace) 00:53:22 Then I can write up a comment here, to say that the annotations is what we're going for. One person came back here saying that the README might not specify it properly yet.
So that's also something… We can, we can update, just state in the README that these features are experimental, and then… We can move on.
For that one.
Renaming the SDK log record, I guess we could put an up for grabs label on that one.
And see if somebody comes around to pick it up.
I see.
Trent Mick 00:54:15 In minutes, yes.
Marc Pichler (Dynatrace) 00:54:23 I guess, for to start with, we would also want to have a type alias that's deprecated still right, so that not everybody is broken immediately.
And then we remove that in a future version, or should we just go for the break?
Trent Mick 00:54:39 I mean, I guess so.
The log record processors API change that I did, that just broke everyone immediately.
And the last one, so… Either we go for it, or… we data type alias, and I should feel bad for breaking people last time.
Marc Pichler (Dynatrace) 00:55:02 I think both are.
fine. It's experimental for a reason, right? So…
Trent Mick 00:55:10 Oh, I thought you were saying I should feel bad and we should do.
Marc Pichler (Dynatrace) 00:55:12 No, no, no, that was not what I was saying.
if it helps, I always feel bad.
Trent Mick 00:55:22 All the time.
Marc Pichler (Dynatrace) 00:55:24 Yeah, for breaking stuff, making breaking changes.
Okay.
But…
Trent Mick 00:55:32 Finally, Ving, as says, you don't have to add it on.
Marc Pichler (Dynatrace) 00:55:36 Okay.
Trent Mick 00:55:37 It's there.
Marc Pichler (Dynatrace) 00:55:42 then We also have this one here.
Looks like somebody already… devise the plan. Should we just tell them to go ahead and do it?
Marylia Gutierrez 00:56:15 I would just, like, double check what their actual plan, because this just… looks very AI generated.
Yeah. And I was.
Marc Pichler (Dynatrace) 00:56:24 I think that's one of these that, is very easily AI, implemented, though.
I would guess AI could one-shot this.
Trent Mick 00:56:40 But the existing thing is also already, okay, setters for everything.
Marc Pichler (Dynatrace) 00:56:46 Yeah, so… I will actually just, ask them to go ahead, I will deal with the review, so, You don't have to bother with it in case it goes wrong.
Daniel Dyla (Dynatrace) 00:57:04 You should approve like they're an AI to say like approve and accept edits.
Marc Pichler (Dynatrace) 00:57:44 Okay.
all right. And then we have this audit logs. Api extensibility and compatibility issue here.
Then just disappeared.
From the call, I think.
Marylia Gutierrez 00:58:11 Yeah, I was going to say very convenient, like, oh, you're open mind. Oh, I have to drop.
Marc Pichler (Dynatrace) 00:58:23 Yeah.
So.
the actual logs API is fairly minimal. I think it wouldn't be prone to the same issues that we've had with the other APIs, because For the logs API, we really just have to emit method.
Trent Mick 00:58:44 And it's already an object, right? Instead of taking… Number.
Marc Pichler (Dynatrace) 00:58:48 Yeah, yeah, it's always.
Trent Mick 00:58:49 Thank you.
Marc Pichler (Dynatrace) 00:58:50 Yeah, it's always taking options, so.
There's not that much that can go wrong.
Trent Mick 00:59:03 He says.
Marc Pichler (Dynatrace) 00:59:05 Yeah, it's, We still have the recording for that meeting, so somebody will clip me and send it to me.
Trent Mick 00:59:12 Not in a month.
Marc Pichler (Dynatrace) 00:59:18 Umm.
There's 1 thing that says emit emit events instead of calling Sdk functions.
Umm.
Trent Mick 00:59:41 This is background when he was more actively working on the API POC, right?
Marc Pichler (Dynatrace) 00:59:53 Yeah, this would be a fairly large change.
So I'm not sure if,
Trent Mick 01:00:02 Maybe put an agenda item for next week and we can… Ask Dan if this is something I want to push off this GA.
Marc Pichler (Dynatrace) 01:00:08 That's a good idea.
Trent Mick 01:00:09 Question.
Thanks, Matt, for bearing. I know you came just for the one PR, but you're still sticking out the whole meeting.
Matt Wear 01:00:27 No, I'm.
I'm here for the full meeting. There might be other interesting things that come up other things I can help with. So.
Marc Pichler (Dynatrace) 01:00:39 All right. Speaking of the full meeting.
That's it for today.
Thank you everybody for joining. Have a nice weekend, see you next week.
Marylia Gutierrez 01:00:50 And Marc, I just added the custom message to the first PR, like the change log. Let me know if that's what you had in mind I added there now.
Marc Pichler (Dynatrace) 01:00:59 I'll have a look. Thank you.
Marylia Gutierrez 01:01:01 Cool, thanks.
Marc Pichler (Dynatrace) 01:01:03 Thanks, bye.
Marylia Gutierrez 01:01:03 Bye.
