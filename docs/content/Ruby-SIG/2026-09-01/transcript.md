SIG: Ruby SIG
Date: 2026-09-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle (New Relic, Inc.)** 00:30 Hello!
**Xuan Cao** 00:35 Alright.
**Kayla Reopelle (New Relic, Inc.)** 00:54 I can wait another minute or two and see if anyone else is joining us today.
Hello?
Hello!
Welcome.
Don't know if hannah's joining us today… There we go.
All right, okay, I think we have everybody we're expecting.
Yeah.
So, joseph, thank you for joining us today.
We've interacted with you online, but nice to meet you in person. Is there… are you interested in, like, introducing yourself? Do you want to just kind of, like, sit back and watch the meeting? How… what would you like to do today?
**Josef Šimánek** 03:04 Hello, everyone.
And I'm happy to introduce myself.
I'm Josef, I'm based in Prague, Czech Republic, in the middle of the Europe.
Big fan of the Olta project.
active… active user, and I try to help, usually, with some basic stuff, like a review over… Maybe a few years already.
I've seen there was some exodus of some maintainers recently, for various reasons.
So if any help is needed, I'm around, happy to help, I'm also… you can take a look at my GitHub, I have a long history with open source maintaining, and Ruby, in general.
Various contributions, various projects, not all will be already scoped.
But Robbie is still my, secret fashion points.
And for auto, I see a lot of value in this, actually, projections.
It's trying to tame the jungle around us, right? Of various vendors and metrics and all this stuff.
So, yeah, big fan of those, Open, community-based standardization.
**Kayla Reopelle (New Relic, Inc.)** 04:17 Awesome. Thank you for coming today, thank you for all your help on the project.
So far, yeah, I've really appreciated your support lately, especially with some of the departures.
Nice. Okay, we have a full house today. Here is… the… Meeting notes, and then… Share my screen. Hold on first, let me attend to my dog, and then I'll be right.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 04:55 Hey, everybody.
Take this moment, say hi.
Faces I haven't seen in a while.
**hannah** 05:01 Hey, Rob.
**Kayla Reopelle (New Relic, Inc.)** 05:03 We could do a quick round of intros, too, since we do have a new person.
I'm Kayla, I work at New Relic. I've been… working in Ruby for a while, and contributing to this project for a couple years, and I'm hoping that We can keep making progress towards getting metrics and logs stabilized.
Yeah, does anyone want to go next?
**hannah** 05:29 I'm Hannah, and I also work at New Relic. Probably, I think… I've been working on the hotel project for maybe 2 years? Mostly in semantic convention migration work.
**Matthew Wear** 05:44 You can go next. I'm Matt. I work at Dash Zero. I worked on OpenTelemetry Ruby a lot, like, in the early days, and then I did not work on it for a long time, and now I'm back working on it, a lot more.
And… yeah.
That's me.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 06:05 And I'm Rob. I've been… working on OpenTelemetry Ruby since the middle days, and then I wasn't. And now I'm trying to again.
I'm a maintainer in Contrib for the instrumentations and whatnot, and an approver in core, and… Hoping to maintain that, because I care about being able to look at Ruby apps.
**Xuan Cao** 06:33 Hi, my name is Shen. I've been here for almost 2 years. I work for the Slovins.
**Josef Šimánek** 06:45 Nice to meet you, everyone. I probably forgot to mention, actually.
What is my interest or background?
I do work for, currently it's… Virgin Music Group?
But my open source work is unrelated, actually, to my daily job.
So I'm mostly trying to represent the community, actually, and the users.
So I'm independent in here, not coupled to the company either.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 07:14 So not a big Rails monolith at Virgil.
**Josef Šimánek** 07:17 Not that version, but we have, yeah, in the… some subgroup in there.
And we are actually happy about, to be honest.
**Kayla Reopelle (New Relic, Inc.)** 07:29 Nees.
Alright, I will share my screen.
Okay, Spec SIG had some connectivity issues this morning.
Matt, were you able to go? It looks like you were. Is there anything in here you think we should discuss today?
**Matthew Wear** 07:48 There were definitely some relevant things, so, There's this entities spec that also… Kind of changes some things around resource detectors?
**Kayla Reopelle (New Relic, Inc.)** 08:06 this…
**Matthew Wear** 08:09 Yes, so that's, That's the spec, I haven't read the spec, I just kind of… it was announced, and then there was some discussion around it, but if you go back to the spec SIG notes… It seems like it's formalizing this resource provider concept for how to create resources and run detectors, and there's… Boom.
Yeah, I need to read more about entities, which I've said a lot, but those also, Are related to resource detectors, but not exactly resource, like, the attributes that you will collect are actually, like, entity attributes, but there… there's some interaction, I think, that we probably also need to understand, so… I don't have a lot of information on this other than I think that it would be good for us to… to read up on it and see, See what's happening here.
**Kayla Reopelle (New Relic, Inc.)** 09:13 Right, sounds good.
Yeah, I guess I'll just add that.
Care.
Nice.
**Matthew Wear** 09:33 And then, the other one that… Seems relevant is there's this clarification of the server address.
attribute, and it was discussed in… yeah, in relation to database, it says it right there, database server address.
And… Yeah, I know, I think Hannah has been doing some work on… updating databases to match current semantic conventions, so this is probably somewhat relevant. It's just… it just has, like, special cases for How you're actually connecting to your database, like, I don't know.
how much we deal with this in Contrib, but… If you, like, connect to your database via, like, a load balancer or something that kind of routes you, you know, to somewhere else, then the server address is that first thing that you talk to.
And then the, I think it's the net peer that ends up being the actual database you get routed to.
So…
**hannah** 10:43 Okay, I'll just look at that.
**Matthew Wear** 10:45 What's that?
**hannah** 10:46 I'll take a look at that.
**Matthew Wear** 10:48 Alright, yeah, there's… There's a link there to, like, the new… the new spec.
Verbiage.
I think.
**Kayla Reopelle (New Relic, Inc.)** 10:59 This one?
**Matthew Wear** 11:06 Possibly.
This is a lot more than I remember seeing.
**Kayla Reopelle (New Relic, Inc.)** 11:11 Maybe.
**Matthew Wear** 11:12 What was the other link that was a little bit below in the bullets?
**Kayla Reopelle (New Relic, Inc.)** 11:16 This one…
**Matthew Wear** 11:18 Yeah, I think this was the one that was a little more digestible. I think it, And then if we scroll down just a little bit… there's a table, yeah, so here you go. You can end up with, like, server address. This is… yeah, the first column, or the first row is the thing that we're probably used to.
But… You can technically have multiple servers.
You would have, like, a comma delimited list.
Multiple servers with shared port.
Multiple servers with different port.
**Kayla Reopelle (New Relic, Inc.)** 12:02 Interesting.
**Matthew Wear** 12:06 And yeah, all of this kind of came out of the Java instrumentation SIG they had all these cases, so they had to spec it out.
**Kayla Reopelle (New Relic, Inc.)** 12:20 Interesting.
Anything else you can… you want to call out from here?
**Matthew Wear** 12:35 No, I think that, Those were the most relevant things.
**Kayla Reopelle (New Relic, Inc.)** 12:47 Awesome.
Thank you.
Okay, yeah, core… there's a whole lot happening there. It might be worth just scrolling through the PRs to see what jumps out at us, but we should have the first release of the OTLP Common Gem, which was something we talked about recently.
Which will also have releases for… The exporter and, metrics, we have, like, a couple of gems that are queued up.
The thing I wanted to chat with everyone about, so maybe we do this first before we go through all of the… PRs, is that I noticed the OpenAI instrumentation wasn't running in the CI, and when I added it, there were a few failures related to logs.
And it looks like there's still some, even after my latest changes. Okay, bundler issue.
Anyways, it did lead me to look a little more closely at our current implementation of it, and we are listing the logs API as a dependency, and I don't remember… If we discussed it, or what we decided.
About that, because when we had talked in the past about having… metrics as a dependency. We didn't want to put something that was a dependency on an unstable library into the all gem, or… but I don't know if that's also still the case, now that we have the logger instrumentation in there, maybe logs is seen as a little different.
But mostly I just wanted us to be aware of the choice that we were making before we release OpenAI instrumentation for the first time.
I think this pull request still needs a little bit of work.
It's all kind of fast yesterday, but the idea… Here would be to only… create a logger if we see that the logs API and SDK are installed.
We had talked about this previously with metrics. We were also talking about adding Another, like, configuration that would determine whether or not you send metric events, so we could add that here as well, and have a configuration to decide whether or not you send logs.
And then the kind of second… check here… Where'd you go? Is that unless, you know, there is a logger, which that method that we looked at before will return nil if the log's gems aren't installed.
Then we just skip calls to this event.
Yeah, so I'm sure there's other ways that we can do it, but the philosophy question still stands? Like, what do we think about shipping the logs API in the OpenAI library?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 15:59 Can I get caught up on why that's… Controversial?
**Kayla Reopelle (New Relic, Inc.)** 16:05 I mean, and maybe it's not controversial anymore. I guess I don't think it's particularly…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:08 Instrumentation has to depend on the API, and if the logs API is in the logs API jam.
**Kayla Reopelle (New Relic, Inc.)** 16:14 And so the logs API gem is not stable, but the tracing API gem is stable, so that's…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:21 Oh, I see.
**Kayla Reopelle (New Relic, Inc.)** 16:22 The main thing is, like, there's a stability discrepancy, but our instrumentation libraries are all at zero dots, so they're also not stable.
I don't know, yeah, in our House of Stability cards, like, how many we need, how many layers.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:40 So the, the, the question is, do we let, do we enable the… this particular instrumentation to, like.
By default, if you just have the standard OTEL SDK and this instrumentation, it would trace. But if you were to opt in to adding the logs SDK, which is experimental, that would enable the logging in it, too.
**Kayla Reopelle (New Relic, Inc.)** 17:04 Yeah, that's how it currently works, and so it includes the Unstable Logs API as a dependency, so that's getting installed in your environment as well, if you have this gem.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 17:14 Matt, what did we do when the… when the… SDK gem was unstable.
I feel like instrumentation had to depend on it.
**Kayla Reopelle (New Relic, Inc.)** 17:22 No, instrumentation doesn't depend on the SDK.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 17:24 I'm sorry, I'm sorry, I misspoke. The API.
In all of this, I mean the API, because instrumentation depends on the API, not the SDK. So, like, when the API was unstable.
Not yet stable.
**Matthew Wear** 17:37 Everything was unstable.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 17:38 Right?
**Matthew Wear** 17:40 all there was was a tracing API that was kind of under development, and then at some point in time.
Oh… Yeah, tracing became stable, and… The other signals came along, and they have been in various levels of stability.
So, like… The reason for this, technically, is there's some… Stability document somewhere that says, like, a stable.
Yeah, it's like a stable component cannot reference an unstable component, more or less.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 18:14 Good news, the instrumentation's not stable, so we can do whatever we want.
**Matthew Wear** 18:18 Well, the instrumentation is not stable, but I think a lot of people use instrumentation all, so, like… Kind of by… By that fact, everybody ends up pulling in all this unstable stuff if we rely on it, which is… What we're trying to avoid… I think, not so much… that… I think not so much that maybe we have a problem with instrumentation, depending on the stuff, because we kind of own it. I feel like we worry more that users… users will somehow get their hands on these unstable APIs and start, like, using them, and then they'll be mad if we change them.
It's like… instrumentation, I kind of feel like we… we are gonna be the ones that have to change those when the APIs change, so… We probably won't be mad at ourselves.
But,
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 19:17 I think it's fu- the ifs are fine, I think.
If you happen to bring in the logs, it'll light up the logs, and if you have a bad experience, take that gem out.
**Kayla Reopelle (New Relic, Inc.)** 19:27 Yeah, because if you… if you don't install… the Logs SDK, you won't get logs. You have to install that separately. With how it is right now, the Logs API would be installed, but… So this PR takes out the logs API. So I guess, yeah, we have… we have a few options that I see are we leave it as it is, we install the logs API, we include the instrumentation and instrumentational.
we could… leave the gem as it is, but take it out of Instrumentation All, since it has unstable code. Or, you could leave it in Instrumentation All and pull out the log's dependencies and force users to install them.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 20:08 Let's do that.
**Kayla Reopelle (New Relic, Inc.)** 20:09 Okay.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 20:11 I'm open to pushback, because I've been away a while, but that feels like… Use all, and you won't break, and we can document in this gem, if you want to light up the log signal, you have to install the unstable API, and… And it's fine. Some future release, we'll… Will depend on it, but until then, you can opt in on the logs.
Okay. And honestly, sort of selfishly, I want people to trace. So, you know?
**Kayla Reopelle (New Relic, Inc.)** 20:42 Yeah, yep.
Okay, that works for me, and I can polish this up a little more to make that happen. That would be postponing the opening eye release until we… get this merged, which we would probably want to do anyway, since the CI isn't running for it right now.
Does that sound good? I mean, we've got… we know Rob's opinion. I'm also aligned with Rob's opinion. Does anyone have a different opinion, or something else that we should, be thinking about?
**Matthew Wear** 21:16 I'm fine with it. I think, Yeah, I think the… the way to get around this is to… see what our stability roadmap looks like for both metrics and logs, and I feel like, Yeah, it would… it would be nice to see what needs to be done to make those stable, and then try to make them stable so that we can start using them everywhere.
**Kayla Reopelle (New Relic, Inc.)** 21:41 Yeah.
**Matthew Wear** 21:42 Oof.
And then these problems disappear.
**Kayla Reopelle (New Relic, Inc.)** 21:45 I do have a thing I could show you guys, it's a little haphazard, but, I'm not really sure where to put it, because it's a markdown document, but I do have, like, a full Claw spec audit, implementation audit, that I'm planning to turn into issues in a project, but if… I guess if we want to discuss those stability roadmaps together today, we could look at that.
Or we could leave it for next meeting, and I can get some artifacts out to everybody.
**Matthew Wear** 22:14 would it… Are we kind of springing it… springing it on you for today? Would next week be… be better, do you think?
**Kayla Reopelle (New Relic, Inc.)** 22:22 I mean, I don't think… I think next week would be more polished, but if you don't mind some roughness, then this is fine with me.
**Matthew Wear** 22:30 I'm fine with next week, I think that's cool, if you would like the time.
**Kayla Reopelle (New Relic, Inc.)** 22:34 Sure.
Sure. Then we can take more action and have prettier things to look at.
Cool.
So… okay, so the plan here is… To continue… oh, thank you. Sweet. Appreciate that.
Okay, cool.
That was the main topic topic that we had today. Should we just do… does anyone else here have something specific they want to discuss, before we go into… Just the perusing of the repos.
Sounds good.
Yeah, so… Core repo… We have some dependencies, we have some yard dock… Changes… this one, I have not looked at yet, Xuan, are you aware of this one?
**Xuan Cao** 23:41 Yeah, I'll… I'll take a look at it.
**Kayla Reopelle (New Relic, Inc.)** 23:44 Okay, thank you.
And then we have these baggage limits discussions.
that are happening. I still think we might have a little more work to do here, I'm also… Not a baggage expert, and so if anyone else has more confidence in this, I would love a second set of eyes before we merge it in.
**Matthew Wear** 24:18 I can take a look.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 24:20 who have handled baggage in the past. I will…
**Kayla Reopelle (New Relic, Inc.)** 24:24 Nice. Yeah, I think it… this change, I think, has the potential to add some overhead. I feel like it's trying to handle a lot of edge cases, so, more eyes would be good.
This one we talked about somewhat recently… I… Opened up… yeah, we haven't… heard from the reporter. But, I opened up a separate PR to merge into this branch to kind of adjust how log record limits are being counted.
So that it reflects a little bit more closely with Java.
If we don't hear back from the contributor, I do think this is a fix that we'll want in eventually. It is kind of based on some undocumented use cases of the logs API, but Since I've kind of gotten deeper into this, a review from someone who isn't me on… on this and the code change would be great as well.
Let's see, what else do we have? We've talked about declarative config… And… it's been a minute there, It might actually be waiting on me. I did mark the changes requested.
Okay, this looks like it's something I need to… address my own comments on, so that's my bad. But if anyone else is interested in declarative config, it seems like we're getting pretty close to releasing that, so it would be a good time to take a look.
Since we're in the core repo, any pull requests that anyone else wants to call out?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 26:25 I, before I had the personal stuff come up, I was trying to track the schema URL, which was also related to.
**Kayla Reopelle (New Relic, Inc.)** 26:34 Damn.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 26:35 instrumentation scope level attributes and all that. Has anything changed there?
And if nobody knows offhand, I can go research later.
**Kayla Reopelle (New Relic, Inc.)** 26:48 I think Hannah, has been looking into it. I saw you come off mute. Is there anything you want to add?
**hannah** 26:54 Yeah, I was just gonna share that that's something I hope to work on. I don't think we've had any updates, I was looking at some old PRs, and it looks like if I remember correctly, at one point, we had, like, an almost implementation, but that didn't go through. So it's something on the radar, but nothing has happened yet with it.
**Matthew Wear** 27:14 That, discussion during the Spec SIG also was… Yeah, there's some combination of entities, resource, and schema URL that, that was being discussed that I think would be also probably relevant to, that conversation. I feel like… Yeah, I feel like schema URL… causes issues when merging resources, and the way that various SDKs handle this is varied and not great, and I think That was trying to smooth over some of those issues as well, so…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 27:53 I'm… I'm hoping.
if my memory is… I'm hoping my memory is correct, because my memory is that it can happen at the instrumentation scope, and that doesn't… Affects, really, what is happening at the resource level, but… That could just be me wishful thinking.
Okay.
Cool. Hannah, I'm trying to, like, ease back in and not over-commit, but if you've got stuff that… you want to point me towards that I might help.
something.
**hannah** 28:25 Yeah, that'd be great. Let me get started on stuff, and then I'll rope you in. That sounds wonderful.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 28:30 Thank you.
**Kayla Reopelle (New Relic, Inc.)** 28:34 Alright, cool.
Okay, we have a… Issue for that… We haven't had much change here, any… Issues we wanna discuss?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 28:57 I'm assuming that baggage issue that scrolled by was the… what the PR's attached to.
**Kayla Reopelle (New Relic, Inc.)** 29:01 Yep, yeah.
It's the second PR that's tried to work on this as well. There's another one that, did some similar things, but the person kind of dropped off, and I think there were a few changes we wanted made, so… Keep that in mind, too.
Contribib.
Okay, got a lot of dependency things, The OS resource detector is also nearly ready for release.
Lots of appraisals… Yeah, just kind of open floor, any PRs that folks want to discuss?
One contrib.
Oh, I have one. I do want to talk about this one. We had some reviews… Last week, thank you, Matt.
Yeah, I'm… I'm fine to approve this one, but because it is RAC, if anyone else wants to take a look, I'd love to get this merged this week, if we can.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 30:41 What was that, Piano, baby?
**Kayla Reopelle (New Relic, Inc.)** 30:43 Pr2130.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 30:47 Okay.
**Kayla Reopelle (New Relic, Inc.)** 30:51 Or Caesar donor?
Issues… We have one new one. I haven't seen this yet.
**hannah** 31:29 I'm happy to take this one, this seems relevant to some stuff I've touched before.
**Kayla Reopelle (New Relic, Inc.)** 31:34 Okay.
That's good.
Thanks, Hannah.
Any thoughts on it before we move on?
**hannah** 31:52 It's based on… it looks reasonable, what they've said, but… We'll take a look. Looks like something that may have existed previously before the Migration stuff was in place, so…
**Kayla Reopelle (New Relic, Inc.)** 32:07 Thank you.
**hannah** 32:08 Yeah.
**Kayla Reopelle (New Relic, Inc.)** 32:16 Alright, yeah.
Any auto instrumentation discussions? Rob, that's a change since you've been here last. We have… Wait, I don't know if we have a release yet, I'm not sure… Oh, I see the release PR was merged. Were we successful today?
**Xuan Cao** 32:46 Yeah, he's out.
**Kayla Reopelle (New Relic, Inc.)** 32:47 Yay! Oh, wonderful! Nice. Thank you.
Okay, so we have a first… version of, the auto instrumentation gem out for people to use, and it's in this separate repo so that it's a little easier to manage with dependencies and everything else, and contribib.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 33:06 How does it… diff… differ from… the instrumentations that…
**Kayla Reopelle (New Relic, Inc.)** 33:13 I know, it's kind of a weird name, but this is the name that all the other languages are using for this. So all it is, is the auto instrumentation gem. So this is the gem that, if you have it installed in your environment, it will install everything else for you, but you don't have to put it in Bundler.
We all.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 33:33 Oh, it's… it is like a,
**Kayla Reopelle (New Relic, Inc.)** 33:36 It's like a meta gem, that takes care of installing the API and the SDK. It's like that one step.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 33:43 It's like all… -Oh.
**Kayla Reopelle (New Relic, Inc.)** 33:45 Or zero-code instrumentation, that idea.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 33:48 It's a way to deliver a command that will do the rest of the work that we have had in getting started since forever. Yeah. Okay.
**Kayla Reopelle (New Relic, Inc.)** 33:56 Yep.
And, if you are interested in this too, Matt has another approach for how we could do this, because right now we're patching Bundler to make that happen. So,
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 34:10 This is Ruby Way.
Monkey patches.
**Kayla Reopelle (New Relic, Inc.)** 34:13 Anyway.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 34:14 Okay.
**Kayla Reopelle (New Relic, Inc.)** 34:17 But we wanted to get that first version out before we moved forward on the trace point.
**hannah** 34:24 I forget, is that part of instrumentation at all, or is it a separate gem for installing?
**Kayla Reopelle (New Relic, Inc.)** 34:29 This is a separate gem that includes instrumentation all as a dependency.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 34:36 Does… Is it… mmm… Okay, I think that answers it. The question I was going to ask is, I know that the Python auto-instrumentation does, like, looks at Things that are in, dependencies that you have, and then goes and gets the… Python modules that instrument them, as opposed.
**Kayla Reopelle (New Relic, Inc.)** 34:57 I wouldn't.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 34:58 everything. Ours is, no, you get all, and… We figure it out, and we do it live.
**Kayla Reopelle (New Relic, Inc.)** 35:05 Okay. Yeah, but I think, Matt, is yours a little closer to that Python approach that Rob was describing?
**Matthew Wear** 35:14 I mean… all the gems are so bundled, so I feel like that's not different.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 35:21 I'm okay with that.
**Matthew Wear** 35:23 I feel like fetching things at runtime seems fraught with peril, thinking about that?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 35:28 Yeah, oh yes, it's not… it's not a fetch at runtime, it's we figure out… we do it live, in that we have everything available, and we, load based on, So, yeah, dependencies… all dependencies are resolved and retrieved before runtime. It's just at runtime, we decide whether they're loaded or not.
**Matthew Wear** 35:46 Got it, got it.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 35:47 Which I approve.
I mean…
**Matthew Wear** 35:50 That's kind of how the instrumentation bass class works.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 35:55 Right, that's… yeah.
**Matthew Wear** 35:56 You just go through and try to install each one if, you know, its predicates pass.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 36:03 My philosophy has been, you start, like, you want the easy button, here's the easy button, the easy button includes everything, and if you have a problem with everything being there.
Take what you'd want out.
**Matthew Wear** 36:15 That's kind of been the philosophy.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 36:17 Yep.
Cool.
**Kayla Reopelle (New Relic, Inc.)** 36:22 Okay, nice. And this is also using trusted publishing with Ruby Gems, so that's something we could look into as well for other repos eventually.
I don't think Toys supports trusted publishing yet, though. It was something Daniel talked about supporting, but… Just noting that.
Alright, well that is our… agenda, Does anyone have anything else that they want to talk about today?
Going once.
Going twice?
Alright, cool. Well, thank you everyone for coming today. It was really great to see you all. And, yeah, we'll chat more online.
And next week, be prepared for a presentation on the status of where we're at with metrics and log stability, and some brainstorming on how we can, get closer to a place where we can actually request the spec SIG, or TC, to review.
Thanks. Sweet. Bye, have a good day.
