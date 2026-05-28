SIG: JavaScript SIG
Date: 2026-05-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:00:42 Hello?
Trent Mick 00:00:59 Hello.
Marc Pichler (Dynatrace) 00:01:32 It looks like not that many topics on the agenda today.
First topic here, perhaps chat about this PR, which I said I was going to review, but I didn't. Sorry, David.
I went through these files, but didn't go to these yet, so… This here says, get about, SDK trace stunts in FOS.
Trent Mick 00:02:36 So that's… I mean, there are a few issues on this one, but this is work to… I was gonna say Titan 3.0 kinda is, but only if we need breaking changes there, which I guess we do.
But to… Yeah, because I've been working on the… declarative config stuff, and ran into a step where I… I… need this work, because I want… Like, the create step.
given a config that doesn't specify any of these things, I want to be able to call or the, SDK that's creating the SDK components from the config that doesn't specify these things needs to be able to create a tracer provider and have it not look up stuff in the environment, so we need this.
tracer provider and the batch fan processor, which isn't covered by this PRS. I've been adding comments to the bottom of this PR review.
About whether we need to do… A bit more work there. Because, like, this lookup stuff in the environment is… That's… Tendrils deep into this package, so… Anyway, I think the PR is going fine, the way it is. So I guess, maybe it's just… just reiterating for you and David, but… The plan is to provide environment variable free… things in SDK Trace Base, and then eventually rename that package to SDK Trace as part of the 3.0 breaking change, is that the plan?
Marc Pichler (Dynatrace) 00:04:12 Yeah, that's, the idea, essentially giving people a way to move over to a new, way of doing things before going to 3.0, so we can deprecate the basic tracer provider and have just the tracer provider from there.
And then just rename the package, so it should be a bit easier for people to migrate there.
If they have to, and they're not using Node SDK or anything like that before already.
Trent Mick 00:04:41 Would we drop all the nth stuff when we do the rename, or we could do that later, I guess?
But that is the breaking change dropping things, I guess. Or maybe renaming the package. Anyway, yeah. Done.
Marc Pichler (Dynatrace) 00:04:52 Yeah, so, renaming the package, I think the breaking change would be discontinuing the old ones, and whatever functionality they provided extra on top of the, like, new base, implementation, which is just a trace SDK without any MVAR stuff.
So, yeah. What we can do is, even if we don't get that into 3.0, or if we want to do that in 2.0, we can also already introduce an SDK trace package.
that SDK trace base then uses.
So, this way, we wouldn't be able to… we wouldn't need to remove anything, at all, immediately. It just keeps existing and, is… A feature-freeze package.
And then we removed that eventually.
Trent Mick 00:05:52 So I agree we could do that. One of the things I was trying to think through is maintaining the git history for the interesting bits in there. So, like, renaming basic tracerProvider.ts to tracerProvider.ts, because that's where some of the interesting implementation is.
But if we were to create a new SDK trace package and still have the SK Trace base package, then that gets to be a little bit harder, unless you're… Playing weird games, so, okay.
That was… maintaining that history was the main reason I was… So far, preferring… working on the STA Trace Base Package to add this new non-environment functionality, and then eventually removing that from the package, so then the history is still there. But yeah. I don't know if it's going to require more… excising of, stuff in there. So, like, David, what you have right now is a tracer provider.
can be… created that doesn't use the environment, but when it creates a tracer, it's still… it's still looking up things in the environment. When it's doing a merge config, it's just the tracer provider passes in all of the things, so the environment variable reading that's done doesn't actually get used. You can still get warnings about reading bogus environment variables, so there's some things in there. And then the batch band processor still reads stuff from the environment.
So we'd want to have an environment-free one in there.
let me know if you don't have the bandwidth to be working on this, because I can definitely work on this stuff, too, because it's… One of the things I'm doing on declarative config work is hitting wanting this. So, at least one thing that I want to do for declarative config will get blocked on this, so I'm happy to work on it, too.
I think maybe that's… That's…
David Luna Bistuer 00:07:42 Yeah, I think I can allocate some time, during today.
I've seen that, Tracer, the class… tracer class is not even exported from the package, so I think it's safe to just remove one. We are, as you said, in the tracer provider, we are already resolving.
All the defaults on configuration, so… Yeah, we can just remove, just drop that.
Or we can't.
Trent Mick 00:08:06 drop it, we still need it internally, it's not exported, but you could… we could change the internals for it to require all of its pieces, but then maybe you need two separate tracer… classes, one that's still used by the environment variable using basic tracer provider, and one that's used by whatever. Another pain in the ass thing is that new tracer is used all over in the tests, even though the tracer class is never exported, and all the tests don't pass in all the things, so they're relying on the environment verbal reading, so it just means more work.
David Luna Bistuer 00:08:42 Okay.
Marc Pichler (Dynatrace) 00:08:43 The reason why that's the case is because Tracer used to be exported, and we removed it in Tudor, I think. Right. So… There's a lot of history behind that one, but probably one way to go about it could also be to just in-check the config into the constructor of the tracer, and then overwrite the tracer creation on the basic tracer provider.
To use that.
Instead.
Bali.
But then I don't think they would share a lot of… common cold anymore, which…
Trent Mick 00:09:25 then it's a judgment call, I guess, you can do whatever.
Either way will work, whether they're separate or… One sharing implementation, yeah. I've been thinking about a static… Method on the class for… one of the guys to use instead of the constructor. Get the constructor to take everything, and then have a static method for from environment variables, and that's the one that basic provider.
uses. That, or… Just have a separate function that we can then just drop later that gathers all from the environment variables, yeah.
Alright. Great.
Marc Pichler (Dynatrace) 00:10:01 Yep.
I think it would be good to have that, sorted out and everything aligned, so… A source of confusion sometimes for us developing, but I don't think a lot of users actually run into that, confusing behavior. I've never, or not often heard people ask for mvarconfig, like, the trace package has in metrics or in, in logs, so… I think moving on from that is probably gonna be a good thing.
Trent Mick 00:10:40 Yep.
Marc Pichler (Dynatrace) 00:10:45 Right.
Any more thoughts or questions or anything about this?
If not, then let's move on to the next one.
Yeah, that's my UC on the thing. Thank you, Trent, for reviewing that one.
Trent Mick 00:11:10 Yeah, so I've had a look. I like the basic layout. As I say there at the top, I'm a good call on not exposing the mechanism yet, so we can still feel it out, how we want to… expose that. If you scroll down to my third comment, just to plant a seed, maybe, or bottom… the last comment that I made in review, I think.
That's where I say I'm dreaming right at the end.
Marc Pichler (Dynatrace) 00:11:32 Yeah. I do wonder…
Trent Mick 00:11:34 Go ahead.
Marc Pichler (Dynatrace) 00:11:35 This is what I was kind of thinking of as well, when coming up with that, that this could be one of the things that we can do in the future.
Trent Mick 00:11:46 Just to have… oh, the interface component provider? Yeah.
Marc Pichler (Dynatrace) 00:11:49 Yeah, the last… thing on there.
One of the, issues with this flat array that I ran into is getting types to work properly. It's kind of annoying with that.
Okay. I was playing around with different ways of, forcing the… forcing this relationship here, the name and… I don't know, what was it? The component type and… Create component.
Because one of the things that people can do is they can just create a component provider for whatever thing that doesn't really exist yet.
I wanted to lock that down for them, so, only things… That are actually supported can be created by people.
Because otherwise they're just passing it in to create, and it doesn't really… help them with anything, it's just a know-op. And once we later on decide to add something, then it might break, because we just assume now that this this component type uses… Or returns this sort of plugin, but it doesn't.
Yeah, that makes sense.
Trent Mick 00:13:12 sense. If it's… Yeah, yeah, if that ends up being too much of a pain in the ass, then we wouldn't have to go that way. Component type could maybe be an enum.
set of well-known. I don't know if that would defend against that, or if it's still.
Marc Pichler (Dynatrace) 00:13:25 boy.
Trent Mick 00:13:26 Yeah.
Marc Pichler (Dynatrace) 00:13:26 I had defined a type, where it was just enumerating all the different strings that it could be, and then it would map that to the actual type, down here.
It looked like crazy TypeScript, but, I think it would have been, it, would have been very difficult to extend later on. Again, as a similar issue that we have with attributes right now, where it's kind of unclear now what is a breaking change and what isn't.
and… I was just trying to, like, work around that issue from the beginning by having this map.
Because then there's a… Well-defined set of interfaces that people can implement.
They can't implement something that doesn't exist, and we can just still merge that down somehow internally, or handle it somehow internally, and still get proper types.
It's mostly TypeScript.
issue, for me. Or maybe I'm just not, thinking deeply enough about how to structure the TypeScript types for that.
Trent Mick 00:14:45 Okay.
Then, slightly separate thing, looking at the third code block that I have right down at the bottom, the YAML.
To plant a seed. This is me thinking out loud about what The eventual user-exposed mechanism for adding component providers might be. This is getting back to, like, the vaporware ideas for extensions.
Things like that, and how… Custom components will be provided.
Marc Pichler (Dynatrace) 00:15:12 Yeah.
Trent Mick 00:15:14 Presumably at some… I mean, there needs to be some user config way to specify these things, so this is throwing it into one of the… Open buckets in the declarative config schema right now, but… Yeah.
Marc Pichler (Dynatrace) 00:15:28 Yeah, I think that is a… is a good idea. The way that, like, this is also one of the things that I was thinking of, like, this… entry point, or, just… An entry point with one function that we can call, and then we get a bunch of component providers, or, like, the component provider map and pass it in there, would be really helpful for doing stuff like that.
And it also would… Allow us to… do something similar to what Java is doing right now with, like, for example, when you use the auto operator and you use the Java auto-instrumentation provided by the auto operator, you can just build your own image, which has a bunch of extra stuff.
In there, and you want it to load, and then you can just specify that image somehow, and have the… auto-instrumentation stuff loaded, which I think is… is really helpful also.
To grow the ecosystem in the future without having to have everything in Contrip.
Right.
Because then people can do stuff like… What you're showing here, and just have one metapackage that just bundles whatever they need.
or… Company could, have their extensions.
In that, sort of format.
And load them this way.
One thing that comes to mind was, I think, the, escher, folks.
were asking for a few components in Contra, because they wanted to deliver it via the auto-instrumentations node package.
And… If this… would actually be possible, then this is really just a config setup, and you need to get the package somewhere.
And then you're all set.
And, yeah.
everybody can maintain their own set of extra instrumentations or whatever.
Outside of the country people, which would be nice.
Trent Mick 00:17:49 Yes, agreed. The big, kind of, gorilla for me, or elephant in the room, or whatever, that I don't ever see… getting a satisfactory answer is the declarative config stuff is originally just about SDK components, and SDK components are separate from instrumentations, and how instrumentations fit into either this… component providers, they don't. They're not listed as SDK components, or into whatever the extension mechanism here that we're defining. And also, how selecting which instrumentations to enable via declarative config, all that stuff is not clear to me at all, because it's not really… A place where that's well-defined.
I mean, at some point, we need to have… or presumably, we want to have an answer for the environment variable OTL node… enabled instrumentations and disabled instrumentations, and have a choice on how those get selected in declarative config, but we don't have a spelling for that yet.
It's kind of a few ideas that are related, but how instrumentations fit in here isn't clear yet.
Marc Pichler (Dynatrace) 00:19:03 Actually.
Trent Mick 00:19:04 Unless it is to some of you.
Good, please.
Marc Pichler (Dynatrace) 00:19:08 Isn't the… Instrumentation schema, the one that would be used for configuring that stuff?
Trent Mick 00:19:20 Yes, but that's a in-development catch-all.
Marc Pichler (Dynatrace) 00:19:24 Just chemo.
Trent Mick 00:19:24 section of the thing that was glommed on to the end.
there's the config provider thing, which is a little bit of a nod to… so, I mean, okay, so declarative config… here's my understanding of the history. Declarative config… was… the idea was started for how to configure the SDK.
And then… there was this one ticket that I found where someone said, oh, well, we're defining all this infrastructure for defining config, it would be… nice to provide some way to configure instrumentations as well. So, this instrumentation slash development schema-less node was plopped onto the end, and this idea of a config provider that's added to the API was added, so that declarative config can be loaded.
And the config provider and the API can be used by instrumentations to get access to that instrumentation node in the config schema. But beyond that, nothing's really been defined. And of course, it's language-specific, so there's only so much that can be done.
At the spec level there. But, Yeah, there's that general section at the top, which is trying to generalize some… Some… some pieces, but the rest of it's just language-specific, so… Out of any real guidance.
Marc Pichler (Dynatrace) 00:20:38 Which I guess… Could be fine for us to experiment in that place, then.
Yeah, one of the downsides, of course, is that people will start using that and rely on it being, Not changing, and, it's staying the way that it is.
Oh.
Trent Mick 00:21:03 If we define some behavior in there, you mean?
Marc Pichler (Dynatrace) 00:21:05 Yeah,
Trent Mick 00:21:09 So, yeah, it's something we need to… Default behavior I see on the JS thing, hovering line 43.
Instrumentation defaults are used, yeah. What are our defaults?
I guess… I guess our current default thing is, like, everything that's in AutoInstitation node, except for the small set that we do not enable by default, like FS and now host metrics.
Which is similar to what Java has, I think, in the world. So if you use the Java agent, you get… All of the instrumentation's enabled, except for a couple notable painful ones.
I don't know, so maybe there's some, basically, prior art on how the environment variables work that go in there, but we do need to define that.
Vertical, okay, okay.
Marc Pichler (Dynatrace) 00:21:55 Yeah, agree.
Trent Mick 00:21:59 Okay, anyway, sorry, that's just me.
Talking about vaporware.
Thanks, but the… thanks for that POC. It's a good start.
Marc Pichler (Dynatrace) 00:22:10 I tried to, look into the comments, and we'll try to address those, over the next week, maybe I can mark that as ready for review soon, so we can… Start experimenting with some of the other plugin components as well.
And I'll also read up on the instrumentation stuff, maybe I can… read between the lines somewhere. Figure some stuff out.
Alright.
Moving on to TikTok, yeah, we talked about this a few times already, Looks like this is already approved, so I would be… inclined to merge that in, looks like.
That probably just failed on… startup. I'm actually wondering if we should, wrap that in, like, a retry thing, because I see that failing due to network errors.
more often than I would like. I guess also because we run it That often, it just happens sometimes. This, start thing fails.
Maybe that's something that we could, try here, or just rerun that, and once it's done, we can merge it in.
Required back to, so I could probably just, Enable auto-merge, and then we should be good to go.
Trent Mick 00:24:07 I'm sorry if I missed it, you're talking about that.
Starting the services being flaky.
Marc Pichler (Dynatrace) 00:24:13 Yeah, starting with services and also, the NPMCI.
Stuff.
is also failing sometimes, due to network errors, because it can't get one package, and then one has to restart. I feel like it's more… happening more often on call drip than core.
Trent Mick 00:24:35 The trip's way bigger, yeah.
Marc Pichler (Dynatrace) 00:24:39 And there's… I think there's a few steps that we could wrap in a retry that would, Improved the experience a bit.
In the core repo, it's the lint.
workflow, which… on OpenTelemetry I.O. sometimes gets 500s, and I have not figured out why.
Trent Mick 00:25:01 I think… okay.
Okay, different issues. So, yes, if a reach… okay, so the services for hotel contrib.
For the contrib repo.
So I wonder if part of that is a side effect of us having moved away from using correct me if I'm wrong, David, but I think… I think you helped make this migration to move away from using GitHub Action services to just using a Docker Compose file, so that tests in and out of CI are using the same thing. I think that's still a good thing. If we can do a retry there, that sounds great. We should do that, because then you just get rid of the transient one-off things.
Going back to the other one, the lint step that's failing, the one that I found is almost always the issue is the docs test, and that's the thing that's checking all the links in all the docs. So every time you, like.
increment a Boolean, or increment an int in some piece of code somewhere, you're doing a DOS attack on OpenTelemetry.io as we check every link again.
Every time we do a lint step.
I think it would be nice… I have to look around, I don't know if anyone else has done this, but the similar kind of, things are happening in the other repo. So, like, in the semantic… inside the specs or the semantic convention repo, also have a link checker thing, and they're using a tool called Lychee. I'm not sure if we're using the same one. But you look at the Lychee config, and over time, it keeps adding exclusions to say, like, oh, 400 or 500 from this domain is fine, we'll just move on and ignore it. So basically, link checking isn't happening, it's just a… it's a… distributed DOS attack via GitHub on all of these websites.
I think it would be nice if we could find a way to only check links for files and even changes in that file that have changed, because there's no point in rechecking links for the old ones. Maybe you have a weekly thing that checks them all or something, but otherwise it's not worthwhile.
I'm not sure if people have seen other failures in the lint thing in Kintrip. I think it's always been that.
Marc Pichler (Dynatrace) 00:27:00 It's usually always that one, yeah.
Sometimes stuff happens that some site is down, and that's… Expected, but… OpenTelemetry one is the one that I've seen most of the time.
Failing for some reason.
And then I try again, and dude, it's back, so… There's no… Maybe it's even here, no.
Trent Mick 00:27:41 Did it happen there?
Marc Pichler (Dynatrace) 00:27:43 Oh, that's.
Trent Mick 00:27:44 I'll.
Marc Pichler (Dynatrace) 00:27:44 something else. I think that's, probably NPM reinstall.
Trent Mick 00:27:50 Test services. Okay, well, there we go. Okay.
Marc Pichler (Dynatrace) 00:28:08 Yeah, but I think moving the… the docs test out to just run weekly is probably fine.
broken links.
Happens from time to time in the docs, and… If we figure it out at most one week late, I don't think it will.
Like, be that painful to anybody.
Trent Mick 00:28:33 Yep.
Okay, so I had a couple to you, Sarah, I'll follow up on at least one of those.
Marc Pichler (Dynatrace) 00:28:39 Yeah, thanks for writing that down, that's fine.
All right.
Trent Mick 00:28:46 So, yeah, this… we've been talking about doing SDK 3.0 in June. Well, it's due next week. I don't think we're ready.
Maybe we should look at that. Yeah.
We should.
Marc Pichler (Dynatrace) 00:28:56 optimized.
Trent Mick 00:28:57 milestone.
Marylia Gutierrez 00:28:58 the year, or do you just say June?
Trent Mick 00:29:02 No, you're right, this is not my first rodeo. I probably did not say the year.
Marc Pichler (Dynatrace) 00:29:10 Yes, we should probably look at the milestone, and we should probably also start with a few issues to just prepare for it.
there's a few things that we need to put in place before starting with 3DL, which is, releases from the… From a newly introduced 2.X branch, so that we can get bug fixes and security fixes out while we work on 3.0.
Okay.
And… Then, once that's done, we can also look into, adding a pre-release workflow for domain.
Ranj.
probably we don't need to do it in that order. We can also do the pre-release on the main branch and get that working first, and then introduce it to the next branch, and… little stuff clear Because the pre-releases, I guess we want to keep around after 3.x has released for anything that we want to try out.
I think it would be helpful to just have one more box in the release PR creation workflow that just says.
Do this as a pre-release.
And then… We can continue iterating on that to maybe do, Pre-releases automatically halfway through, our two-week release cycle or something.
Trent Mick 00:30:54 Okay.
On the, the various release scripts and things for the… Or repo.
You know that stuff best, Mark. Is that… do you think it's pretty easy to add what you're asking to that stuff, or are you at a point in those scripts where you're ready to flip the table?
Marc Pichler (Dynatrace) 00:31:13 I moved most of these scripts from the NPM package JSON scripts to a JS file.
So, it should be fairly easy to add these sorts of things. One of the things that, might be a bit more difficult is, Making sure that all the… Like, making sure that the versioning works correctly, because some packages we carry it depend.
And I think those don't pull in pre-release versions, so we might end up with, like, half an updated, half an updated… repository, or, like, have an updated package, which just… like… for example, pulls in the trace SDK, and the core package is still held back at whatever Non-pre-release version we had.
So we need to figure that out somehow.
But once that's kind of figured out, I think it should be fairly easy to do.
We did pre-releases in… When we were going to 2.X, and that was just… Oh.
I think some extra tagging work.
That we needed to do.
When planning our publishing, we needed to make sure that it's not tagged as latest.
Alright.
But other than that, it's just juggling versions around, and making sure they end up in the correct place.
Which… yeah.
Should be fine, I guess.
Trent Mick 00:33:08 Okay, cool.
Marc Pichler (Dynatrace) 00:33:12 And…
Marylia Gutierrez 00:33:13 some of the, like, issues, like, for example, one of them that I can help out is that one that… what's the semantic convention, like, both for the database and HTTP that we have, we can change the default now? So, for example.
do we… because I can open a PR for that, but I can have it open and just wait for, actually, to merge when it's time, or it's going to be, like, on a different branch, or no? It's just gonna be… Straight to me.
Marc Pichler (Dynatrace) 00:33:42 on… The core repo, it's gonna be straight domain, so for the HTTP instrumentation, For the contrary pre-po, we'll need to come up with a plan how to do that, because right now.
we can't really do pre-releases in… in contrib.
And… We also need to make sure that we can continue releasing the… Previous version that, we had for security fixes and stuff like that.
I think the worst case would be to open a PR and leave it open, Because that just… Like, creates a bunch of conflicts, and is probably very painful for people to work on.
But we might have to do that, depending on whether we can figure out a strategy for contract or not.
Hmm.
Marylia Gutierrez 00:34:42 Okay.
Trent Mick 00:34:43 I think a potential is just wait until we're done the core 3.0 release, and then have a breaking, change, release, and all of the relevant instrumentations that drops the… The handling of the old semantic conventions.
Whether that's one or multiple PRs.
Yeah, I don't know, you can interpret it either way, we could just, like, you could go ahead and do it now, arguably. Six months later, and it's a breaking change, and… Theoretically, if we need to do… A patch release of… instrumentation PG.
that still has the old semantic conventions to fix a security issue, then we could manually try to do that, but practically, I don't expect that we're going to do that. We're just kind of always moving forward on instrumentation, so… Yeah, I don't know. Like, I think it's… I think… what I think is that this… these changes dropping the semantic convention stuff are mostly… orthogonal to doing a 3.0 release, breaking changes that we're doing, but it might be good and reasonable, maybe useful to do them at the same time so that the messaging… so if we write this, migrating to 3.0 document again, we can have a section there talking about the… the semantic conventions for HTTP and database.
Marylia Gutierrez 00:36:05 Yeah, because I wanted to do it at the same time, because I got, like, feedback from people, like, when are you changing the default? And I always reply, like, 3.0, 3.0.
Trent Mick 00:36:14 Right, so that's cool.
Marylia Gutierrez 00:36:15 Yeah, I can help, I can definitely do that, and I have the PRs, and whenever we think it's time to merge, we merge, or solve conflicts, I don't mind.
Trent Mick 00:36:26 Cool.
Marc Pichler (Dynatrace) 00:36:27 Yeah, one thing that I was just thinking about with these things is that we have Code already in place to turn that off, right?
So, to a user.
whether the code is there or not, doesn't really matter. What matters is that the behavior changes. That's the breaking change for them.
So what we can do with 3.0, is, once we're ready to do that, we just… change the config code to say, like, it just emits the stable stuff.
that change should be fairly small, and pretty much self-contained, and should be easy to do, like, one PR for all the instrumentations, right?
When Frida rose around, we merged that in.
People can't reconfigure it, and then afterwards, once we've released that, we can still go in and clean up all the extra code that's now not really used anymore.
So… That could be also one way to go about it without running into a bunch of conflicts and having a lot of work that has to be done in that short, 3.0 timeframe while still delivering to people, the change that they're expecting for 3DO.
Marylia Gutierrez 00:37:56 Because, yeah, the way that I'm thinking, like, I… maybe I'm just not thinking of the options, but I don't think we're gonna have, like, a lot of conflicts on this area, because I don't think, like.
our… things being done for the tweet at all, specifically, like, on the same files and stuff, so I don't think we have, like, any, like, big, actually, conflicts.
Marc Pichler (Dynatrace) 00:38:17 Yeah.
Marylia Gutierrez 00:38:18 So that is why I was thinking of just doing, instead of creating a bunch of.
Marc Pichler (Dynatrace) 00:38:22 Interesting.
Yeah, that makes sense.
Trent Mick 00:38:30 Yep.
Yep. I think you're right.
I don't think there'll be conflicts.
Marc Pichler (Dynatrace) 00:38:36 In that case, I think just opening the PRs and leaving them open until we're ready to merge them is probably a good idea.
Marylia Gutierrez 00:38:44 Nope.
Marc Pichler (Dynatrace) 00:38:45 It's the simplest of all the solutions as well, which I like.
Simple is good.
Trent Mick 00:38:55 I don't know if this is gonna show up properly.
No, it's not. I was gonna try to write a comment, but you can't do this.
Marc Pichler (Dynatrace) 00:39:06 So then we would probably also want to go through the backlog and make sure we add everything to the 3.0 milestone that we want to do in 3.0.
That's something that can also be done in parallel with the changes to the release.
Stuff.
There are a bunch of things, probably, in the backlog somewhere, that would be… would be nice to have for 3.0, and we would also want to have an issue announcing that 3.0 is coming, and if people have breaking changes, to bring them up.
As soon as possible, so that we can… Triage the issue and put it into the milestone.
Once we have that, we should be ready to… ready to go.
Trent Mick 00:40:07 to make sure I'm clear, we were planning on and hoping to do the logs, API SDK stabilization as part or before the 3-day.
Marc Pichler (Dynatrace) 00:40:17 Yeah.
Trent Mick 00:40:19 So the issues on that milestone are relevant, too.
Which I think is mostly waiting on me to do the POC using Widening attributes to the unknown?
Is that right? That's what we discussed a couple of weeks ago.
Okay.
I gotta stop.
Marc Pichler (Dynatrace) 00:40:40 Yeah.
Trent Mick 00:40:42 I just stopped playing with declarative config for a little while.
Marc Pichler (Dynatrace) 00:40:46 a clarity config is fun to… to play with. I, also enjoyed the POC PR that I did, so I understand.
Yeah, I think for the SDK… Logs, milestone, we have… Just these few left here.
As well as, documentation thing.
It'd be fairly quick to do.
I think it is mostly double-checking.
-Oh.
If everything's marked as experimental, it should be marked as experimental.
And the complicated stuff that we were talking about.
extensibility… .
Trent Mick 00:41:50 That's… that's just a meta issue for Carlos to work through.
Doing the audit.
Marc Pichler (Dynatrace) 00:41:58 Alright.
Yeah, the… integrating it, into the…
Hector Hernandez 00:42:05 Yeah, huh.
Marc Pichler (Dynatrace) 00:42:06 Happy to update.
Hector Hernandez 00:42:07 This one, whenever you guys are ready.
Trent Mick 00:42:10 You are holding the current… oldest open… PR in the core repo, Hector.
Hector Hernandez 00:42:16 Alright. You're waiting a while.
Marc Pichler (Dynatrace) 00:42:25 Boom.
Yeah, hoping to get that done soon, and then… Good.
We'll see if we can release it before we start working on 3DL, or if we… Postpone it to 3.0 and just have it, be… an additional thing that 3DL brings.
Type up the thing that I said here, before create issue, or three little announcement.
Probably.
And then I'd say we do, issue triage for 3.0 on the SICK meeting, And async. So, we cover a lot of ground.
Before starting there.
And prevent some scope creep.
Dated.
David Luna Bistuer 00:43:48 about talking about EZ Ethrevenue and the releases.
Do you think it's necessary to… Kind of define, kind of a backboard process.
So, if we discovered need a new… version that there is an issue, the lawsuit impacts 2.X.
Marc Pichler (Dynatrace) 00:44:10 I think it would be helpful, yeah, to have some sort of… Backboard policy, in place so that we can easily refer to that when we run into the situation that we have to do something like that.
I'm not sure if the specification has some guidance on that.
I think there is a requirement for us to… keep supporting a version for a set period of time, but I'm not sure if it has any additional, guidelines or requirements on how we are supposed to do that.
So… whatever, thing we do. We probably have to make sure that it's specification compliant.
But having something would be very helpful.
Trent Mick 00:45:20 David, were you asking about having a process beyond just… Some written words policy.
David Luna Bistuer 00:45:29 I, I was…
Trent Mick 00:45:31 Yeah, okay, good. I think that might be overkill for us. I expect we won't do a whole lot of that. We won't really have an active 2.x branch, I don't think.
But I wasn't sure if that's what you're suggesting.
David Luna Bistuer 00:45:42 Maybe, I don't know, maybe it's just, Well, as I said, so maybe it's just, Writing down something, or adding a couple of labels in the issues, like, okay, this should be backport.
Trent Mick 00:45:53 Yeah, that's… Probably a good idea.
Makes it easier to find if we have a well-known label.
Marc Pichler (Dynatrace) 00:46:05 Which makes me think about, workflows on these relief branches. We need to make sure that everything that we do is also Like, any changes to workflows and stuff like that need to be done on the… Release branches as well.
Because any, like, security issues with workflows, we also want to backboard to the… to the next branch.
This is one… this was one of the attack vectors that I think the… Which build system was, compromised a while ago.
It doesn't really matter in…
Trent Mick 00:47:01 A lot of them.
Marc Pichler (Dynatrace) 00:47:02 Yeah, it doesn't really matter which one it was, but one of the attack vectors was an outdated workflow, where they had They had fixed it on main.
But the workflow wasn't fixed in… Another branch, and then the attacker got somehow access to push to that branch, and they pushed a commit to that branch, and then triggered the vulnerable workflow, and then used that to publish packages that they weren't supposed to publish.
So if we have the 2.x branch, we need to make sure that we are so… Move any changes that we do to the workflows to that branch.
To avoid introducing more attack surface there.
And also make sure that branch protection and everything is set up just as if it was main.
Which might be a… Yeah.
Might involve a lot of config work that we need to do to make sure that this is… are in place. Right now, nobody can publish from… any other branches in main, because it's locked down through the deployment environment.
But…
Trent Mick 00:48:34 That's only admin repo, yun.
Marc Pichler (Dynatrace) 00:48:37 Yeah, I think it's all in the admin repo, or configured there.
Or through that, actually.
Trent Mick 00:48:53 Okay.
A major… Point on the… Where's the milestone?
I miss this issue.
I was just looking through the… SK 3.0 milestone issues the other day, just to get an idea.
Marc Pichler (Dynatrace) 00:49:17 Hmm.
Trent Mick 00:49:18 there was a request from… I can't remember who was it? From Century, right?
Marc Pichler (Dynatrace) 00:49:24 Andre, I think, yeah.
Trent Mick 00:49:26 Yeah, true.
asking us not to drop Node 20 support.
So that's… Something we should discuss and decide on.
I can… I can understand his point of view.
Marc Pichler (Dynatrace) 00:49:41 Yep.
Trent Mick 00:49:45 We are fighting against the grain in a lot of depths.
In that regard, so… Personally, I don't have a problem avoiding, like, new stuff from… The latest versions in general.
But I guess it depends on some things.
There'll… there's some detail in there to think about.
Marc Pichler (Dynatrace) 00:50:18 one of the… I think we had talked about that a little bit before, with possible changes to the way we test.
Because the main reason why we want to move ahead, quickly to… 22 and beyond is that, we want to update our dev dependencies. We don't have that many production dependencies, so… Just moving ahead.
The dev dependencies is one of the concerns that we have.
And the reasons why we want to do that is because we want to run tests against all the versions that we support.
Trent Mick 00:51:08 And it's just looking, we're using Mocha currently.
Okay, MoCA11 is the current latest.
it supports our version, for sure. Hold on.
it still supports Node 18 that we're using as a base.
Sorry, second, yeah, 18… about 18 and up.
There's a Mocha 12 in beta right now, so presumably that'll come out soon, we'll want to do that. It has 20.19 as a minimum.
So, theoretically, that doesn't screw us. We talked about, like.
potentially wanting to use Node's core tests package, which I can't remember what the base version is, but that's probably a pipe dream, I don't… we're not gonna do that anytime soon, because of my god.
the amount of test code to be updated to do things, so, and Mocha isn't awful, so… I think that's been pretty good so far.
For other testings, so, like, linting and those kind of things, those can be set to only run for… more recent versions of nodes, so, like, the CI for running lint uses node 22, could be whatever, so I don't know that that holds us back too much.
Side question, what do we do for the… spectacularly old node version tests for the API. What are we using in there?
I haven't even looked.
Marc Pichler (Dynatrace) 00:52:34 Ayy.
created one… I actually wrote that recently, and I… don't record anymore. So, we have… some workflow somewhere that does… Compatibility tests.
and there, I think.
Trent Mick 00:53:01 Sure.
Yeah.
Marc Pichler (Dynatrace) 00:53:07 Have to… backwards compatibility chairs thing, and it… It really doesn't do a lot. It just checks if nothing… Immediately crashes when doing that.
Trent Mick 00:53:24 Okay.
So no test for.
Marc Pichler (Dynatrace) 00:53:27 Rich.
I don't think so, no.
Daniel Dyla (Dynatrace) 00:53:30 No, I don't think there's any framework at all.
Trent Mick 00:53:33 It's the NoSQL of testing. Okay, cool.
We can use tape, actually. Tape still works back to ancient versions, I think, but anyway, if we want to test. Not like we're gonna go add stuff there. Okay, so that's probably fine, then.
So I guess maybe… I mean, whatever, we maintainers, we can do what we want, but we could… our… an argument could be that burden of proof is on us to prove that we need node… 22 is a base for something.
Daniel Dyla (Dynatrace) 00:54:05 The only current example.
Trent Mick 00:54:06 is module.registerHooks requires node 22, I think, for the non-experimental version of it. But we're not actually using that yet, so… Sorry, go ahead, Dan.
Daniel Dyla (Dynatrace) 00:54:18 I was just gonna say, when we… When we did 2.0 and dropped support for, like, really old versions, we had a lot of things that were, like, active pain points that we wanted to… to drop.
We made the policy… Not because… We wanted to, like… Drop old versions just to not have them, but because we wanted some… I… like, something to point to in the future when we drop dull to say, look, we said we were going to do this, but I don't think it obligates us to do that.
we could… retain… The old version, for now.
And say, you know, we could keep it in testing, and say.
We're testing it, but it's not officially supported, or something along those lines, and… If it causes problems, then we're not going… you know, a best effort, I guess, is what I'm saying. We could do something along those lines.
Trent Mick 00:55:24 Okay.
Yeah, I'm not opposed to that.
Marc Pichler (Dynatrace) 00:55:31 idea to me.
Daniel Dyla (Dynatrace) 00:55:33 Because if we don't… If we say, okay, we're not gonna do it for 3.0, then… we have to wait until Fordeadow, which should hopefully only be a year, but still.
Trent Mick 00:55:47 I mean, the subtlety will be lost on some people, but we put this front and center on the docs, I guess, saying, node version supported.
22 hard thing and 20 best effort, we'll try to maintain that because of data that we have that there's still a lot of usage and migration is slow.
Is that where we're leaning?
Daniel Dyla (Dynatrace) 00:56:06 Yeah, I guess Andre is even saying… he's only asking us to push, 3.0 back to September. He's not… he's not saying that 3.0 should support the version, he's just saying, wait a couple of months before doing it.
Marc Pichler (Dynatrace) 00:56:31 I have to reread.
Daniel Dyla (Dynatrace) 00:56:32 It's the last line of that big comment.
Marc Pichler (Dynatrace) 00:56:38 Oh.
Late Q3.
Started Q4.
Daniel Dyla (Dynatrace) 00:56:44 I think what he's just saying is, like, the… L… Does cause people to move.
But not immediately. Like, there's some lag.
Oh, my headphones died.
Did you guys hear that?
Trent Mick 00:57:01 Yeah, there's a blip, but you're still there.
Marc Pichler (Dynatrace) 00:57:05 So… September… Susan.
So we can try…
Trent Mick 00:57:20 Well, that's true, it isn't.
Get the summer off.
To play with declarative config.
But then, more really, it still has to fend off these people that we aren't doing the sim conf by default, or we could… we could separate So many choices.
Marc Pichler (Dynatrace) 00:57:36 Yeah.
Marylia Gutierrez 00:57:39 I like that I just… I infected Trent with the declarative config bug. It was me just, like, talking about it for so long, and now, ha, I got someone.
Trent Mick 00:57:50 Well, what you did is you got to my manager that said that we want this, so…
Marylia Gutierrez 00:57:55 That was…
Trent Mick 00:57:57 I do need to justify my work, so yeah.
I mean, so, if… correct me if I'm wrong, but I think if we maintained Node 20 support, then Andrea would be fine.
If us doing a 3.0 soon.
Marc Pichler (Dynatrace) 00:58:24 Our main driver for… Doing 3.0 is… the instrumentation stuff, right?
Trent Mick 00:58:38 Which? Like, the module register hooks?
Marc Pichler (Dynatrace) 00:58:42 No, the SEMConf.
Stuff.
Because it coincides with us dropping support and everything.
Trent Mick 00:58:56 I don't think that requires an SDK 3.0 to do, though. Yeah. You just need… you need a breaking change in the instrumentations, and theoretically can support the older versions, though. That seems vanishingly unlikely.
Marc Pichler (Dynatrace) 00:59:10 So… What if we actually just… do that.
we… Publish new instrumentation versions that go to… to stay with SEMConf without… That coinciding with 3.0.
we push back 3.0 to September, Where, we then drop Node.js, version support?
And… Get some extra time, as you said, to work on declarative config, or… SDK logs, or whatever is the current thing that… People are interested in.
Trent Mick 01:00:06 Okay, we're kind of out of time, so I guess we're gonna discuss one later, but… Yeah, boy. I do wonder if we do the logs thing, including widening the attributes type before 3.0, or if that's not even possible.
That's something… also waiting on a little bit, but maybe less so than the Semantic Convention stuff. So, okay.
Could be continued.
Marc Pichler (Dynatrace) 01:00:34 Thanks, everybody, for joining. Let's continue discussion.
On this issue here, and next week, and have a nice week, and see you next week.
Hector Hernandez 01:00:46 Thank you.
David Luna Bistuer 01:00:47 Okay. Bye.
Marc Pichler (Dynatrace) 01:00:48 Great.
