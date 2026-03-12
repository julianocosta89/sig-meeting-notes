SIG: Ruby SIG
Date: 2025-08-12
Duration: 47 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 01:14 Hey folks, we'll wait another minute just to see, if anyone else is going to join us. We'll get started at 3 after.
Alright, we'll give Eric another minute to see if he'll join us.
Okay.
Well, I… we can dive straight into the agenda, but there's some new faces today. I wasn't sure if we wanted to do a round of introductions first, or at least new-to-me faces. I mean, folks may have come before.
I can start. My name's Kayla, I'm one of the maintainers of OpenTelemetry Ruby. I'm based in Portland, Oregon.
And, I work for New Relic as my day job on their Ruby agent.
… Since it's… yeah, I guess, Wendy, you're next on my screen. Do you want to go next?
**Wendy Smoak** 03:42 Sure, I'm Wendy Smoke, I'm… South of Atlanta, near Columbus, but if you say Columbus, people think Ohio, and it's in Georgia, so… And Ben working with… you've seen me on the channel, well.
Having success with logs, and now looking at metrics, so pretty much just… Hanging around, trying to see what the state of metrics are, and what's needed before we could get another release with what's there.
**Kayla Reopelle** 04:08 Okay, nice.
**Wendy Smoak** 04:09 Thanks.
**Kayla Reopelle** 04:10 Welcome.
Hannah, I see you next. Do you want to go?
**Hannah Ramadan** 04:14 Yeah, hi everyone, I'm Hannah. I live in San Francisco, and I work at New Relic on the Ruby agent as well. I'm always trying to contribute more to open telemetry, and yeah.
**Kayla Reopelle** 04:30 Nice.
Mikael? Is that how you say your name?
**Michał Kaźmierczak** 04:34 Yep.
Yeah, my name is Michal, how about everyone.
I was working on the gRPC instrumentation, I was helping out with, with the adaptation of the gem. And yeah, I joined today to… just to understand if there are next steps regarding this JRPC instrumentation. If not, how I can help… how I can contribute to the project.
**Kayla Reopelle** 05:03 Thanks.
Yeah, Eric or Schwan, whoever wants to….
**Eric Mustin** 05:10 I joined late, sorry. Eric Mustin, I'm in New Jersey. I work at Elastic, but not on the… I'm a customer architect there, which is, … you know, like, reports in through, like, sales, for context, and not, like, the engineering teams, but was, formerly associated more closely with this project at, Datadog and Shopify, and still try to contribute where I can, which is… more limited. Yeah, so I don't know much about, most of my context is the tracing.
Trib libraries?
**Kayla Reopelle** 05:49 Nice. And Schwan?
**Xuan Cao** 05:54 Hi, … I'm visiting, Toronto, Canada.
Oh.
Working on the matrix most of the time.
And, some of the… Oh, lambda, … serverless stuff.
Sorry.
**Kayla Reopelle** 06:13 Awesome, thank you.
Alright. Well, let's jump into the spec sig. So, there was a pretty short meeting today. … Most of the conversation was just kind of focused on what it is that needs to happen to, kind of change development sections of otherwise stable specifications. I think there's going to be a little more discussion about this in the issues themselves.
… KubeCon EU CFP is open now, the Observability Day for KubeCon North America CFP is open as well, and then they were just checking in on some PRs that needed to be merged. So, nothing, nothing super relevant to our group, or new things that we should work on.
I kind of dominated the agenda, but I'm happy to talk about other things. I was just kind of filling in stuff that popped up, so if anyone else wants to add things, especially the folks who are new today, here's a link to the document. Feel free to put things, Put things on the list.
But we'll start from top to bottom for now. … So, I wanted to check in, I'm really glad you're here, Eric, to talk about this one. … But maybe, since you opened the PR, Schwan, you can… chat about it, too. It looks like a pretty simple PR. I think my main concern is about the braking change and whether we want it to be a breaking change, since traces, that SDK has already reached a 1.0 level.
So, yeah, I'll stop talking.
**Xuan Cao** 08:05 So… yeah, those two, just, like, Janelle, you know, questions, … That's fine. I, so we have this, we have this kind of issue.
While we're in testing the Lambda, layers, if the… Somehow the… the span is not… recording, it's not recording. And then the user still wanted to access the… Back to attributes and, events, it works through the arrow.
So currently Lambda… instrumentation, there's no… Rescue for this kind of a, case, so… So there's two ways, either we… fix… well, we add rescue in Lambda implementation.
to prevent this from happening already, I just know about now, or… options to this API.
So that if… Review there have, … Encountered as kind of a… like, … not overspend, and… There'll be no arrow.
That's the main idea.
**Eric Mustin** 09:18 Boom.
Okay, … I… Don't know if I… Holy… Understand, to be honest, but… What is the, … so basically we're adding… these two public methods to the NOAP, just the no-op span on the API.
… and… but that's not documented in the… specification for… you know, I guess, what is the no-op span specification? Is there… How well specified is that? … I don't have a… I have not looked at it.
And I've not looked at this PR until 30 seconds ago.
So….
**Kayla Reopelle** 10:02 Yeah, the span….
**Eric Mustin** 10:07 … a, … would… Be hesitant to push any braking changes and create a, you know, a major version.
**Kayla Reopelle** 10:22 Well, and I think generally, … adding an API isn't seen as a breaking change. I think that's just normally seen as a feature. I guess, why… why were you thinking it might be a breaking change?
**Eric Mustin** 10:32 Oh, you had… sorry, I thought you had said at the beginning, at the, when you were mentioning the issue, ….
**Kayla Reopelle** 10:38 Oh, it, that's how the PR was opened, was as a breaking change. ….
**Eric Mustin** 10:45 Oh.
**Kayla Reopelle** 10:46 Yeah, for sure.
**Eric Mustin** 10:46 Sorry, I didn't see the bang. You're saying in the conventional commit message?
**Kayla Reopelle** 10:53 Correct.
**Eric Mustin** 10:53 Okay, … Yeah, I guess it's just additive to the, … Is there… in the… Sorry, in the PR description, is there a link to… the, … this occasion?
**Kayla Reopelle** 11:12 No, it doesn't look like.
**Eric Mustin** 11:13 Okay, … Oh, okay. I, … Original Hashtra.
Turns.
I mean, … It seems fine, but I, I don't have an offhand opinion. Or I don't want to, you know, give an incorrect opinion without having looked at it.
I don't look at the, … Hold on.
**Kayla Reopelle** 11:47 Yeah, I think just to have it on your radar, something to think about this week, so that we can talk it through.
more deep in the traces, I'd love your input.
**Eric Mustin** 12:02 In spam.
Okay.
I guess I'm, … yeah, I'm surprised.
Yeah, I'm surprised it's, … Yeah, okay. Let me, let me think about it. I'm not, I'm not sure, and I don't want to talk about it, so….
**Kayla Reopelle** 12:23 Oh, grease.
Okay, the next one is another one that is just kind of on radar, new contributor, updating the max instrument length. I think this all looks good, but, it's nice to sometimes have a second, approval on things, so since it's a short PR, I just thought I would, shout it out, if anyone could take a look.
**Eric Mustin** 12:55 I can approve it.
**Kayla Reopelle** 12:57 Okay, thank you.
The next thing I wanted to chat about was related to metrics and the drop aggregation.
So, the… I wasn't exactly sure how the current drop aggregation is working.
This came up while I was reviewing one of the other Metrics PRs that was opened, … I think this one… But given that we have a larger crew here today, I'll just… I'll message you about this, … offline, Schwan, so that we can chat about it there.
As well as the merge order for the new PRs. I just want to check to make sure.
we're doing everything in the right order, because I think we should have… Oh, we surprisingly do not have a new release out that is unexpected.
Well, I think we'll have some changes that'll be ready soon for a release, with the async instruments getting merged, So… Yeah, so maybe you and I can work together to coordinate.
Those releases, and what should be included in them.
Alright, the next thing I wanted to chat about was, I think towards the end of a recent meeting.
We were talking about the locker… … bridge, instrumentation, PR that's been open for a long time, and trying to figure out how to get it wrapped up.
And I did a little bit of research, … On the other implementations.
Of logging bridges, just to see how they were organized, and… It doesn't seem like there's a consistent place. Like, in Go, there's a separate directory called bridges that it puts the instrumentation. Java and JavaScript are kind of similar, where it just has it in general instrumentation. … So, I guess I just wanted to check, since it seemed like organization was the main sticking point, if I remember correctly, about where we're gonna put it.
Slash, this all happened a while ago, so I don't exactly remember what the blocking feedback was.
I think my concern about creating a new directory for bridges is that it will… make our CI… I think a little more complicated, … But I… I am also okay with it, if that's what, people think.
Is going to be the best approach to… Keep things organized separately.
**Eric Mustin** 16:16 I was looking at the spec for the API thing, I think it's fine.
**Kayla Reopelle** 16:19 Oh, yeah.
**Eric Mustin** 16:20 Sorry.
**Kayla Reopelle** 16:21 That's okay, no worries.
**Eric Mustin** 16:22 I'm really bad at meetings.
Yeah, I feel like, we just didn't do it to save the allocations on an upspin. Getting back to Schwan's… that's my guess. Or, like, that sounds like what… Francis would have done. … So, it's… I can approve it, but I might just… let me just maybe review it a little bit more, while I have a minute outside the meeting.
Okay, for the logger, ….
**Kayla Reopelle** 16:51 So that's Yeah, so it's just about, if the instrumentation organization is the problem, or if there were any other… problems.
See something in the chat.
**Eric Mustin** 17:08 Right.
**Kayla Reopelle** 17:08 Thanks.
**Eric Mustin** 17:10 So these are for… wrapping… like, Log Rage or something, or….
**Kayla Reopelle** 17:18 Usually.
**Eric Mustin** 17:18 Okay.
**Kayla Reopelle** 17:19 Eventually, we'll have, yeah, like, longer age, I think semantic… logger is doing it as a first-party thing, so we wouldn't have to… Yeah. But, yeah, I guess, do we want to group all of the log?
Stop into its own directory.
Or keep it mixed in.
**Eric Mustin** 17:35 I, … I don't know, I feel like it would be nice if there was a way to indicate signal, like in collector, processors and stuff like that, there's, and instrumentations, like, you know, they don't have, like, instrumentations, but whatever, they're receivers and, like.
they mark the signal that's supported by it. I don't feel like we have a corollary to that, where, like, we're using directory structure, so it would make… and just from a… You know, it seems like a common… When, you know… a common… question people have, it would be nice to be able to point people to a folder and just say, go look in there. So, yeah, short, like.
That being said, like, if it's complex to do, and we think we'll create, like, we could paper over it with just some sort of, like, matrix of… Saying these instrumentation, like, documentation could just… kick the can on this problem, if you feel like it's a problem. But I don't, … Know of or have personal experience with the, loggers yet, so… I would be, you know, deferring to… whatever, you know, Wendy or Kayla, whoever is Touching that… those packages.
**Kayla Reopelle** 18:46 Right.
Cool. I think, you know, having… Separate directories for signals.
… makes sense, though I think eventually we will probably want metrics and traces to be emitted from the same instrumentation gems. … Just to avoid continuing to….
**Eric Mustin** 19:09 Yeah, yeah, I guess that's right. That's… … Yeah, I wonder, what's like… Who would ever, like, yeah, I guess the logging… these logging, like, monkey patches are sort of weird, ….
**Kayla Reopelle** 19:22 Yeah. In the sense that….
**Eric Mustin** 19:23 They're logging libraries. Yeah, not, ….
**Kayla Reopelle** 19:25 Yeah, they do some….
**Eric Mustin** 19:27 … I, … okay. Yeah, I mean, alright, what is Go, like, … what is it? Go calls and bridges?
Yeah, yeah.
**Kayla Reopelle** 19:36 They do have their own directory, but basically Java and JavaScript don't, and it doesn't look like Python's written any… yet.
**Eric Mustin** 19:44 Hey, young.
certainly someone who's not, volunteering to do the work. My… I think it's okay living in instrumentation, and it can be something… you have, you know, documentation for, like, you know, but … Yeah, I, … I couldn't even tell you how many metrics, you know, libraries we have, and whether that's, … Whether people are getting confused on knowing what can, you know.
**Kayla Reopelle** 20:13 Yeah.
**Eric Mustin** 20:14 You know, I'm at Metric, so I, ….
**Kayla Reopelle** 20:16 We don't have any metrics libraries yet, but….
**Eric Mustin** 20:19 to hear Rob or Ariel or some other folks who have, you know, use cases.
**Kayla Reopelle** 20:22 Sure, yeah. And I guess we have, like, users, too, in terms of discoverability. Do you think it's, … is there a benefit to having something in, you know, a bridges directory versus just in standard instrumentation?
**Eric Mustin** 20:36 Alright.
**Kayla Reopelle** 20:38 I think another concern was that, like, if it's in instrumentation, should it go into the instrumentation all gem and get installed automatically, or be separate?
**Eric Mustin** 20:47 Yeah.
Yeah, I'm just thinking of the, lift of, like, we have… I feel like we have the word instrumentation hard-coded into a lot of our, like, release pro… you know, stuff like Daniel, you know, those toys gems, which do some of the CICD things, and I'm just… you know, would be, like, scared of Eddie, touching you, you know, like, it's a Rube Goldberg, situation, so, … Yeah, I, you know, I, ….
**Kayla Reopelle** 21:16 I mean, we do have, like.
**Eric Mustin** 21:18 as long as it's in Markdown, you know, somewhere, the LLMs will ingest it and will tell the users the truth, and it'll be fine.
Just rambling, apologies.
**Kayla Reopelle** 21:41 Alright, well, … Yeah, we can, we can chat about this more… Outside of this meeting, just was planning to bring it up, and … maybe I'll just go through the exercises.
**Eric Mustin** 21:54 What do you like to do? Yeah, like, what would be your inclination, having done the work here?
What's your opinion?
**Kayla Reopelle** 22:00 I think my… Initial opinion was to leave it in instrumentation to make it you know, when it becomes stable, easier for people to install, easier for people to discover. I guess I'm worried about it getting potentially lost if it's in a different directory, but it does have a different name inside of the specification. You know, they do call them bridges, it's not instrumentation.
So… I… I could… yeah, I think I could go either way. … we maintain so many gems as part of Contrib that, I think trying to simplify things is sometimes nice, but I don't want to simplify things unnecessarily.
**Eric Mustin** 22:44 Yeah.
Okay, I, … Yeah, I just, I… you know, I think if you could snap your fingers and have it, like, you know, re-architected, it would just spit out, like, a new tree, like, that would be cool. I'd just worry about… yeah, I don't… I don't want to over, promise, or force you to, you know.
Might be a good, exploration to document the areas that will require change, like a larger ticket, and if we feel like that you have bandwidth to do that work, or someone has bandwidth.
prioritized, can also be something, like, I feel like those are good to put for when we do our inevitable, like, wishlist type things, then it's… but yeah, again, I'm not putting in cycles here unless it's, … I don't know.
Priority, so….
**Kayla Reopelle** 23:30 Okay.
Sounds good.
Yeah, Eric, you're up next.
**Eric Mustin** 23:35 We can do… this one was not particularly, … this came up, someone was asking in an internal chat about the SEMCOM changes for .NET. They were complaining that people were … Yeah, it's in .NET, and they've been implementing… someone made a PR that was incorrect, it didn't have the, stability flags, and they were asking about it, and… but it… when I was looking into .NET, I noticed that they did have, and the guy who made the PR wasn't, like, a maintainer, but, it surfaced this milestone for this income, and I thought that was a useful one, just, like, a resource that maybe we can, crib from, especially with some of the implementation details here, which, yeah, look like a hassle.
Hassle is not a hassle. Look hard. And … and yeah, I don't know. I was just like, oh, a milestone, people use that. So I was just surfing it for you, really for you, Hannah. But I haven't actually reviewed… I saw you put up the trilogy and MySQL PRs, I haven't had a chance to review them by solos, and I was just sharing.
**Hannah Ramadan** 24:35 Yeah, no, this is helpful. I was just taking a look at it. I really like the way they organized this. It's pretty clear. I think that.
**Eric Mustin** 24:42 Yeah.
**Hannah Ramadan** 24:43 I mean, I guess they're doing… it more from, like, a sequel, like, as, like, per library, with, like, sample conventions and new attributes, versus, like, we were kind of….
**Eric Mustin** 24:54 I think, I think their SQL world, or, like, their… I think the… and correct me if I'm wrong on… I'm not a .NET person, but, you know, given the pace of Microsoft Script.
**Kayla Reopelle** 25:06 Oh.
**Hannah Ramadan** 25:07 Nope, there he goes.
**Kayla Reopelle** 25:10 I guess I've cut them off.
Okay.
But yeah, this is pretty, pretty cool, and I think, we were talking about some of the issues about adding, you know, missing conventions. This seems like a great way to track those, like, things that we're not currently recording and aren't just a translation.
**Hannah Ramadan** 25:32 Yeah, yeah, I definitely… I want to go through this. I'm noticing, like, they have some… like, outdated spec info. So, like, for the operation name and collection name, parsing that from query text, like, that's been updated to no longer, like, support that, so I might, like, chime in and just be like, hey, y'all, like… Double check that.
**Kayla Reopelle** 25:53 And… Yeah, you could… you could reach out to Alan, too, to check in with… Best practices, since he's worked.
**Hannah Ramadan** 26:01 Yeah, definitely. It's nice that all the agents are kind of going through this.
**Kayla Reopelle** 26:07 Yup.
**Eric Mustin** 26:14 Alright, my computer died.
**Kayla Reopelle** 26:16 Oh, bummer.
Welcome back.
**Eric Mustin** 26:19 I'm disorganizing and plugging my computer. … I think it's just, like, Rack and Rails, like, where it's, like, a multi thing, … is, like, their SQL, you know, SQLRM, ecosystem is, like, you know, SQL, then, like, special SQL. So, like, … Anyway, that's all I got.
**Hannah Ramadan** 26:35 No, perfect, I appreciate you sharing. And I'll… I don't think there's an open issue right now for tracking Ruby work for database semantic conventions, so I'll get that created.
**Eric Mustin** 26:48 Oh, man, it's cool to… it's easier said than done, I think, with… It's cool to see people, like, some of these, like, immaculately maintained milestone tracking things, and then the reality is, like, it's incredibly time-intensive to do, so, you know, all good.
**Kayla Reopelle** 27:07 Nice.
All right, Michal?
**Michał Kaźmierczak** 27:12 Yes, so I will repeat a little bit myself from the introduction. So, I joined because, I worked on the gRPC instrumentation, instrumentation, of course, tracing.
And, I saw that there is a nice adaptation of this gem, at least by the number of downloads on Ruby Gems.
However, we only have the client side currently, and I was just curious, you know, if I want to offer some time to contribute to the project.
Do you think, like, adding the server instrumentation is the right thing to do, or, like, there are other projects or other… Topics that you think are, better to work on?
I think this is probably a broad question.
**Kayla Reopelle** 28:09 I mean, I think we haven't had anyone reach out to us about the server instrumentation, but that doesn't mean there isn't a desire for it.
So I think to create a complete instrumentation would be excellent. I mean, there's semantic conventions out there, and I think the ideal situation is that we can emit all of the semantic conventions that are available for any of the libraries that we instrument.
So, I feel like for that reason, adding the server would be great.
We have also had some other gRPC-related requests in the core repository that we haven't been able to address yet related to gRPC exporters, so if that interests you, that could be another opportunity.
… Like, for example, we have a… OTLPAGRPC exporter for traces that hasn't been released, because it doesn't really have sufficient tests.
But if it were to get sufficient tests, I think it could, you know, be ready for release, and we have had a few people reach out to us about that. So, if you wanted to continue on to your PC contributions, that could be another place to look, but if you feel, yeah, confident about being able to implement the server.
instrumentation on the JRPC, instrumentation gem. I think… I think that would be a great next step.
**Michał Kaźmierczak** 29:34 Sure.
So, do I understand correctly that, currently, the exporter only uses HTTP? I mean, the standard… okay, so… even though this says implemented, it's not, like, released, or….
**Eric Mustin** 29:49 Maybe I can provide some minor, or, like, some Chesterton's Fence-type context, which is, I think, originally, I think the specification a lot generally defaults to GRPC, but… … it allows for language-specific choices there, and so Shopify, which was, … I think did a lot of the work to migrate these specific gems, and was… some of the early maintainers had historically had some internal issues using gRPC as a transport mechanism, and so they def… they… you know, there was a preference to… and just, I think, generally in Ruby world, there's some… folks have some struggles, maybe there was more struggles during the… when it was, like, you know, the M1 days, and they were moving, you know, arm, … That's compatibility delays. So anyway, so it just never… we just defaulted to HTTP at the time, because it was, yeah, it was more robust, and so I think the open… there's always been an openness to revisit those conversations, depending, on… yeah, I don't know, who's, … who needs what, but the reality is just, like, this work never got prioritized. It wasn't like there was some fundamental reason why it wasn't getting done, it just wasn't getting… prioritizing, I think not many people have asked for it. So, yeah, this would… but it would be helpful to get finished and released, and any expertise, I think… I think we were, you know, it could have just been also, like, us at the time didn't have the expertise to have confidence, so we just went with, you know, HTTP. … But yeah, I think, back to the original question, like, for sure, especially if… it sounds like some of the other adapters out there have server support. I looked at DD TraceRB, which is like a… where our instrumentation originally was donated from, and they… it looks like they have a server implementation?
So, yeah, I think, like, just coming from… our number one thing, or one of the things we often get is, like, folks coming from, you know, they're migrating from some other library to OpenTelemetry, that migration is mixed, you know, across their languages, and so, yeah, definitely, like.
That'll get, you know, stuff like that comes up, where it's like, oh, we had this.
it was getting lit up in our… in this one format that we were instrumenting, and now we've moved libraries, and it's suddenly dark. We're missing those stats, or those spans, so I… it would be super helpful to have, … Better levels of interoperability with some other standards out there. … You know, selfishly.
if you just want to do, like, really good metrics through gRPC, like, I think that'd be the most, that'd be awesome, too. But yeah, yeah, any works, like, yeah, yeah, for sure, I think, I don't know. And I, … I don't know of any gotchas. I don't have any, you know, … I don't… or, you know, I don't have any helpfulness in terms of the implementation, but I think we would definitely be open to it if you have cycles.
And you're already a maintainer, so, you know, let it rip.
**Michał Kaźmierczak** 32:53 Okay, yeah, so I think I would tackle that. So I will start with the server gRPC instrumentation, just for the completeness, right? We want to have it just both for clients and for… Or server. And then, let's look into gRPC exporter. I know that, you know, Ruby and gRPC was a difficult relationship in the past. I mean, there were plenty of issues with compiling the gem and so on.
But, as you said, maybe we could revisit those, those, those, those problems and see if it's the, … If the problems are still valid.
**Eric Mustin** 33:33 Yeah, yeah, I, you know, don't, … Don't mistake anything here for, … the cosmos, it's just, you know, was the reality. You know, some of it was just practical realities of implementation at the time, so, ….
**Michał Kaźmierczak** 33:47 Yep.
**Eric Mustin** 33:48 there's other, you know, other, … I wish the, some of the other folks who are some of the larger, users would have some… might… may have some contacts, so definitely, like.
If it pops up again, or it might be good when, you know, Arielle or Robert or something is back in, Kayla, like.
ping them and see if they have any specifics, because they may have some, yeah, just some, like, skeletons in the closet. They're… they're war stories they'll share, and that might, you know, help everyone avoid some… some rakes, without getting too… you know, I'm being vague and using a lot of big words, but … Anyway, yeah, it's cool to, … I think it's cool to have interoperability, so awesome. I appreciate, … Appreciate you offering to work on it.
**Michał Kaźmierczak** 34:32 Sure, thank you. Then my… my topic is, is clarified.
**Kayla Reopelle** 34:38 Excellent.
Yeah, okay, so… That covers our main agenda. … Wendy, I guess, yeah, does anyone else have other things they want to talk about specifically?
**Wendy Smoak** 34:55 The milestones example looked really good, because I'm struggling to kind of get a handle on what… specifically with metrics, what's… going on exactly? Is there anything that's already committed that's likely to just change out from under me, or is, like, what's in there and working pretty… like, I know it's still in development, that's fine, but… Are there big changes coming? What is your sense of… Of just, kind of, the… Level of stability.
And then how do I kind of… like, the milestone thing looked great, like, if I could go to a thing and say, like, here are the list of things that need to happen, because I'm just digging through issues and trying to figure out, is anything broken? Is there anything I should… are there any sharp edges in here that I should watch out for?
That's… and is there anything I can help with?
**Kayla Reopelle** 35:48 Awesome.
I think there's a lot more that we could do to verify what's available. There is this metrics milestone that hasn't been, I think, thoroughly maintained, but there are some… there's some automation associated with it that's doing things.
So you can kind of see the issues that are done, or pull requests that have also been tagged with metrics, things that are in review right now.
But I… I should probably do a more thorough audit about where things are at right now to make sure that this is accurate. But this is one resource, and I think given some of the questions you asked recently about, you know, like, the gauge and things like that. There's also a… oh no, I have to sneeze.
Oh, that's not gonna happen. Okay, there's a SPECT compliance matrix that, I'm working on updating.
As well, this is available for all of the languages, and I had been kind of hesitant to update it for metrics or logs, because I wasn't… really sure if, like, something being supported meant it had to be stable or not, but, I think just kind of checking out to see the plus signs for some of the other implementations that have things in development, it seems like, you know, if it's been implemented and we think that it adheres to the spec as a language SIG, then that's okay. So, I can send that pull request to you when I do open it up, … So that you can take a look, too, to see… Because right now, yeah, it looks like Ruby doesn't support anything on metrics, and that's not the case at the moment. I would say right now, exemplars are one thing that we don't have support for, but I think there's a pull request that I need to review to add support for them. I'm trying to think of what else. I mean, the asynchronous metrics, you know, are available on main right now, but they're not… … Not released inside of the gem itself.
I'd say one… bigger… restructure that could be a problem is that… is this refactor? I don't know if this will potentially change some of the APIs that we're using.
But, an initial design choice that we made doesn't really align with, some of the other implementations, and we're encountering… some complexity in our exporter because of it, and so we may need to kind of change how some of the classes are structured and what their behavior is like in order to get things to work. And because it's at a zero… level, like, major version. We will have breaking changes in the minor versions, but we'll try to make it clear in the changelog when they are happening.
So, does that help answer your question?
**Wendy Smoak** 38:39 Yes, yeah, I just wanted to… just kind of get a lay of the land and see. I'll keep an eye on that one.
**Kayla Reopelle** 38:45 Do we….
**Eric Mustin** 38:46 Do you have any instrumentations that emit metrics?
**Kayla Reopelle** 38:50 We have a lot of sweet PRs that, need some love, but no instrumentation at this time. So there's a few different, approaches. We had someone… come in and submit a lot of PRs for metrics in January. It got kind of… bogged down in discussion and abandoned, but I've had some more time to review PRs lately, and so I was hoping to get back into them. I think the first thing for metrics and instrumentation is we need to decide on a format, because metrics aren't stable, but traces are, and I think the best solution is to keep them inside of the same gems.
But we need to have some clear toggles to make sure that it's off by default, and, like, separation to kind of avoid conflicts.
We were waiting for the semantic conventions, stability environment variable to get integrated as well before we added metrics to instrumentation, so that way we can only add metrics for the new and stable conventions, and not need to go through that whole rigmarole of, like.
different attribute names and stuff. So, since Hannah's work is almost complete, I think HTTP metrics is where we'll probably start, and get those released first, and then move into database queries when that one's ready.
**Eric Mustin** 40:08 Cool.
Yeah, I'm still….
**Wendy Smoak** 40:12 Oh, good.
**Eric Mustin** 40:13 No, I was gonna say, … That's not important. Yeah, I was gonna say that, you know, sharp edges, I feel like, If we look back, you… we won't know until people get automatic instrumentation emitting metrics, and then we'll… we'll figure out, really, we'll get we'll figure it out. But, like, just… that's how I've seen this go in the past, is that's kind of the gate that I would apply. So yeah, I would certainly proceed with… I wouldn't… I'm not trying to, you know, negate anyone's work, but proceed with caution, for sure.
**Kayla Reopelle** 40:45 Yeah.
**Wendy Smoak** 40:46 Yeah, nothing's instrumented. These are just explicitly counter… create a counter and increment it, and if there's some gauges….
**Eric Mustin** 40:53 use cases, yeah.
**Wendy Smoak** 40:54 Yeah, just plain, like, nothing. We did logs, we're just, like, barely doing metrics.
So, really the simple stuff. And does the SDK itself have any metrics? I'm specifically interested in how much memory is it using? I did manage to run out, like, on the 1st, which is a busy day, we dropped some logs because the buffer filled.
**Eric Mustin** 41:15 Mmm.
**Wendy Smoak** 41:16 So, is there… like, I'm trying to get a handle on how much memory is the thing using, and, like, I probably need to bump it up, but I don't… I'm guessing.
**Kayla Reopelle** 41:24 I don't think that we have anything that's automatically recorded right now, but I think there might be some semantic conventions around memory that we would eventually….
**Eric Mustin** 41:34 So, there's a hack, is in the, … for… like, there's some metrics that the SDK… that this gem emits.
… But not, … I wouldn't say there's, like, runtime metrics. There are a few… there's a hook in the, … Oh gosh, I gotta find this.
**Wendy Smoak** 41:54 You can ask in the channel, we don't have to, like.
**Eric Mustin** 41:55 Damn.
**Wendy Smoak** 41:56 I'm going over this, too.
**Eric Mustin** 41:57 There's basically just, like, a class, an empty class that's been implemented, so you can, like, provide your own metrics class that has some… … basic… that will emit some basic metrics on… on just, like, traces emitted, like traces in the, you know, a couple things on, like, failed… failed to emit, you know, thing… Things emitted, like, one or two other things, so you get some basic, like, throughput monitoring, which is just a, … you know, and I think that the… and the subtext there is, like, we had a… Shopify had a StatsD implementation that, you know, was just, you know, what we brought our own. It wasn't part of this thing, it was just for our own monitoring. It wasn't, like.
So yeah, there's a, the metrics reporter class, so if you, you know, you can provide your own metrics reporter, or module, And so you can get some metrics out of, like, the core batch span processor and core exporter path, but it's not on… you'd have to ballpark your own, you know… you can use it, they're helpful, especially when you pair it with collector metrics.
You can generally figure out where the things are dropped and for what reasons, what error codes, but it will not get, you know, it's not going to give you memory out of the box or anything like that.
So yeah.
**Wendy Smoak** 43:10 That was the thing, like, I don't know whether the… I don't know whether it filled up because the hotel collector was unreachable, or… because I don't, like, I just don't have everything correlated yet. It's brand new. I just saw the….
**Eric Mustin** 43:18 Yeah, this was our hack, that it worked, like, it helped… it was definitely helpful for same… same exact things, like buffer, oh, super spiky, like, hey, the, you know, guy doing data science thing, super spiky traffic, you know, all of a sudden, and then the buffer filled up, and we didn't know, and then these metrics said, like, yep, you're getting fails related to this, you know, attribute status code. ….
**Kayla Reopelle** 43:37 So, okay. The only gotcha I would add is that this has been implemented in traces, but we didn't add it to metrics and logs. Right, right. So, you'll have to use this Sorry, so it won't be helpful at all.
**Wendy Smoak** 43:51 kind of thing will work for logs, if I just….
**Kayla Reopelle** 43:52 Exactly. Yeah, yeah, precisely.
**Eric Mustin** 43:55 Well, well, it's slightly more… I guess, does… it uses the same batch span processor and exporter? You'd have to pretty….
**Kayla Reopelle** 44:02 The batch log record processor is really good for the batch scan processor. I think you could kind of copy and paste the same work over.
**Eric Mustin** 44:11 Yeah, there'd be some monkey patches along those, too. But yeah, it could be done.
**Wendy Smoak** 44:16 Thanks.
**Kayla Reopelle** 44:26 Okay, cool. Anything else we want to talk about today?
**Wendy Smoak** 44:33 I can do one of the happy reports? Like, what do we need to do to get logs out of development? I'm seeing….
80,000… I don't know, I don't… I don't have a… I don't have a metric for the size, but we're doing 80,000 logs a minute that I can see in….
**Kayla Reopelle** 44:49 Wow.
**Wendy Smoak** 44:50 And… Good spot!
**Kayla Reopelle** 44:54 That's really exciting. … I… will start reaching out to the… technical committee to see what we need to do, because I think having one, like, power user is kind of the minimum step. I know we've had it out for a while. I know that there's other folks who are using it, but I haven't engaged with them as much, so I'll take that out.
**Wendy Smoak** 45:20 I got permission to make sure we could, like… it's obviously, I mean, you can look on LinkedIn and see where I work, it's not like it's a secret, but… I checked with my boss and make sure that….
**Kayla Reopelle** 45:29 Okay.
**Wendy Smoak** 45:30 So, yeah, it is, it's… well… It's in production, but not, like, really being used yet, so… Yeah. We're dual right now, comparing things, so… But yeah, I'm not having any problem with the batch log record exporter, other than, like I said, I think we need to bump up the memory from the default.
Because I'm pretty sure we just ran it out.
And then, same deal. Is there any, like, are there any… things missing… I'm using just basic stuff, so maybe there's other stuff that has to be implemented before it could be final, or whatever the next thing is, so….
**Kayla Reopelle** 46:04 Yeah, I was doing that spec compliance assessment yesterday for logs as well, and we're really close. There's a few things that were added, since that initial implementation came through. I think it's, like, being able to enable and disable a logger through configuration, and being able to enable to disable a log record processor.
And then there was one other… spec line that didn't really make sense to me, but I… I'm not sure if those are required to reach stability or not, because I believe that they're also in development right now, so… We might… it might be okay, but, … Yeah, those are the only things that I'm aware of that… Are where we deviate from the specification.
**Wendy Smoak** 46:49 Yeah, I mean, I'm fine. I've read the code, the code works, it's just a marketing thing. Like I said, you weren't here last week. Like, this is completely marketing. When I show it to people at work, they're like, it's in development, it's not ready yet. Like, no, really.
**Kayla Reopelle** 47:01 Read the code.
**Wendy Smoak** 47:01 But it's right there.
**Kayla Reopelle** 47:02 Yeah, yeah.
**Wendy Smoak** 47:03 It's completely us.
**Kayla Reopelle** 47:04 Nice.
Well, yeah, and I….
**Wendy Smoak** 47:07 on it.
**Kayla Reopelle** 47:07 I would also selfishly love for it to reach stability as well, so that I could… I could close that… that chapter and move it into a new mode. So we'll see… yeah, we'll see if it's possible. Thank you for that.
**Wendy Smoak** 47:18 Enjoy your work on it.
**Kayla Reopelle** 47:19 Yeah, yeah, happy to do it.
**Eric Mustin** 47:21 Alright.
**Kayla Reopelle** 47:25 Cool. Alright, well, if we don't have anything else, then, I'll see you all on GitHub or Slack, until next week, and yeah, reach out. Don't be strangers. Thanks for coming.
**Wendy Smoak** 47:38 Thank you.
**Eric Mustin** 47:39 Right.
**Michał Kaźmierczak** 47:41 Right.
