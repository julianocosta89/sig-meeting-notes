SIG: Java SIG
Date: 2025-10-09
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/DEXdFu3BBQMQTA18kktakIo6CIjzHZe_R8GrqqCj8O6uEW_6IptXlJ58ZOr9sByx.WuFWS67EfDEQM5am
============================================================

## Zoom Recording Transcript

GZ Gregor Zeitlinger 00:01:01 What else?
Trask Stalnaker 00:01:36 The wrong glasses.
Jason Plumb 00:01:39 I do that sometimes.
Welcome back.
Trask Stalnaker 00:01:47 Bang.
Missed you all for 2 days.
Jason Plumb 00:02:10 Did you see my OpenTelemetry pumpkin in the OpenTelemetry channel in Slack?
I know Jay's not.
Trask Stalnaker 00:02:15 Oh…
Jason Plumb 00:02:16 It's completely ridiculous.
Trask Stalnaker 00:02:24 I gotta see this.
Jason Plumb 00:02:45 And it's even sitting on my porch now, so there you go.
Trask Stalnaker 00:02:48 That's fabulous.
Does this work?
Copy image…
Jason Plumb 00:03:11 Paste.
Trask Stalnaker 00:03:12 No.
Jason Plumb 00:03:14 That'd be too easy.
Trask Stalnaker 00:03:16 Yep.
Whoa!
It's a jack sighting! Yeah!
Jason Plumb 00:03:33 What?
What's the password? I'm the real welcome back. Yeah, what's the password?
Jack 00:03:43 I, misaffiliated myself originally. We're all gonna, like…
Trask Stalnaker 00:03:52 Oh, yes, yes, yes, or, Jack Berg Grafana, congratulations!
Jack 00:04:00 Yeah.
Trask Stalnaker 00:04:02 I think we're all gonna run now and add a bunch of extra topics here.
We wanted to discuss with you.
Next week.
We'll ease you back in.
Jack 00:04:16 Yeah, I'm still, I'm still not returned to work, but I'm gonna, I'm gonna start coming to these, I think. I think I can make it work now.
Trask Stalnaker 00:04:26 Oh, fantastic. Here's Jason's pumpkin.
Jason Plumb 00:04:28 There we go.
Trask Stalnaker 00:04:30 Amazing.
Jack 00:04:32 What, do you have a laser cutter, or do you do that by hand?
Jason Plumb 00:04:34 I just did it by hand, yeah.
Jack 00:04:36 Cool.
Trask Stalnaker 00:04:42 Alright, let's get rolling. Jason…
Jason Plumb 00:04:45 Yeah, first topic. So, I think we talked about this in the past, but the long story short is that a new, new-ish version of OKHTP is now publishing, kind of, I will say, two flavors, but really there's a third flavor that sits on top, and they have the OKHTTP JVM,
flavor, the OKHTP Android flavor, and there's one at the top that's just called OKHTTP. That's kind of the dependency triad. And the way it's supposed to work, if you use a build system that understands modules, is that it will pick the right one depending on what platform you're using.
Trask Stalnaker 00:05:21 Gradle… that understands Gradle modules.
Jason Plumb 00:05:23 Sorry, Gradle modules, yes.
And, if you're not using, Gradle, if you're using Maven, then you're… you might have a bad time and get the wrong one. So, to prevent that, I believe that the core repo,
has some code in a PR that I linked to that defaults to JVM.
And I also linked to the POM file that shows that, like, the dependency listed in the POM file is the JVM version.
And what this means is that from Android, when we depend on the exporter, we end up transitively depending on JVM,
And that breaks our users. So we've had a couple of people notice this in the last week.
And I'm interested in creative ideas on ways of solving this, but one thing that came to mind was that maybe we can, from core.
Create a new module that is,
like an OTL… I think it's just the sender that uses OKHTP that's specifically for Android and uses the Android flavor, and that way we can then be specific.
Lauri Tulmin 00:06:29 I'm sure you're not messing up something.
Jason Plumb 00:06:32 I'm never sure of that, Lori, come on.
Lauri Tulmin 00:06:34 The core used to depend on the JVM version, but we changed it so that in the POM files, it uses the JVM version.
Jason Plumb 00:06:43 Yeah.
Lauri Tulmin 00:06:43 metadata, metadata.
Now uses the… Whatever, variant aware thing.
Trask Stalnaker 00:06:51 This hasn't been released, though.
Lauri Tulmin 00:06:54 so…
Jason Plumb 00:06:56 Oh…
Trask Stalnaker 00:06:57 I think this fixes your problem, James.
Lauri Tulmin 00:06:59 Yeah, so next release will fix it for you.
Jason Plumb 00:07:02 What does that look like again?
Lauri Tulmin 00:07:05 You should know.
Jack 00:07:08 Let's go look at snapshots, just to confirm.
Trask Stalnaker 00:07:10 Jason.
Jason Plumb 00:07:13 That's alright, I don't remember what.
Lauri Tulmin 00:07:14 The problem with looking at the snapshots is that,
In the snapshot repository, browsing isn't enabled, so you need to somehow figure out the file names that you want to look at.
Jack 00:07:27 The exact file name.
Jason Plumb 00:07:28 Damn.
Lauri Tulmin 00:07:29 If you deploy them to the Maven local repository, then that's easier.
Jason Plumb 00:07:36 Okay, so this, we think that this, when this is published, this'll fix us.
Lauri Tulmin 00:07:40 It's, actually, the same solution is published somewhere in the contrib, and
I think there is also a release for that.
Might be easier to…
Trask Stalnaker 00:07:53 Oh, that's true, yeah. Good idea.
Lauri Tulmin 00:07:55 But I don't know which module uses it.
maybe the Open client?
Jason Plumb 00:08:09 So, if one were to go, look at the
For the snapshot, does it have the transitive dependency on…
Lauri Tulmin 00:08:17 The home file will depend on the JVM version.
But there is… there is, besides POM file, there's a file called .module, that's the greater metadata.
Jason Plumb 00:08:26 Gradle should use. Okay.
Lauri Tulmin 00:08:28 That one should contain the… non-JVM version.
Jason Plumb 00:08:36 Okay, I will… I will try it, I'll just… I'll point to snapshots and see if, that fixes… like, I'll reproduce this, and then I'll make sure that that fixes it, but I believe you.
Trask Stalnaker 00:08:46 Yeah, and you can look at the, AWS X-Ray, you could browse that, because it's published in…
contribib already. I just copied Lori's… Lori's.
Amazing fix. Yeah.
Jason Plumb 00:09:05 I know. That is awesome.
Okay, so I think I didn't make that connection between the module file and the POM file being…
used differently by different tooling. So one… yeah, okay. Cool. I think we can move on from me, then.
Trask Stalnaker 00:09:26 J.
Jay DeLuca 00:09:28 Yeah, maybe this is already known, but I was looking into one of the old issues around the enable strict context for the tests, and
One of the final ones that is still using the… or disabling it in the test is the Zeo instrumentation.
And, while I was looking into it a little bit, I noticed that, like, Lori had opened, that issue in the core repo. I think just laying out how there's some complications with
the API that make it a little challenging to work with, but also I noticed that in the…
the repo for Zeo, the maintainer of Zeo, kind of talks about how he considers the OpenTelemetry Zeo instrumentation as… broken.
And so I'm wondering if there's even value in us having it?
I mean, he seems to be recommending that users use, like, a newer version, which…
I don't… I didn't look to see if he's recommending that they use that with the agent, and that our instrumentation is supposed to work, but…
Yeah, I just was… wanted to know if what people think about
Whether or not we should continue having a module for this.
Lauri Tulmin 00:10:46 Well, I think it is actually sort of broken.
Trask Stalnaker 00:10:58 If you say it's broken, I say remove… I vote for removing it.
Lauri Tulmin 00:11:02 But it, like, it probably, like, kind of works, but,
The thing is, like,
It basically has, like, the same kinds of features, like the Kotlin coroutines and stuff like that.
That instead of, like, trying to use our context
you probably should be storing the things in some CO-specific context, That the framework itself manages.
Trask Stalnaker 00:11:41 How, do we… Have that problem in… with Kotlin coroutines anymore?
Lauri Tulmin 00:11:50 Yeah, but, like, in the Kotlin coroutines, They have this, like,
This library that's in the core repository.
So instead of, like, calling, like, context make current, you use some sort of, like,
With context, and and pass a span to it, or something like that.
Trask Stalnaker 00:12:27 Right, and I think we even… in the… make current…
Don't we document, say something like, don't use this?
with Kotlin…
Oh, we do some detection.
Yeah, okay, so we have at least a story for Kotlin.
a complete story for Kotlin users.
Lauri Tulmin 00:13:18 But yeah, for CO, like, I don't know, like, Scala at all, and I don't know what CO does, but it might be that it's also better solved in some sort of library-specific way.
We had to do some, like, weird things to… to restore the context.
And probably it's, it's something that just won't work out nicely, whatever we do.
Jay DeLuca 00:13:50 I think if you go to, like, there's, like, a fiber class or something, and it has a comment around…
yeah, fiber contacts.
Trask Stalnaker 00:14:06 So, we… have we rem… Ever removed on instrumentation?
Lauri Tulmin 00:14:18 Well, we have disabled, like, the…
Controller, view span instrumentations by default.
But… well… I don't know if, like, I guess we aren't in a hurry to remove it.
It could be something that could be doing it, for, like… 3.do, or something like that.
If there is a better alternative.
Trask Stalnaker 00:14:49 But at least disabling it by default.
Gives, kind of, that message that it's… Something that, I mean…
beware, I guess, I don't know.
Lauri Tulmin 00:15:07 Like, I haven't obviously checked, like, what the author of CO had to say.
And why he considers this instrumentation broken.
But it very well might be.
Or there might be better alternatives.
Trask Stalnaker 00:15:31 I like the… I mean… The idea of just disabling it by default?
We could…
Lauri Tulmin 00:15:42 Ideally, if we want to disable something, there should be some…
Like, there should be some way out for the users.
Like, there might be some users for whom this instrumentation works well.
We should at least…
Like, ideally, we should be able to provide some guidance and tell them, like, what they should be using instead.
Trask Stalnaker 00:16:05 I mean, if we disable by default, though, I mean, they can still opt into it if they want.
Lauri Tulmin 00:16:12 Another good candidate for disabling by default would be the… Gotlink coroutines, sweet span instrumentation.
That is also, like, problematic, because it doesn't work correctly, always.
And fixing it, like, At one point, I tried, but wasn't able to do it.
Trask Stalnaker 00:16:35 Yeah, don't we have a… I think we might have an issue for that.
Lauri Tulmin 00:16:42 Yeah, I think…
I think the one from 2 weeks ago.
Trask Stalnaker 00:17:01 Oh, hats the most, okay.
Yeah.
Lauri Tulmin 00:17:19 But again, in this case, like…
We might need to provide some guidance, like what to use instead.
Perhaps a library.
Trask Stalnaker 00:17:42 Yeah, I mean, that would be great to have a library, but even if we don't have a replacement.
just… For this one, could we disable it by default?
This is kind of baked in…
I forget how this works. Is it baked into our width span?
Lauri Tulmin 00:18:05 No.
Trask Stalnaker 00:18:05 Already.
Lauri Tulmin 00:18:06 to separate instrumentation.
Well, of course, another option would be to figure out what's wrong with the instrumentation and fix it.
Trask Stalnaker 00:18:22 Yeah, but I, I mean…
I feel like we've spent, over the years, a good amount of time trying to figure out, I mean, the coroutine
We're trying to find a way to interop with… coroutines… bet.
And we do have a solution that does work here.
Lauri Tulmin 00:18:48 Well, this one works, yeah.
Trask Stalnaker 00:18:52 It's just.
Lauri Tulmin 00:18:52 So, actually, somebody reported a bug against this one, too, I think.
But I think it boiled down to being something, inside Kotlin broken.
Or it's at their libraries?
Trask Stalnaker 00:19:17 Okay, I'm just gonna make a note, let's consider disabling… This man…
And I know we've got both a 3-0 project now, and a milestone…
Do we want to continue? I guess we're…
Doesn't hurt to just tag it both.
And for ZIO…
Jay, maybe just open a issue? Yeah, because I agree that this, I think we…
Should probably close this, since… It's… Completed now.
Other than the ZIO question?
And, just open a issue to…
about the ZIO instrumentation, and whether we should disable it by default, or provide, library, or…
Lauri Tulmin 00:20:53 Like, another thing to pay attention to is that, Some of those,
For some of those libraries where you enable the strict context thing.
It might be that the tester passes only sometimes.
Jay DeLuca 00:21:11 Yeah, I was gonna keep an eye on the flaky test spreadsheet over the next few weeks.
Lauri Tulmin 00:21:16 They're probably, like, if they don't pass, the problem is probably something obscure, like, you have to somehow shut it down
Like… Before the test is completed, or whatever.
Jay DeLuca 00:21:32 To solve the… the leak.
Lauri Tulmin 00:21:35 Yeah, like the… Yeah, like, we need to look at case by case, but it's probably, like,
Like, the warning, like,
Something, like, everything might still, like, be working correctly, but there is, like, some small piece that somehow trips to check.
Jay DeLuca 00:21:57 Yeah, I'll keep an eye out, Avazario.
Lauri Tulmin 00:21:59 There must be a reason why they weren't enabled from the start.
Trask Stalnaker 00:22:08 Yeah, I remember some of these were pretty…
dicey, I mean, like, very internal…
Do you want to… I mean, would you like to just leave this
Issue open for a few weeks, until we get a sense that
Whether it's successful or the last couple PRs were successful or not.
Jay DeLuca 00:22:36 Yeah, I think that makes sense.
Trask Stalnaker 00:22:41 Cool.
Let's move on, Gregor.
GZ Gregor Zeitlinger 00:22:53 Yes?
Trask Stalnaker 00:22:55 Hey, Mize commands for common tasks.
GZ Gregor Zeitlinger 00:23:00 Right, since we now have MES for link checking, and that is working out well, I hope, I was wondering, if it makes sense to add other commands, like formatting, running tests, and so on. I'm using them in other projects,
Before I add them, I just wanted to have some feedback.
That's gonna be useful or not.
The advantage is that, you don't have to care about
the language and the build system if you run multiple projects, and also, the Gradle wrapper is sometimes annoying that you have to do this,
directory up, if you don't want to run, like, format in the entire project.
Jason Plumb 00:23:57 The trade-off there being that you have to have this Mize tool installed globally.
GZ Gregor Zeitlinger 00:24:03 well, if you want to take advantage of that. Otherwise, it's just a couple of lines that is in a file. You don't have to use it, you can still call a Gradle
Directly, if you want to.
We could, in addition, decide that we want to get rid of the Gradle wrapper, and then you have to install Gradle, but that's, like, an additional step.
And completely optional.
John Watson 00:24:36 Yeah, I think we want to stick with the wrapper, just for making sure we get build consistency, like, so that different developers don't have to align on their Gradle version, etc.
GZ Gregor Zeitlinger 00:24:49 If we would get rid of the wrapper, then we would have the Gradle version and the MES file instead.
Jason Plumb 00:24:55 But…
GZ Gregor Zeitlinger 00:24:57 This is…
Lauri Tulmin 00:24:57 They want, like, the contributors to be able to build it.
You can't expect anybody to know that tool.
But, everybody's pretty much able to run the Gradle wrapper.
GZ Gregor Zeitlinger 00:25:10 Yeah, right. I'm not suggesting that we get rid of it. I'm just wondering if it would be good to have this as an additional,
Flavor of running, instead of typing in the commands manually.
John Watson 00:25:31 I'm not opposed to it being there as an option, but I don't think we should force… force it.
force anyone to.
GZ Gregor Zeitlinger 00:25:41 And what kind of, commands would make sense?
to have, like, if I do this across multiple projects.
format and test is what I can think of. Anything else?
John Watson 00:26:00 That's what I was gonna…
Lauri Tulmin 00:26:01 Well, since you are the person who's going to be using it, add whatever you like.
Trask Stalnaker 00:26:06 Yeah, I wouldn't use it myself, and I would prefer not to document it in the contributing guide, because then we have multiple
Things that we have to document and support users using.
GZ Gregor Zeitlinger 00:26:21 Okay.
Lauri Tulmin 00:26:22 Generally, like, I think we haven't had good track record with features like that.
Like, that, somebody has contributed, like, this, The option to disable, renaming the packages.
And stuff like that.
Trask Stalnaker 00:26:42 Oh, the shading, right, right.
Lauri Tulmin 00:26:44 Like, somebody occasionally tries to use them and turns out they don't work at all.
GZ Gregor Zeitlinger 00:26:50 What's the similarity? It's also a tool that is rarely used, or what's the…
Lauri Tulmin 00:26:56 Yeah, like, something that only one person uses.
GZ Gregor Zeitlinger 00:27:03 Right?
I can also edit locally if nobody else is interested.
It's also fine. I don't have to commit it.
Trask Stalnaker 00:27:15 Yeah, I mean, I think that would be my preference, just to stick with Gradle in the… we already have, kind of, common Gradle commands across all the Java repos.
It's already documented.
GZ Gregor Zeitlinger 00:27:28 Yep.
Trask Stalnaker 00:27:29 Flexible, you can… yeah.
Cool, let's go on new slot for a declarative config meeting.
So I realized I can do every other Thursday before this meeting.
Or every other Monday.
I do think it's nice, I do like the… our declarative config separate meeting, just allows us to spend some deep dive into the PRs a little bit.
GZ Gregor Zeitlinger 00:28:05 Yeah, I think every other Thursday,
would be sufficient. There's not so much stuff Going on right now.
Trask Stalnaker 00:28:16 Cool. I will put it back on the calendar. We just had the SEMCOM meeting today before that, so it's… we're off next week, so I'll start it next week.
Jay DeLuca 00:28:31 Gregor and I will be at an off-site next week, but…
Trask Stalnaker 00:28:34 Okay.
Jay DeLuca 00:28:35 And I will.
Trask Stalnaker 00:28:37 Three weeks from now.
Jack Shirazi!
Jack Shirazi 00:28:50 Yeah, so I'm printing out the, the OpenTelemetry object,
And what I do is I just wait a few seconds till after the agent's finished and print it out. It works really nicely, but I'd like it to be a bit more…
Specific as to when it… can be printed.
So, I tried using an Asian extension.
It works externally, but you can't include it with the agent.
Because of shading. So, I'm just wondering, is there any, like, entry point Or I could add in…
Configurably add in a method that
Would allow me to access that object after it's been configured.
Jack 00:29:36 I thought there was a dedicated place where you can get a callback when, the OpenTelemetry SDK instance has been configured.
Huh.
Jack Shirazi 00:29:48 That would be perfect.
Lauri Tulmin 00:29:51 Every choice, or…
Jack 00:29:53 Agent listener, yeah.
Lauri Tulmin 00:29:54 Yeah, agent listener, I think, is the one that.
Jack 00:29:57 Posted in the chat.
Jack Shirazi 00:29:59 Fabulous, thank you.
John Watson 00:30:03 Hey, Jack, welcome back.
Jack 00:30:05 Hey, John.
Trask Stalnaker 00:30:13 Cool, great.
Then, moving on, Bruno.
Bruno Baptista 00:30:20 Hey, good afternoon.
Trask Stalnaker 00:30:21 Hey!
Bruno Baptista 00:30:22 Welcome back, Jack, and good luck on the new job.
Jack 00:30:26 Thanks, Bruno.
Bruno Baptista 00:30:28 So… We have this semantic stability class, on the instrumentation project.
Currently, it holds, well, a switch, basically, to use the old or the new stable semantic conventions for databases. That's just one example.
However, the way it switches is based on, on,
What's its name? It's… it's a system get property call.
So, it totally bypasses the configurations that are actually used by the SDK.
Therefore, if we curate the properties and we use a property supplier.
Well, that's not going to be applied here.
So, my question is… so, I have a few questions. One is that if we already settled on,
On a timeline for the instrumentation of 3.0.
Because, well, if it's close enough, this is not a problem, and this will go away soon.
The other is, if in the long run, we shouldn't… I should have a way to retrieve the properties that are being used by the SDK itself.
I remember that we discussed it a bit, at some point.
I don't know if we should actually expose a getter or something in the… in the SDK API itself.
But this would be quite handy.
for the instrumentation.
Yeah, so what's your thoughts on this?
Trask Stalnaker 00:32:25 Yeah, so… This is… Yeah, so this is in the API,
Bruno Baptista 00:32:34 Yeah.
Trask Stalnaker 00:32:34 No, sorry, in the… yeah.
So, instrumentation, you're right, instrumentation has not had access to configuration properties.
Previously, that is… Changing with declarative configuration.
And this PR, which has not been released yet,
Gives us the first crack at being able to use declarative config.
from instrumentation.
Bruno Baptista 00:33:10 Yeah, but that… that… will that include,
So imagine that I don't have the quality config by file, but I'm using the config supplier. Will those configurations be available,
In here, as well.
GZ Gregor Zeitlinger 00:33:27 And know the… Declarative configuration does not have the same notion of a properties supplier.
So, this will not help you.
And also, in the place where we are asking for the semantic, for the opt-in,
There's also, no way that I found to, look at the… declarative configuration.
Because it's in some static place. For a lot of other usages, I have a PR that is based on this extended open telemetry that actually looks at your declarative configuration, so you could put it in
you're in the YAML file, and I think this was one of the few that, would not work, because it would have been a bigger refactor to make that work.
Bruno Baptista 00:34:31 Okay, so…
Trask Stalnaker 00:34:32 So there were… there were a couple different things there, Gregor.
For the staticness,
can't we pass in the open telemetry? I mean, is that not… isn't that solvable? I would assume that's solvable just by passing in… making this not a static
class and passing in the OpenTelemetry instance to it.
GZ Gregor Zeitlinger 00:34:58 It probably would, yeah.
Trask Stalnaker 00:35:01 Okay.
And then the other point about the… The…
not the config properties. So, Bruno, today you're using config properties.
And the auto-configure… Callback there to add config properties.
Bruno Baptista 00:35:26 Yes.
Trask Stalnaker 00:35:27 What you'll want to look at
Is how to migrate that, how to support how to…
Use the new callbacks that are declarative config-based.
So that you can, map your Quarkus properties into declarative config.
Structure. So it doesn't mean you have to use the declarative config file.
But you'll want to map your config properties into the declarative config.
format.
Bruno Baptista 00:36:01 Yeah, that can be a way to do it, yes.
Well, basically.
Lauri Tulmin 00:36:07 Gotcha. Basically, this class is an internal API for… for us.
And it has been designed in a way that it works well for us.
Bruno Baptista 00:36:19 Yeah, I know, but…
Lauri Tulmin 00:36:21 If you need something else, then, well, you're welcome to do the work, but it's going to be complicated.
Because…
Trask Stalnaker 00:36:29 I think the problem, if I understand Bruno's problem, is that our, like, our JDBC instrumentation, uses this class.
And so…
the… in Corcus, they want… they use our JWC instrumentation, which then uses this, and they have no way of influencing.
Mapping their config properties into here.
Lauri Tulmin 00:36:55 The thing is that most of our library instrumentations are programmatically configured
And now, if we want to, like, make this also configurable, the question is, like, how do we do it?
Do we add this option to our, like, library instrumentations as some sort of experimental thing?
So that you can choose, like, the symptom stabil stability there.
Or do we figure out some other way how configuration could be passed through the library instrumentations?
Bruno Baptista 00:37:32 I'm thinking…
GZ Gregor Zeitlinger 00:37:33 Peter.
We have figured this out already. This, is exactly the extended open telemetry that enables it, and I have draft PR that takes advantage of that.
Lauri Tulmin 00:37:45 The thing is that I don't think that all the places where this class is used from have readily accessible OpenTelemetry instances available.
Anyway, it requires some effort to make it work.
And probably the motivation for us to do it isn't super high, I don't know.
Or maybe Gregor is working on it already.
GZ Gregor Zeitlinger 00:38:08 I am motivated, because I think, it is required to give you the full,
experience of using declarative configuration, because if you still need to configure some things as environment variables, then it's a mixed experience.
But I also wanted to, add something else,
Maybe the Quarkus implementation is similar to what I'm trying to do with the Spring Starter. And,
I could add a link to how the Spring Starter is working, or we can also
I can also walk you through it,
After the meeting, and how this is working, maybe you can take some inspiration from that.
Or give us better ideas how we can do the Spring Starter.
Bruno Baptista 00:39:04 Yeah, so I want to hear Jack, Jack's opinion, his… Has his hand up.
Jack 00:39:13 Just, just a quick question, Trask, where, where's this, config propertyUTILS clause?
Is that part of the SDK, or instrumentation?
Bruno Baptista 00:39:23 API.
Jack 00:39:26 And is that…
Trask Stalnaker 00:39:27 R.
Jack 00:39:28 So maybe I was misunderstanding, does that…
Directly read system properties, or… and environment variables, or…
Lauri Tulmin 00:39:37 Yes.
Jack 00:39:37 does that also read the configured… so it basically skips any sort of the SPIs that, you know, things can use to overwrite those system properties?
Lauri Tulmin 00:39:48 Yes.
Jack 00:39:50 And so there's this other place where we,
like, you know, centralize some tools to read common config properties, which is called Common Config. I just pasted a link in the chat. And,
My understanding is that this does not directly read system properties and environment variables. It… it is… it can be influenced by
the, you know, any of the SPI overrides, and so I guess my question is, like.
what about semantic stability requires it to skip the SPI overrides and, like, you know, directly read system properties and environment variables?
That just seems like a miss, right? That, like, you know, an agent distribution wouldn't be able to influence the…
Semantic stability.
Lauri Tulmin 00:40:43 I think it's, all about ease of implementation.
like, this is the tool that we had available, and we have always treated sim core stability more like our…
Internal incubating feature that allows us test, the new SimCons.
We haven't, like, really considered it as a user-facing feature that much.
Jack 00:41:11 So, Jack, this…
Trask Stalnaker 00:41:13 This requires injecting the… basically turning this into a, you know, non-static class, and injecting something into it.
Which is… I mean… I mean, it makes sense, this is obviously simpler, it's gonna, we'll have to look at how many places need to inject it, but I do… I mean, I think it makes sense to inject it, or I would support a PR that…
injected it, and then allowed us, even better, to inject OpenTelemetry instance, so we can get extended
We can get the new config properties. Really, that's… I don't really…
I mean, we've basically steered away from any library instrumentation using
Config properties, because we haven't had access to them.
The only way this works is in the Java agent.
Because we do some magic via that config… that common config.
Lauri Tulmin 00:42:17 Like, library instrumentations not using system properties isn't entirely true.
We have those library instrumentations that are automatically configured
Where the, like, basically by injecting some SPI, for example, where the only option to configure might be the config properties currently.
Trask Stalnaker 00:42:40 Yeah, I'm trying to remove one of those right now, the Kafka.
This one.
Yeah, because in some cases we have, so we can actually get rid of that. But yes.
Bruno Baptista 00:42:56 This is…
Trask Stalnaker 00:42:57 the problem with not having a config API in OpenTelemetry, which is now being solved by declarative config?
GZ Gregor Zeitlinger 00:43:09 You would also need to figure out where this would belong in the declarative configuration file, because it sounds like this is something that is cross-language.
Jack 00:43:21 Exactly.
Trask Stalnaker 00:43:21 Yeah.
Jack 00:43:22 That's kind of what I was thinking about, is like, this…
like, what does the actual story look like, this end-to-end, even once, you know, we have this configuration API readily available to instrumentation? It's like,
Okay, so an instrumentation accesses, the OpenTelemetry instance, it determines that it's an extended OpenTelemetry instance, and therefore can read, you know, the config
configuration options from that, and then, you know, it walks the configuration scheme to find these specific properties that configure semantic stability opt-in, and that's, I guess, what's missing then, is where exactly do these options fit into that schema?
Trask Stalnaker 00:44:07 Yeah, Gregor, do you want to open a… it would be great to open a issue in the configuration repo.
I know this will probably be… we're… we gotta deal… Jack, between SEMConv, and I think we're blocked on another one like this, of the known methods.
Jack 00:44:26 Right.
Trask Stalnaker 00:44:27 Do we add it to SEMCOM? Do we add it to declarative? How do we document that?
But…
Jack 00:44:34 This is the same type of thing, right? Because this property is one thing that's… it's part of the semantic inventions repository, right? It's mentioned in a bunch of documents over there, and so, you know, I think by the sort of, you know.
what we've come up with in declarative config is, like, if there's a reference in semantic conventions to a particular property, we want to be able to have a schema corresponding to that, and so it fits that criteria.
GZ Gregor Zeitlinger 00:45:05 So, semantic convention.
repository, then?
Trask Stalnaker 00:45:12 I think configuration… Repo?
Jack 00:45:16 Just like your known methods, right, Gregor? I think you have an issue about that.
GZ Gregor Zeitlinger 00:45:20 Exactly, and that has not been moving forward.
Jack 00:45:24 What's that stuck on, out of curiosity? Just…
Trask Stalnaker 00:45:28 or absence.
Jack 00:45:29 Oh, so… sorry.
So, so we just don't wanna, like, cause… We…
So, is there a PR open in declarative config?
GZ Gregor Zeitlinger 00:45:42 There is a PR and semantic conventions open right now, but I…
don't know how to unlock it, and I have not spent so much time on it.
Jack 00:45:54 Okay. Well, my position is, like, I don't want to get perfect in the… I don't want to let perfect get in the way of good here. You know, if we can… even if the initial solution for referencing semantic convention properties and declarative config is sort of imprecise, or maybe redundant in some ways, I think that that's fine to get us started, and we can work towards a more optimal solution where, you know, things are…
In exactly one place.
GZ Gregor Zeitlinger 00:46:21 Yeah, that sounds good.
Trask Stalnaker 00:46:22 Okay, yeah, so this is, I think, what it's… Like.
Jack 00:46:30 Okay, I'll take a look at this then. Maybe if you can just link to this in the notes.
Trask Stalnaker 00:46:35 Yeah, yeah. Yeah.
Jack 00:46:37 I'll just… I'll try to get this unstep.
Trask Stalnaker 00:46:43 Where do we… Thanks for great note-taking, as normal.
That's not me. Thank you to Mysterious Notetaker.
Yes, I think this is… that's a great plan. Gregor, you'll open, I think, let's see, we can put this… do you mind if I put your name, Gregor, for opening an issue?
John Watson 00:47:24 The fonts… the fonts, Trask.
The fonts, what's going on?
Bruno Baptista 00:47:30 I think it's my fault. And it probably pays to be…
Trask Stalnaker 00:47:35 Always Jason's fault.
Jason Plumb 00:47:39 I'm the one that comes and fixes it.
Trask Stalnaker 00:47:44 Alright.
Bruno.
Does that at least give you… Some ideas, next steps, understandings.
Bruno Baptista 00:47:56 Yeah.
Trask Stalnaker 00:47:57 I know it doesn't completely solve everything today.
Chet, it would be great, in these deep dive declarative configs meetings, which will start
The hour before this, in 3 weeks from now, is a good place where we can really dive into
Because I would love to understand the mapping from FCUS, how you all can take advantage of declarative config, because we are… we're really trying to lean into that.
Bruno Baptista 00:48:29 Sure. Going forwards.
Yeah, at some point I will have to do that mapping, so better start working on that soon.
John Watson 00:48:40 Before we dive into issue triage, Jack, do we… should we talk about release tomorrow?
Yeah, haven't thought about that in a while. Yeah, because I think tomorrow is the scheduled day for it, so… is there anything that we need to get
in… before the release.
Jack 00:49:00 And also, who's been running the release? Thank you to whoever's been doing that.
John Watson 00:49:04 So, both Chask and Jason have pitched in, and I came in to…
Support in at least a couple cases, so…
We've been sharing the… sharing the love.
Jason Plumb 00:49:15 Teamwork.
John Watson 00:49:17 It makes the dream work.
Jack 00:49:21 Nice.
GZ Gregor Zeitlinger 00:49:22 I have one that I wanted to get merged. Should we just create a milestone and then track it using that?
Jack 00:49:30 Do you have right access?
John Watson 00:49:32 Ain't nobody got time for milestones? We got a release tomorrow.
Jack 00:49:39 How about, I mean, what… is there anything lighter weight than that? Just like a… if… if folks have…
Trask Stalnaker 00:49:45 Added in here.
John Watson 00:49:46 Yeah, there are things we just put it in the doc here, I think it's probably…
GZ Gregor Zeitlinger 00:49:50 Okay.
Jack 00:49:51 Gregor, if you're talking about the PR that you tagged me on earlier, I merged that.
GZ Gregor Zeitlinger 00:49:58 Oh, okay, cool.
Jack 00:50:00 About accessing, the resource when using declarative configuration.
GZ Gregor Zeitlinger 00:50:06 Right, yeah, cool. Thanks.
John Watson 00:50:08 Hey, Trask, are any of the… the Java 25…
unsafe things? Are there any… it's unclear to me, there's a bunch of different things floating around, like, do we need to merge any of those, or are those experiments that you're running?
like the VAR handle one.
Trask Stalnaker 00:50:25 Hmm.
John Watson 00:50:27 And the other one, and…
Trask Stalnaker 00:50:28 Our handle one is… Be ready for reviewing. The only failure is CodeCub, which I disag… vehemently disagree with.
John Watson 00:50:42 Is that because CodeCov only runs against, like, one of the build things or something?
Trask Stalnaker 00:50:48 No, it's just there's… what, on this one, or was it… let's see…
John Watson 00:50:56 your point.
Trask Stalnaker 00:50:57 This one…
John Watson 00:50:58 92 behind the required amount.
Jason Plumb 00:51:01 By banana?
Trask Stalnaker 00:51:03 Maybe it's…
Jack 00:51:03 No, we're going.
Trask Stalnaker 00:51:04 that I…
disagree with. I think it was a different one that I disagreed with. I can look at that one… this one.
But I'm not even sure if y'all want this.
Jack 00:51:16 I think I want it. Yeah, no.
John Watson 00:51:19 I took a picture.
Looks good to me, too. Like, I think it seems good.
Jack 00:51:24 Yeah, I don't think it's necessary, like, strictly necessary for this release, because, in Trask, you know, we've talked about this asynchronously, but,
You know, the references to unsafe, they all have alternatives available. It's just you get some pesky warnings in your logs that suggest that something's wrong. But we've already got backups in place that, you know, use less performant implementations if you're using Java 24+.
Trask Stalnaker 00:51:51 Yep. And this one is kind of interesting, if you all caught that the var… this is pretty much only going to be used by the Java agent.
Because… for var… for, var handles, go through the normal… We're accessing string internals.
And so you actually… to get it to…
work, you have to open Java Lang.
to OpenTelemetry.
Packages.
Which users are basically not going to do. I mean, we can give them that as an option.
Jack 00:52:35 So what about, what about accessing string internals makes, makes you have to open this up? So, var handle, you don't need special access for, but you're saying var handle plus accessing string internals requires this special module access?
Trask Stalnaker 00:52:48 Yeah, because unsafe… bypassed the Java module system.
Jack 00:52:54 Yeah.
Trask Stalnaker 00:52:55 Var handles does not bypass the Java module system.
Jack 00:53:00 Okay, so then… the situation of people who would be getting, like, suboptimal string encoders are Java 24 plus users who are not using the Java agent and who have not, opened up this, you know, module access, as you've described here.
Trask Stalnaker 00:53:18 Right?
Jack 00:53:19 So, like, and they… there's no recourse for them right now.
Right? Like, you know, the additional security of removing unsafe and of the module system is basically means that, like, every time we encode a string in Protobuff, we have to pay a tax.
Like, that's the price we pay for these additional restrictions from the JVM. And so, like, it might be worth documenting this, you know, you're saying that regular users won't do this, but it might be worth putting somewhere on Opentelemetry.io, like, hey, this is something you should consider, because this is a meaningful performance improvement.
Trask Stalnaker 00:53:58 Makes sense.
Jack 00:54:00 Not a blocker for this PR.
Trask Stalnaker 00:54:01 Yeah, yeah.
Jack 00:54:02 isolate, but…
Trask Stalnaker 00:54:04 Let's see, add to my action items… Consider documenting this.
Jack 00:54:21 Thanks for doing all this, by the way, this is… This is great.
Trask Stalnaker 00:54:26 Yeah… It was overtaxing co-pilot.
Jack 00:54:36 A co-pilot was involved?
Trask Stalnaker 00:54:38 Oh, Copilot's involved in everything I do now. It needs a lot of guidance, and a lot of fixing, and, it doesn't… yeah.
John Watson 00:54:52 Yeah, I would guess this is a corner of the JVM in Java that Copilot probably doesn't know much about, because there's probably just not much usage of var handle out there in the real world.
Jack 00:55:03 Not much Stack Overflow posts.
Trask Stalnaker 00:55:05 VAR handles… the VAR handles stuff, I think it did fine on, it was just… it was really… the part that took me a long time to really get my head around was the… that there… I could not find any way to bypass this problem. The ad opens.
John Watson 00:55:25 Oh, "…
Lauri Tulmin 00:55:27 You know that JVM Motors have done this… have done it this way deliberately.
Trask Stalnaker 00:55:34 Sorry, where?
Lauri Tulmin 00:55:35 You know that JVM Motors have done it deliberately.
You aren't supposed to be bypassing it.
John Watson 00:55:45 It's true. They don't want you accessing the internals of their classes, and why would they? Like, that's…
I mean, that's… it's just… they're breaking encaps… we're breaking encapsulation intentionally here, so…
Jack 00:55:56 That should give us better tools to UTF encode strings, then, performantly.
Lauri Tulmin 00:56:01 Well, actually, like, I think,
The standard way might be a bit faster.
Than what we do without the unsafe?
But it, the downside of it was that it… it allocated memory.
Jack 00:56:21 Oh, well, yeah.
John Watson 00:56:24 Yeah, I mean, that's where the JVM has to make a call, right? To say, we're either going to give you a performant memory or performant time, and…
Lauri Tulmin 00:56:32 I don't know if the allocations are actually, like, that big of an issue, but it sure as hell looks nicer in benchmarks when you have, like, zero allocations added by us.
Jack 00:56:43 Yeah.
John, we had performant time and memory allocations, so…
Lauri Tulmin 00:56:54 If you want to… if you want to improve it even further, you should be checking the…
incubating vector APIs.
Jack 00:57:05 Hmm…
Trask Stalnaker 00:57:12 Okay, we are… At one minute over time, anything else that… is approved? Does that work?
John Watson 00:57:30 I just approved, yeah, that one there.
Just moments ago.
Which is profile and stuff, so we can merge it if we want to… if it… if we want to get it in there. It's fine.
GZ Gregor Zeitlinger 00:57:41 A lot of the, renovate PRs will run now because, the link checker has been fixed, but I cannot…
John Watson 00:57:50 You just have to rebase them or rerun them, yep.
Trask Stalnaker 00:57:54 Everything's been failing due to the link checker, so…
So you can, you can click here. Gregor, I think you can actually…
GZ Gregor Zeitlinger 00:58:03 Oh, if you're a teacher…
Trask Stalnaker 00:58:05 Oh, you're not a triageer?
GZ Gregor Zeitlinger 00:58:07 Yeah, but.
Trask Stalnaker 00:58:10 Oh, we made you a triager?
GZ Gregor Zeitlinger 00:58:12 Yeah?
That would be great.
Trask Stalnaker 00:58:14 Oh, but you can't click, so you can only add labels, but you can't that's…
John Watson 00:58:20 And edit descriptions.
Jack 00:58:21 Freddie.
Lauri Tulmin 00:58:23 But, like, the link check failure shouldn't be… Blocking the mergers anyway.
John Watson 00:58:28 No, we can merge without it, it just looks a little… it always makes… it looks a little weird, but… because Java.io has been so flaky lately. Is it even up anymore? Like, if it was down for at least a day, I don't even know if it's up.
GZ Gregor Zeitlinger 00:58:42 But, with the latest changes to the link checker, it will only check if you have actually changed Markdown files.
John Watson 00:58:50 Yep, yep, yep. No, it should be fine. Yes.
Trask Stalnaker 00:58:54 I think there's a shortcut.
John Watson 00:58:55 Although we may have problems with the release because of that.
Jason Plumb 00:58:59 Wait, so if a link becomes broken and we didn't update the URL, then we'll never know about it now?
GZ Gregor Zeitlinger 00:59:05 We will know when we change the configurations, so for example, when we update Litgy, then it will show up.
Jason Plumb 00:59:13 When we update the version of Litchy?
GZ Gregor Zeitlinger 00:59:15 Exactly.
Trask Stalnaker 00:59:17 Don't, don't we run night daily?
across… I know in the contrib… in the other repos, we're running daily.
Jason Plumb 00:59:30 That would be fine, but I hate for stuff to be broken.
Even if we didn't break it, right? If somebody else breaks it, we should know about it.
GZ Gregor Zeitlinger 00:59:39 That's a good question, if the daily is catching it.
Trask Stalnaker 00:59:48 Damn.
So…
GZ Gregor Zeitlinger 00:59:54 We're passing the, the event type to the script. If the event type is,
Something different, then we can adjust the script.
Trask Stalnaker 01:00:10 Yeah, I thought that I handled that, but…
Now I'm bouncing around and not…
GZ Gregor Zeitlinger 01:00:23 Yeah, I can look into that.
Trask Stalnaker 01:00:26 So I think these builds… this… Bill Daily…
Link check…
Jason Plumb 01:00:43 8 seconds, that's very fast.
Trask Stalnaker 01:00:45 modified files only. Okay.
Jason Plumb 01:00:48 Probably, yeah.
Trask Stalnaker 01:00:50 I would probably have a problem, yup.
Jason Plumb 01:00:52 zoom.
Trask Stalnaker 01:00:55 I did want to show you all this little shortcut on the…
dashboard, so there's a renovate issue in all the repos. That's kind of like a dashboard, and…
John Watson 01:01:07 We can rebase all at once.
Jack 01:01:09 Oh, that's awesome.
Trask Stalnaker 01:01:10 book.
Jason Plumb 01:01:13 I just felt the money, like, fly out of our wallet when you did that. Oh my gosh.
Trask Stalnaker 01:01:21 Alright, y'all, we hit our time.
Jack 01:01:23 See ya! See ya.
Trask Stalnaker 01:01:25 Good to see you. Bye.
