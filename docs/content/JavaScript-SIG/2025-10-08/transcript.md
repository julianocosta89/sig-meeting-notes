SIG: JavaScript SIG
Date: 2025-10-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marten Hennoch 00:00:37 Hello.
MG Marylia Gutierrez 00:00:39 Hmm.
Marten Hennoch 00:00:42 Finally, someone joined. I thought I'd joined some wrong meeting.
MG Marylia Gutierrez 00:00:49 Yeah, a lot of times on this one, people join, like, on the one minute, and yeah.
Marc Pichler (Dynatrace) 00:01:08 Hello?
MG Marylia Gutierrez 00:01:10 Hello.
Marc Pichler (Dynatrace) 00:01:48 Alright.
Let's get started.
The first topic on here is, from myself.
There is… a PR open right now, that will drop the lazy loading of the Jager exporter and SDK node.
I'm just here to make everybody aware that, This is happening right now, and if you have any objections, please note them on the PR. This is mainly to make sure that Pandlas can… actually take SDK node and, no.
bundle those up. We already have a few approvers, so, Yeah. If you have any objections to this, please note them there, or if you want to give it a review, the changes are fairly… Fairly simple, a bunch of remove tests, and the… actual change in the business logic. But other than that, it's fairly straightforward.
Yes, that's it from my side. If nobody has any questions about this right away… I guess we can move on to Marilla's topic.
MG Marylia Gutierrez 00:03:24 Yeah, just sharing, like, the PR. So that was the one that I say, like, I was not gonna put this on the other PR, because it was gonna already get too big, and this is just for the provider, and it still got big, the PR, but it's just pretty much straightforward, this one, and I use the same thing.
This one that had a few examples similar to the other that is just an object of null , so I kept this the object of this one. So it just looks big, but it's a little straightforward.
And then I'm… soon we'll open the… for the logger provider and the meter provider, because the meter is even bigger, so one day I'll finish them.
Marc Pichler (Dynatrace) 00:04:04 Right?
Sounds good. I will definitely have a look at this one as well. If anybody else has some time to look into this, please feel free to go ahead.
Trent Mick 00:04:16 Total, total naive question, Maria. Has there ever been discussion in this or the other languages about and this is super naive, like, I haven't even looked at this PR, but of generating Code for the config model based on… This schema, because there is a schema for…
MG Marylia Gutierrez 00:04:35 Yeah. Even James turned on the account, because actually there is… and I actually created an issue for it, to actually do this, so Java does that, but I just… didn't know how to do this on the JavaScript, so I kept, like, pushing, like, one day? So I opened an issue, and I think Jamie might look into that one.
Trent Mick 00:04:56 Okay, cool. Cool. Thanks.
Marc Pichler (Dynatrace) 00:04:59 I have… I've used QuickDype before. I'm not sure if that is, commercial… thing now or not.
I use it in another language, I'm not sure if it… works for TypeScript as well as for what I used it for back then.
MG Marylia Gutierrez 00:05:18 Yeah, my mind was like, why take some time to optimize something if I can spend, like, 2 weeks doing that instead just manually, right? That's how it works.
Marc Pichler (Dynatrace) 00:05:29 I think you have more control over, how the actual config model looks like when you do it yourself, though, so it might be that, when Jamie looks into, the… Like, generating the types from it, the types may be kind of difficult or annoying to work with.
So, then changing that is, is kind of… annoying and difficult. That's also the thing that I ran into with, what I had worked on before was that, like, then the types were so annoying to work with that I had to do it myself anyway in the end. So, something to keep in mind, I guess.
Jamie Danielson 00:06:16 The other possibility I can see, too, like, so if, like, we timebox it, see how it goes, even if we don't use it directly, but have it as, like, a reference or something to test against to make sure that we have the latest of whatever there is, that could be useful.
But yeah, I think it makes sense that we have something manual so we can keep moving forward, and then we can compare.
If we figure it out. If we figure out how to do the thing.
MG Marylia Gutierrez 00:06:38 Yeah, the one thing that I'm doing, like, I'm copying as is, is just the example. They have two examples there that every time there is, like, a new change on spec, they update this example, like the kitchen sink. So this is the one that I, yeah, I just copy as is to make sure that whatever I'm testing is the same one, and also the migration one that is recommended. So those are the two examples that I always use, at least it Should be, like, handle all cases, pretty much, at least that helps a little.
Jamie Danielson 00:07:08 That's definitely the idea of it.
I don't remember… oh, we do have a README.
MG Marylia Gutierrez 00:07:16 Do you want me to assign you to the issue, Jamie, or…
Jamie Danielson 00:07:21 Oh, yeah, sure. Yeah. The configuration model from SchemaSpec.
MG Marylia Gutierrez 00:07:26 Yeah.
Jamie Danielson 00:07:27 Yeah.
Yeah, I have that on my list this week.
MG Marylia Gutierrez 00:07:37 The gist was not a naive question, Trent.
Marc Pichler (Dynatrace) 00:07:48 Right? Is there anything else we want to talk about on the config?
site.
If not, I guess we can move on to the next topic. This is, martin? .
Marten Hennoch 00:08:09 PR to a package without Codola. So I have this PR… Which… Well, I need to do this for a bunch of languages, but the specification exists for a SQL Server.
Which someone, for some reason, uses.
I have one for Oracle also, but Oracle has a maintainer. We used to actually maintain this tedious package. Rauno… Rauno authored it, but he left, so… I could become a co-donor here, because I need to add another stuff here also.
So my question was, will it ever get reviewed if it doesn't have a code owner? I kinda need it…
Marc Pichler (Dynatrace) 00:08:52 com…
Marten Hennoch 00:08:53 gigs.
Ideally.
Marc Pichler (Dynatrace) 00:08:55 Yeah, so, features, usually somebody who is an approver, can go in and sponsor these. So basically by just going in saying, I'm a sponsor, I'm gonna review this, I'm gonna be responsive to any sort of, bugs that might appear,
Marten Hennoch 00:09:14 This is luckily behind the configuration flag, so it's disabled by default.
Marc Pichler (Dynatrace) 00:09:21 Yeah, but that's how it usually goes.
also the expectation when somebody comes in and actually reviews this and this gets merged, then, the person who's reviewed that is supposed to, also triage bugs and stuff like that that come from it. That's… the ideal way that this would go, but, it doesn't always, happen exactly the way.
Marten Hennoch 00:09:47 Someone…
Marc Pichler (Dynatrace) 00:09:48 So yeah, finding someone who would be interested in also driving this forward would be one way, or becoming a component owner is also one way of going about these things.
Marten Hennoch 00:10:02 Can I improve myself?
Marc Pichler (Dynatrace) 00:10:04 Yeah, that's, that's the problem there. So if anybody else is interested, like, that's the reason usually why we have two component owners required.
Marten Hennoch 00:10:15 They're working on a spec to have this for all of the database libraries.NET has it already.
Java has it to an extent, this set context stuff.
Trent Mick 00:10:29 Are they all making it, Opt-in as well.
Marten Hennoch 00:10:34 Yeah, I think that specification, I think, says that it needs to be opt-in, if I remember correctly.
Trent Mick 00:10:40 Probably because it's still in development, but…
Marten Hennoch 00:10:41 Yeah, and it, add some overhead.
Okay. And here it… they want to do it with the SQL commenter to add comments, but there was some… the spec for that is actually, I think, also approved now, but there was this… Google donated this SQL commenter, but it was in limbo for a long time, but now I think it's moving somewhere.
Trent Mick 00:11:07 But this is.
Marten Hennoch 00:11:09 Those are true.
Trent Mick 00:11:09 way.
Marten Hennoch 00:11:10 Yeah, for a desk or a commenter… For some reason doesn't… they don't want to use it for, Oracle and… no, Postgres and SQL Server, for some overhead reasons, I think. There was something with comments. They prefer to set context.
Trent Mick 00:11:28 Okay. Is that because you can't do… caching, or…
Marten Hennoch 00:11:33 Something, because the… I'm not quite sure. There's something about cardinality also, but…
Trent Mick 00:11:40 Anyways, this is in the spec.
Marten Hennoch 00:11:42 And, .NET and Java did it like this. I'm not sure if it's in Java upstream, but it's in our Java, but .NET is for sure upstream.
Trent Mick 00:11:50 Okay. I'll sponsor this one.
Marten Hennoch 00:11:53 Thanks.
Marc Pichler (Dynatrace) 00:11:54 Thank you, Trent.
Marten Hennoch 00:11:58 And.
Jamie Danielson 00:11:59 I was gonna mention, if you have the link to it, also might be useful to throw it into the PR description.
Marten Hennoch 00:12:03 Yeah, I'll update this.
I'll update the other PRs here, I'll link to other PRs.
Jamie Danielson 00:12:08 Like, minimal friction, like, okay, that makes sense.
Marten Hennoch 00:12:12 They're doing it together.
Trent Mick 00:12:14 Languages, you mean, or what?
Marten Hennoch 00:12:15 Yeah.
Jamie Danielson 00:12:16 Yeah, like the .NET implementation, or, like, if we have links to that.
Marten Hennoch 00:12:20 Yeah, they were able to do it in a much higher level, though. I mean, here we have to, like, do it library by library.
Jamie Danielson 00:12:28 more of an implementation thing where, like, if things are still in development or something, it's useful to know, like, if other languages have done a similar thing or the same thing, like, that kind of helps know that, okay, this is something that is being implemented. It's not, like, a one-off.
Marten Hennoch 00:12:43 Yeah, all of the testing really worked out of the box, someone worked on it, they saw the test services thing.
So it was really handy.
even worked on my Windows machine. The testing for the country stuff, like, all of the databases.
Trent Mick 00:12:58 Nice.
That's David.
Marten Hennoch 00:13:01 Yeah.
Trent Mick 00:13:02 Thanks for that.
Marten Hennoch 00:13:02 Thanks. Yep. So that's it.
Marc Pichler (Dynatrace) 00:13:09 Alright, I guess it's, sorted out now.
Yep.
Aww.
Trent Mick 00:13:20 That's always fun. Yeah, that's good.
Marc Pichler (Dynatrace) 00:13:21 Oh, sorry.
Trent Mick 00:13:22 I filled time, because… I don't want to do as much triage. Ask about config stuff, so this is the off-the-cuff, unprepared questions for Aurelia, I guess.
the… Reading through the config spec stuff, it's still… configuring instrumentations is still pretty much in limbo, is it? Or under-specified?
Is it?
Does that sound accurate? Well, I mean, so if you go look at, The kitchen sink, for example, in some of the write-ups, there's this, like, instrumentations section.
MG Marylia Gutierrez 00:13:59 Which is…
Trent Mick 00:14:01 has no details and stuff in it. I guess it has the instrumentation.general section.
MG Marylia Gutierrez 00:14:07 Yeah, one thing I would say, like.
a little careful with the naming, because a lot of people that were creating those things were, like, in Java. And Java, they have one core repo, one instrumentation repo, and then one contrib. So a lot of the things they were naming based on, like, oh, this is how you should separate, but that is not how we separate, for example.
A lot of the things that… they see sometimes it's just, like, extra instrumentation, sometimes, like, third party, they consider, and sometimes instrumentation. But all the core, like, for example, all the, like.
providers or, like, loggers and stuff like that is part of the main, which is our instrument.
Trent Mick 00:14:49 So that was configuring the SDK stuff, yeah, that seemed fairly straightforward, because… I think probably straightforward mostly because configuration of the SDK has been specced already with the environment variable stuff, but configuring instrumentations is still Wild West, so it… that felt a little bit glommed on. Yeah, okay.
MG Marylia Gutierrez 00:15:07 Yeah, so the…
Trent Mick 00:15:08 about the, extensions stuff, because I was going through trying to think… we've talked about having extension support, and Java does already And so they kind of gloss over in the configuration stuff about how… if, in the config, you run into a my exporter kind of thing, then obviously this is the way you do it in Java, but, like, other languages or JavaScript, I'm being… just talking about JavaScript, there's no extension mechanism, there's no way to map a name that you see in a config file currently to… some implementation of an exporter kind of thing. Have you… have you started thinking about that, or is that kind of, like… Get their willingness.
MG Marylia Gutierrez 00:15:48 Yeah, it's a little… yeah, a little more ahead, because, like, they just preparate an area saying, like, this is for specific if you want to add something. So we do have a place if you want to add, like, JavaScript-specific stuff, but I didn't got to that point yet.
Trent Mick 00:16:04 Fair enough. Okay, good.
I want to make sure I'm not rethinking stuff that's been thought about already.
Marc Pichler (Dynatrace) 00:16:10 I think I've seen, where was this? No.
For instrumentation.
There's always these, pattern properties… thing for it?
basically just allows you to put any key in there, and I guess the config model, once it's parsed, would spit that out as an unknown, type.
And, if we have some way to route it to, which instrumentation it's supposed to go to, Then… I guess… There could be… like, not for this one here, of course, but there's probably other places where this is used. We have some way to route it to the instrumentation, and then have the instrumentation, check If the config that's being passed into it is actually valid for itself.
It could be done with, what's it called now? There's these small extensions that you can use to, like, create the SDK components, Based on config.
Trent Mick 00:17:25 Yeah, I forget the name that they use, which I've asked some names for it.
Marc Pichler (Dynatrace) 00:17:27 Yeah, that was the one that I was initially very confused about what it was doing. Then that could be one way of facilitating this extension thing.
that still doesn't serve the, like, how would we initially load it, but, it is somewhat extendable, I would say.
MG Marylia Gutierrez 00:17:51 Yeah, my concern was, like, adding a lot of extra stuff, because, like, that configuration package, I want to keep, like.
small, and it's not even, like, creating any of the components. It's just parsing, like, returning, this is your model.
And users can be, like, environment trouble, or config file, but then whoever's using don't have to think about it. And now, that is, like, my next step. Now I'm going through, like, the SDK nodes package, importing this, and on that one, I'm gonna create, like, the create SDK, crates, whatever. So, then it starts to get a little tricky for, for example, if there is any extra checks that you want to do, do you do this?
On the package that is important, or in the package that is parsing, because then you want to know right away if the parse was wrong. But at the same time, you don't want to have to add all the checks for all types of instrumentation that might have nitpicks here and there.
So that is a little… I will get there when I get there. I don't know, like.
Trent Mick 00:18:55 Right.
MG Marylia Gutierrez 00:18:55 It's gonna be a little case-by-case.
Trent Mick 00:18:58 Yeah, there are definitely some things to sort out there that aren't spec'd yet. Okay, so I understand you're working through stuff that is specified first, so that's cool.
MG Marylia Gutierrez 00:19:05 Yeah.
Trent Mick 00:19:08 Cool, thanks.
Marc Pichler (Dynatrace) 00:19:17 Alright, any more… Questions about, configuration stuff, maybe?
Or other things.
maybe I'm also trying to delay triage.
Trent Mick 00:19:29 A bit.
MG Marylia Gutierrez 00:19:33 More questions, Mark? No.
Marc Pichler (Dynatrace) 00:19:40 Right, if there's no more questions, then I guess we have to move on to triage anyway.
As always, if you have a topic that you would like to discuss while we're doing triage, please just say the word, and we can go back to the agenda and talk about your topic.
The first one here is in the core repo, I think we talked about this on, on the PR that… David opened… Where the error callback is being called twice on this utility thing.
it… I think doesn't really impact any end users, because in the end, it's actually wrapped again as a promise, and then that promise, just kind of discards the second car, so only the first one counts.
So, mark this P4.
And I'm now looking into doing some work on the exporters again as well, so, I would just assign this to myself.
And then, I'll sort this out. I probably… probably will just integrate this one now into the, HTTP transport thing.
Because, previously we had this extra file to make sure that the HTTP module doesn't get loaded.
Which… Isn't valid anymore, because we now use, We just import the HTTP module wherever we need it, instead of just in this one file. So that makes the whole file kind of obsolete, and then I can also… clean it up a bit. So… that is, the OTRP exporter base package, and, we'll just sort this out, probably as preparation for another PR that I'm, going to open soon.
To add the dynamic, headers.
Dynamic header support to do exporters.
Oh, Alright, this one here is something that we talked about last week already.
And I think the weeks before that, I had pinged the browser maintainers about any specific plans.
On which bundles should be supported, because… We're using these entry points in a bunch of our packages.
That aren't supported by all versions of our panelists, so… It's just trying to gauge, what the browser seek is looking for in terms of bundler support.
There seems to be a workaround to… Actually used this… Which, I guess, can be quite annoying, to use.
Still…
Trent Mick 00:23:14 So we want a doc that says, we don't support Webpack 4, but if you're using it and stuck, here's the workaround.
Marc Pichler (Dynatrace) 00:23:20 Hmm.
I guess that would be one way to go about it.
essentially, once we, decide on what we're gonna do with the browser-specific exporters, if we wanna keep it in One package, or we wanna… Create a different one that's browser-specific, that would actually clean up a lot of the internals of the OTRP exporter base package.
Trent Mick 00:23:52 I'd support doing that.
bet.
Mostly, I think it's your call, because you know the internals a lot better.
Marc Pichler (Dynatrace) 00:23:59 Yeah, it's, the antennas mostly look the way that they do, because, We try to do both from one package. So, yeah, It would be a fairly large change, though.
I guess for now, the question is, do we want to handle this as a bug, or do we… Mark this as, like, a feature request to add back, support for… WebPic 4.
and other bundlers, which might not be able to deal with this. I think we had one.
That we ran into a while ago.
And I was also having trouble with this.
Jamie Danielson 00:24:57 I think we had, like, documented somewhere that we couldn't yet support bundlers, like, that sometimes it might work, sometimes it might not, Which would mean that this would be more of a feature request, especially if there's a workaround. Not saying that it shouldn't get done, I think that's a big thing the browser folks are gonna be looking at doing, but… It seems like it would match the feature request, since that's how we've labeled other similar… Things.
Marc Pichler (Dynatrace) 00:25:25 Oh, you Alright.
Jamie Danielson 00:25:31 Happy to be disagreeable, so every, every bug is a feature, really.
Feature for improvement.
Marc Pichler (Dynatrace) 00:25:40 I'm trying to find now where we documented this… I know we did a bunch of… Like, which versions of things we support?
Hmm.
Maybe it's in talk.
Trent Mick 00:26:13 You mean just which browser support would support TypeScript support?
Marc Pichler (Dynatrace) 00:26:17 Yeah, Panda support, maybe, as well.
Trent Mick 00:26:21 bundlers. There, I mean, there's support sections in the… Or repos README.
Marc Pichler (Dynatrace) 00:26:29 I think we might want to… Yeah, which ones we support, for one, and, problems that people might run into, when they are Bundling their apps.
and they want to use instrumentations.
Because I think that's also one of the common, things that people run into, is they bundle their app, and they want to use the instrumentations, and then UNDIG works, but others don't.
And people are usually confused about this.
Trent Mick 00:27:09 Great.
What?
Marc Pichler (Dynatrace) 00:27:16 And we're… Let's see here, I will assign this to myself, and I will come up with a response here. I will relabel this as a feature request.
And I will create another… Back, issue that, talks about the missing, Information in the docs about which bundles are supported for which platforms.
And I will draft up a document that will state which ones are supported, which would probably just be Webpack 5 for web stuff at the moment, and then once we add more tests, we can add support for more.
More bundles as well.
Sound okay?
Right.
As a side note, the PR I was talking about earlier, which is… This one here.
There's actually a blocker for roll-up Node.js tests that I'm trying to introduce.
So… They are currently failing on this.
so that one would unblock, us from, adding tests like that, and then also adding that to any support matrix that we might have for, bundles.
Jamie Danielson 00:28:52 I found the one note that I wasn't… couldn't find before, but I… it kind of seems like it's very specific to… Node.js the way that's written? Maybe not.
but has… modules are not included in a bundle, like, under this limitations section, in the instrumentation package. So maybe we just need to surface that, because… So, like, right after that instrumentation right there, yeah, the second bullet point.
Facebook.
Marc Pichler (Dynatrace) 00:29:26 things.
I think, in general, the, our README could probably do a bit better in picking people up, where their, issues are. So… Essentially, somebody probably will land here and wants to instrument their app and things like that.
So we could probably point out a few more things here that are, worth noting.
Jamie Danielson 00:29:58 We did talk about that at some point, right? Because we talked about maybe even putting it in the issue template or something of, like.
here's some common issues you might run into. Like, we… that's why we added the one ESM support doc, but even if there's, like, one main… like… Troubleshooting or something, like, here's common issues, that might be… Useful.
Marc Pichler (Dynatrace) 00:30:19 A.
Yeah, there's this doc that somebody added recently, which… oops, why am I clicking on this page here?
frequently asked questions.
this is actually not that frequently asked, but still somewhat frequently asked. It's just the first one that they added there.
But I guess we could somehow integrate that.
MG Marylia Gutierrez 00:30:54 Just put a… instead of just FAQ, put an S in the front, sometimes frequently asked.
Marc Pichler (Dynatrace) 00:31:05 Yeah, I guess it's a larger improvement, that we can drive at another time, but, just adding supported pooling and stuff like that, also to the, like, README would be a good start for people that are… just getting ready, looking at this the first time, to avoid disappointments later.
Jamie Danielson 00:31:35 Makes sense.
Marc Pichler (Dynatrace) 00:31:39 Right, so I just picked this up, Once I'm done with the, the first one here.
And… This one is actually also an FAQ thing, which is… And what's being asked for here is actually blocked on the TC39 async context stuff.
I also just assign this to myself, and write something up in the FAQ thing, Let people know that.
There's… there's little stuff that we can do, to actually make this work.
Damn.
Right.
Let's move on to the next report, and this is… SQS process hook.
I typed out, question… I think that was last week after the STIG meeting.
If there's any workaround that would be, okay, with them.
So, essentially, what happened here is, this SQS process hook doesn't exist anymore, because the process band doesn't exist anymore, because it's not in the semconf.
And they were using that to attach some extra information on their SQS process spans.
And basically do it in one place, so they wouldn't need to instrument all their order code. They wouldn't need to put, thanks.
The attributes on the span, in all of their, In all of their code, but they would just do it in one central place.
And they were using, Manbridge.
Instrumentation layer made it easier to roll out it everywhere.
I will actually recategorize this as a feature request, because the break was actually, done on purpose.
There you go.
I'm not sure if I have a good response ready for them right away.
Jamie Danielson 00:35:19 I was trying to see if it was similar. There was, like, the open PR where someone was trying to add I guess that was SQS context propagation, I think it was related to creating those spans, I guess recreating the spans, to be able to allow that, and it was kind of an open question of whether the Lambda spec was gonna get updated.
So we had something to follow.
Sorry, that was, like, 2981 was the pull request.
But…
Trent Mick 00:35:53 Yeah, it's related, but I think the Lambda spec is just behind, and it's not caught up to what the messaging.
Jamie Danielson 00:36:00 Got it.
Trent Mick 00:36:01 SEMCOV is work… Towards dropping processing spins.
Jamie Danielson 00:36:05 Okay.
Trent Mick 00:36:09 And I think I was tagged in this one, I meant to respond. I haven't yet.
Marc Pichler (Dynatrace) 00:36:17 Okay.
Nope.
Fully up to speed on this one.
Yeah, I guess for… This one here, though, One of the things that I proposed is we could reintroduce a hook that, allows to add that information to the spam link instead.
I'm not sure if that's at all useful.
Boredom.
Trent Mick 00:37:16 Yeah, I mean, possibly, but yeah, I guess the answer you get always from people actually trying to use stuff that's following messaging spec is that I don't know that any of the observability platforms do much with span links.
So, it doesn't buy you much. It's a hard problem, because there's no… I mean, there's… There was no real reasoning or what are the processing spans, and… I don't know.
context propagation through messaging systems is hard, because it's not one message at a time. They come in in bulk, and so you can't just do parent-child.
Anyway, yeah, it's gross.
the response here from Sam's super seemed to… He didn't latch onto that suggestion, though.
Pardon me.
So, yeah, I don't know.
Marc Pichler (Dynatrace) 00:38:13 I were, leave this for now, but I will type up a response after the meeting here as well.
Just to get a feeling of, How we could help them out, too.
to, similar stuff there.
Yeah, that… with the spendings, That's a good point. I don't even know what… we would… how we display those in Dana Trace, And that, I guess, says enough of how useful that would be, for people, maybe.
Alright, I guess that's it for… untriaged 100 bucks, and I guess we can check how many PRs are open in… the repos right now, and then choose accordingly. Looks like, Contrib has more PRs at this point in time, so let's do Contrip first.
This one here, I guess there wasn't any, any change recently?
And we have, page view instrumentation… Let's connected to us.
Multiple requests… in place of HV instrumentation that was being worked on this…
David Luna Bistuer 00:40:20 Yeah, Mark, this was discussed last week, Since there were no… there is no consensus on the page view, we decided at least to start with one simple event, which is page… browser navigation.
So they're going to start with this implementation step.
And that day 2 is going to be on hold.
For now.
Marc Pichler (Dynatrace) 00:40:41 Okay.
David Luna Bistuer 00:40:45 Martin.
Jamie Danielson 00:40:46 Note of that.
David Luna Bistuer 00:40:47 I'll ask tomorrow, maybe, if we can close that PR on the beach view, and then, continue.
On the navigation one, and then let's on the page one, whenever we… have a clear idea on the API that we want to have for PageView.
Yeah.
Marc Pichler (Dynatrace) 00:41:05 Okay.
Sounds good. Alright, then I guess, we'll just leave it, like this now, and then, We can look into it tomorrow again.
Or another time.
The next one is… Liquorize instrumentation… Few changes requested, but… no.
Activity, so I guess we'll also keep that one open for now.
Next one is… With exception instrumentation… Editors… Or some… some activity here. But no changes as well.
this PR here, I had approved, and it worked.
I'll hit the branch here, and I'll merge it in later.
Then to the next one…
Trent Mick 00:42:40 That one's all good and ready, I'll merge that one later.
Marc Pichler (Dynatrace) 00:42:43 Alright, thank you.
Then… Participants are recurring one day.
I guess every time we do this, I… say I want to look into this, but then it's not on the front page of, what I'm usually reviewing, so… look into this, when I have some time.
If anybody else here on the call is interested in moving that along, please, go ahead and do so. It's, kind of gnarly, setup that we have in the auto-instrumentations, node package where there's, like, a bunch of different environment variables and settings from the decon… configuring code.
That makes merging these together, like, really… really frustrating sometimes.
And there's a duck that just… Doesn't apply to things in the correct way, and then, It actually doesn't do what the user configured.
Alright, next one is, I guess something that we were meaning to talk about, A long time ago, but…
Trent Mick 00:44:30 Can't believe it was July.
David Luna Bistuer 00:44:33 Yeah.
Marc Pichler (Dynatrace) 00:44:35 No worries. Let's continue on the next one.
Should we skip it, or do you want to talk about it now?
David Luna Bistuer 00:44:43 No, we can skip it. I think also there was a comment, I think it was two weeks ago or so, that we commented on that maybe… Undichi was not the best example, because it's not a browser instrumentation, which is, or, you know, browser folks are more interested in that feature than us.
Trent Mick 00:45:00 I wonder.
David Luna Bistuer 00:45:01 I do, yeah.
Trent Mick 00:45:01 I wonder if you want one that covers both, or covers… Yeah, yeah. Not Indici, but yeah. A browser and a non-browser one to… Yeah. Get to play around with it.
David Luna Bistuer 00:45:16 Okay, okay, I can… I think I can make some… some… another PL that actually takes both. Okay.
What are you going to say?
Trent Mick 00:45:25 I was gonna say, I don't think it's necessarily on you. I don't, like, I feel bad asking you to do work here, because I've been saying since July I wanted to take time and look at this and have an opinion, and I haven't yet.
David Luna Bistuer 00:45:36 That's fine. I think I still remember something from what it went to life, so… And also try, maybe… I was using DSOP, which is a new dependency, but maybe just using ESV… which is using ESV under the hood.
maybe using ESP directly on that tool.
Instead of…
Trent Mick 00:46:00 That was one of the comments, yeah.
David Luna Bistuer 00:46:02 Yeah.
So, maybe we'll try that out.
Marc Pichler (Dynatrace) 00:46:06 I can also, look into, I saw this in another open source project, that they were doing this, so I could put a link there, so that it's easier to do it, probably.
David Luna Bistuer 00:46:26 Okay, thank you.
Marc Pichler (Dynatrace) 00:46:27 Pack this up real quick so that I don't forget.
Or hopefully don't forget, my notes are…
Trent Mick 00:46:35 Interlink's already there, isn't it?
Marc Pichler (Dynatrace) 00:46:37 Is it?
Trent Mick 00:46:39 The open feature JSSK?
Marc Pichler (Dynatrace) 00:46:41 Oh, right, yeah.
Trent Mick 00:46:42 I remember you'd mentioned it, and so I posted it in the last comment.
Marc Pichler (Dynatrace) 00:46:46 Nice. Okay. Then, I guess I won't note it down.
Thanks.
David Luna Bistuer 00:46:51 Thank you.
Marc Pichler (Dynatrace) 00:47:00 Then the next one's renovate, so we'll skip that one.
This draft.
Trent Mick 00:47:10 Let's draft, skip that one. That one's gonna get resolved out with the ES Splint 9 update.
Marc Pichler (Dynatrace) 00:47:16 Oh, awesome.
Trent Mick 00:47:17 a few PRs down.
Marc Pichler (Dynatrace) 00:47:20 Alright, do we have that.
Trent Mick 00:47:28 I have to look at that again, it's been a week or two.
Marc Pichler (Dynatrace) 00:47:31 Hmm.
Trent Mick 00:47:32 But there's been activity on there.
Marc Pichler (Dynatrace) 00:47:34 Can we actually have… That doesn't work. I thought maybe we can close the draft PR. Oh, no.
Trent Mick 00:47:49 I'll go clean it up afterwards. Yeah, it's a complicated relationship.
Marc Pichler (Dynatrace) 00:47:55 Alright, and the next one is… Not-so-stable semantic conventions for, messaging?
Jamie Danielson 00:48:15 Right, but the messaging isn't fully stable yet.
Marc Pichler (Dynatrace) 00:48:18 Yeah.
So, this PR adds this SEMCOM stability opt-in thing, for messaging, even though it's not stable yet. So, if we actually have to do the, stability opt-in thing when messaging semantic conventions go stable, we have no way to do so.
Yeah, I guess it's been 2 weeks, since the last activity, and… Wondering if we should close this one.
Jamie Danielson 00:48:55 It's almost like it's on hold. Like, if there was, like, a hold tag waiting for…
Marc Pichler (Dynatrace) 00:49:00 Yeah.
Jamie Danielson 00:49:01 Spec, or waiting for… Stable attributes, and it could be revisited.
Hmm.
Trent Mick 00:49:08 Are we not allowed to do this yet?
Just do an opt-in with messaging on this?
Marc Pichler (Dynatrace) 00:49:14 We are allowed to, I guess, but.
Jamie Danielson 00:49:18 if…
Marc Pichler (Dynatrace) 00:49:21 They're not.
Jamie Danielson 00:49:22 Stable, yeah.
Marc Pichler (Dynatrace) 00:49:23 anxious, yeah.
Jamie Danielson 00:49:24 It's frown… it's not frowned upon, it is discouraged by SEMCOM.
Well, if we're breaking, it's one of those things, like, if it breaks again, then even though… like, because we'd be saying that something is stable and it's not stable, so then if right before becoming stable, the attribute changes… Then that person's attributes will be different, which theoretically is on them to sort out, but in practice, that's… Kind of tricky.
MG Marylia Gutierrez 00:49:55 Because then it becomes, like, the environment variable right now is, like, saying, like, old and the stable, but then if there is a new stable, you're gonna add, like.
Stable Plus, I don't know.
Jamie Danielson 00:50:06 Yeah, and it's misleading, because you're giving an option for something that's stable that's not really stable.
Trent Mick 00:50:11 But saying no to this is kind of crap too, right?
Jamie Danielson 00:50:13 Well, that's why I said it should be almost on full.
Trent Mick 00:50:15 Okay.
Jamie Danielson 00:50:16 like, it should almost be, like, on hold, like, this'll probably be a thing that we want, but semantic conventions like SIG has specifically discouraged updating attributes before stable if it results in breaking changes and… You're calling something stable that isn't stable.
Trent Mick 00:50:35 So I'm debating here from… I'm debating here from the user's point of view, so… so I'm a user of MQP, and I want to instrument it.
And I just, like… I just want to use the new… SEMCOM things, even though they're not stable, because they've been written that way, like, 2 years ago, and the AMQP instrumentation has been updated in 3 years, or whatever. Can I just get the new ones? How?
Jamie Danielson 00:51:00 Is this…
Trent Mick 00:51:01 Could we do, like, we could do a breaking change of the instrumentation that just doesn't use the opt-in environment variable, it just gets rid of the old ones and just uses the new ones.
Jamie Danielson 00:51:11 Can I ask a question? Because I don't know enough about the messaging attributes. The stable, or the newer ones, whatever, are they specifically ones that have been around for, like, a year or whatever, and we just haven't updated our instrumentation in forever? Or are these still somewhat recently?
Trent Mick 00:51:30 change. Pretty sure I was throwing out numbers, but I think, yeah, I think we're on, like.
this instrumentation is on ancient stuff. The net ones do show up as well, like the ones that were stabilized in HTTP, so that's part of it, but mostly we're talking about the messaging ones.
I think they are.
in.
Most of them quite old, maybe not all of them. This… the tendency in SEMCOM to add .name to the end of some things is relatively recent, so… So it's not… it's not as cut and dry, so yeah, I don't know.
Jamie Danielson 00:52:05 Maybe we can do a quick follow-up with messaging? Sorry, Marilla.
MG Marylia Gutierrez 00:52:08 Yeah, I was gonna say, kind of, like, similar. The problem is that the messaging group kind of, like, disbanded.
So it was, like, the messaging, and then they were like, oh, let's focus on something else, because people… this is why it came, like, the database one, and that was put on hold. And then the database finished, like, or going back to message, or gRPC, and people were like, oh, gRPC.
So, right now, that is the active one. I don't think there is a group focusing on messaging right now.
Trent Mick 00:52:39 without the G, right? It's the RPC?
MG Marylia Gutierrez 00:52:41 Yeah, RPC.
Trent Mick 00:52:43 RBC that they're working on, yeah.
Jamie Danielson 00:52:45 I mean, there's, like, the… so if there's the main semantic convention SIG, I don't remember if they still meet on Mondays, maybe?
like, you know, asking, like, we bring it up there and ask what they suggest, since we have the older ones, because I also see the other state of, like, if they're… like, so right now, you know that you want these attributes, someone else doesn't know the backstory and just has this opt-in variable.
And then they don't realize it's gonna change later. But it might not change. I don't know.
That's kind of a hairy situation.
Because we're so far behind on… attributes.
I went in a circle.
I have nothing further to provide, apparently.
Trent Mick 00:53:32 Yeah.
Jamie Danielson 00:53:33 are we… like, so, like, we're behind, I assume, say, like.
I mean, Java, probably, but, like, other languages?
In terms of…
Trent Mick 00:53:43 Yeah, I don't know. I'm not funny.
Jamie Danielson 00:53:46 Because I think that would be worth… Checking out how we compare to… Like, one or two other languages.
And… if everyone else is, like.
closer to something else, and we're still just so far behind. I remember we were really behind on a lot when we were doing the HTTP convention, If that's the case, then maybe it's a little bit different. It's still awkward calling him stable, it almost… put in a braking change with the, here's the new attribute. Instead… But… I don't know. I can look at this, too.
And… Word vomit on it, if that helps.
MG Marylia Gutierrez 00:54:29 Yeah, I can also ask Flute Miller if she has any… guidance?
Jamie Danielson 00:54:35 Yeah.
Because I think we have a similar thing with GraphQL. There was an open issue, or VR or something at some point, related to updating GraphQL attributes. I don't remember what happened to it.
Marc Pichler (Dynatrace) 00:54:56 Alright.
Jamie Danielson 00:54:59 2976…
Marc Pichler (Dynatrace) 00:55:01 And I guess we will leave that one open for now, and… At some point, we might need to decide, like, if we have more context from the… semantic conventions, folks.
Whether we want to do a braking change right now to actually Align this, or if we want to have some sort of a transition or a period.
furnace here, but I guess we'll just leave it open for now.
Jamie Danielson 00:55:36 Yeah, because I think in the meantime, we can't use that. Like, whatever we decide to do, I don't think we can use that environment variable option.
Because that's, like, almost… Explicitly going against spec by providing something that doesn't exist, right?
Trent Mick 00:55:52 Wait, so…
MG Marylia Gutierrez 00:55:54 We can't force… Am I misreading?
Trent Mick 00:55:56 The link that I just gave, am I… can you bring that up?
the link in chat.
Jamie Danielson 00:56:08 I mean, these are… stable?
Trent Mick 00:56:12 Isn't that saying we should introduce the environment variable?
Marc Pichler (Dynatrace) 00:56:15 Bye.
Trent Mick 00:56:15 The second bullet in the warning section.
Jamie Danielson 00:56:19 That's what it looks like.
MG Marylia Gutierrez 00:56:21 Yeah.
Marc Pichler (Dynatrace) 00:56:23 Maybe we just open up PR towards the MCOMF repo and mark it as stable and see what's happening. Well, nothing…
MG Marylia Gutierrez 00:56:30 it's stopping for, like, the PR sending both things.
Which is kind of, like, what the… the thing does.
the opt-in, like, you have both of them for a while, so this way, it's not a breaking change for people that are using, but then you get the new things that people do care, but then that is the default. They have no option of opt-in or not.
So, I think that is, like… just act as the default, is the dub, like, the B option.
the duplicate option.
Trent Mick 00:57:10 But then you're in a pickle when things are stabilized, right?
Jamie Danielson 00:57:16 Yeah.
I'm… Did they, like, prepare this document?
MG Marylia Gutierrez 00:57:24 So one thing that happened, like, for example, on the database in a few cases, where, like, oh, if this, like, metric or whatever did not exist.
And we were like, okay, we are creating… we can… even if after it was stable, you can just create without putting the opt-in.
And only things that you were changing that you needed to opt in.
So, you would kinda act like that, saying, like, oh, all those changes are just new things.
Jamie Danielson 00:57:58 Yeah, it's really just if they change before they actually go stable.
Marc Pichler (Dynatrace) 00:58:02 And the kids…
MG Marylia Gutierrez 00:58:03 Well, if they change, then is when you… if they become, like, any of those things change, when you create the opt-in, now you have those current options that we added, and this stable one.
Jamie Danielson 00:58:14 Oh, you're saying if we added in ones that don't currently exist, and just add them in there?
MG Marylia Gutierrez 00:58:19 Yeah, just add them. Like, do not update any of the existing stuff, just add extra, those things. So, I will say… The only one that I don't know, if the spam name is different, that would be a tricky one. I don't know if that is the case or not.
Jamie Danielson 00:58:33 Yeah. I know, like, so speaking from, like.
Right? Honeycomb, I can have all the attributes that I want, so I'm always in favor of, yes, let's add more attributes, but I know, I'm pretty sure there are other backends that, like, that could end up being a problem if people have extra attributes, right, that they don't necessarily want. I think that's why the… The default behavior isn't emitting both.
For things.
MG Marylia Gutierrez 00:58:59 Well, but that happens when you're adding a new metric, right?
Jamie Danielson 00:59:04 I don't know.
I can't speak for other… I feel like I've heard of this, this is in at least marketing materials and things, but I mostly just know what Honeycomb is.
MG Marylia Gutierrez 00:59:12 I'll say, like.
Jamie Danielson 00:59:12 Right?
MG Marylia Gutierrez 00:59:13 No, no, I'm not saying, like, for the vendor perspective, I'm saying, like, how we've been doing so far. If there is a new metric, we just added the new metric. If there's, like, a new attribute, we just added the new attributes. We never added, like, a flag to add the new stuff.
Jamie Danielson 00:59:30 Gotcha.
Do we see which ones are new and which ones are different?
And then… Decide from there…
Marc Pichler (Dynatrace) 00:59:45 I guess that would be a good approach, yes.
Jamie Danielson 00:59:50 Because it seems like most of them… well, I guess now, I see things that are in development, I don't actually see what would have changed.
So that's kind of like a manual process right now, I think.
Marc Pichler (Dynatrace) 01:00:03 And there's also a good chance that the instrumentation itself is using stuff that was never in SEMConf to begin with.
Jamie Danielson 01:00:13 Yes, we have done that.
Marc Pichler (Dynatrace) 01:00:15 Good.
Jamie Danielson 01:00:17 And then what?
Marc Pichler (Dynatrace) 01:00:19 Fair.
Anyway, I guess it's not something that we can… surf on the car today. L.
And also, we are out of time, so… I guess let's look into it, another time. Thank you, R, for joining.
And see you next week.
Trent Mick 01:00:44 Thanks.
Jamie Danielson 01:00:45 Thanks.
Marc Pichler (Dynatrace) 01:00:46 Thank you, bye.
