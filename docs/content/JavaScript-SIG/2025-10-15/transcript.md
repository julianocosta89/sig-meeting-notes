SIG: JavaScript SIG
Date: 2025-10-15
Duration: 68 minutes
Zoom Recording URL: https://zoom.us/rec/share/lAi_DGX31Ajaebts1H9Qn1lXafs8Ly4eYf5gtmjCIeFHiWU756R4xAkMZrDu1SNR.SlGQLixoA4ezL2FO
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:09:54 Hello?
Raphaël Thériault 00:09:59 -Oh.
Hector Hernandez 00:10:05 Hello?
Marc Pichler (Dynatrace) 00:10:13 Let's start to troubleshoot my screen real quick.
Alright.
So, first topic here on the agenda is, welcome, David, to the JS Maintenance Group. I see he's not on the call right now, but, Yeah, we added David, I think, yesterday to the maintainers group, and also welcome, Jackson Weber to… JS approve us.
So… Gap.
That's the two changes, that we made for now. And, yeah.
I guess, in terms of approvals, we're gonna, also make a few changes here and there still, if… That is something, that you're aspiring to, like, to become an approver, please feel free to reach out to either of the maintainers, And, we can tell you how to get there.
In the end.
Alright, with that out of the way, I guess we can go on to the regular… part of the meeting, just a lot more topics here. The first one is… yard that I, marked for review recently.
This is… PR that allows, basically dynamic headers, which is intended for, OAuth2 token refresh and stuff like that.
It's a… Feature that was requested quite a bit in the past.
And… it did work.
To some extent, in the past as well.
Where you could, like.
go through private, or properties that were intended to be private, and, set the headers later on. It wasn't a perfect solution, because, You would run into a race, based on… When you would set the token, it was kind of finicky, so this one actually makes the function async, so you can obtain the headers.
And it's awaited before each request, and then you can actually use these there. Most of the code was already there, so it's… More or less just changing it to be async, and then also exposing it to the user.
Yeah, if anybody has time, please feel free to have a look.
And, yeah, hoping we can get this in, at some point.
Trent Mick 00:13:25 Any immediate questions?
Marc Pichler (Dynatrace) 00:13:30 If not, then I guess we can move on to the next one, which is Luke's topic, adding an OpenTelemetry instrumentation for, MCP.
Luke (GuangHui) Zhang 00:13:44 Hey, hello team. Yeah, this is my contribution to the JavaScript MCP intervention library. Now, we are facing a challenge, as MCP is very popular a lot.
organization developers are building MCP, but we need a way to, have the opportunity. Especially, I think the number one priority is, trace contact propagation.
The MCP server plays a role, just like a broker. It's just a man in the middle. Right now, MCP SDK from AmazonPik doesn't propagate the OpenTentry context.
Which is causing the broken traces in the whole system.
So, it's sort of urgent to have this kind of things, you know, to propagate the open telemetry context from the agent app to the MCP backend system.
So this is my, PR, which will do… which will do the, first do the context propagation. Also, we'll add some attributes. The attributes will… you know, it depends on a semantic convention for MCP, which is an ongoing project. That one, probably, as another thing, This is basically the, the background of, of this, project.
I also created the Python. Also, that PRA has been submitted to the OpenTemmetry community.
Marc Pichler (Dynatrace) 00:15:18 So the, semantic conventions, I'm not too up-to-date with, Is that something that's already in there, or…
Luke (GuangHui) Zhang 00:15:28 They have a PR in the semantic convention, get a repo, and it's not a finalized, it's a draft.
But I think we should not wait for that, because the context propagation is a blocking issue for us.
Marc Pichler (Dynatrace) 00:15:46 Is there any chance you could get started with a smaller PR that just does the context propagation first, and then we gradually build on that?
Is that a possible way forward for this?
Luke (GuangHui) Zhang 00:16:00 Oh… The… So, mmm… Yes, it's definitely doable. Many of the rationale to do this, just split this.
The reason is that I'm asking this is I think, the semantic, convention, the attributes, I define all of them in a… as a constant in a single file. It's a… it's pretty easy to adjust them, you know, when we have finalized the semantic convention for MCP.
Marc Pichler (Dynatrace) 00:16:31 Yeah, I think, so what I was getting at was that, given that the PR is, probably quite large and there's a lot of review, if the biggest issue that you're having right now is the missing context propagation.
Doing that separately, and then going with the other features of the instrumentation might be a quicker route to go.
So, yeah.
Luke (GuangHui) Zhang 00:16:58 Yeah, that makes sense. Yeah, that makes sense. Actually, not a lot of code. I think most of the code are just testing code, and the examples. I built two examples to demo today how this works. But the core code, it's just a tool file.
Instrumentation.cs, that is 300 lines of code.
Yeah, that's the… that's the core, core.
Marc Pichler (Dynatrace) 00:17:27 So, yeah.
I will have a look at this PR, And… yeah, we can see where it goes. One thing that's important with new instrumentations is always that we have at least two component owners.
So, that's something that is a hard requirement for us, so if you have somebody who would also be interested in taking on, maintenance responsibility for this component, please add them to the, component owners file in the .github, directory, and yeah, that will ensure that we can get started reviewing this.
One thing that sticks out to me Now, just looking at this, immediately, is… The direct use of requirement… require in the middle and import in the middle, because usually we have these…
Luke (GuangHui) Zhang 00:18:28 the base class?
Marc Pichler (Dynatrace) 00:18:30 The base class that, it's used there.
Luke (GuangHui) Zhang 00:18:34 Yeah, I tried that, but I couldn't figure out it didn't work, work out, because, you know, the, and certainly because the MCPSDK, It's… it's quite weird. I understand that we also have the wrapper in the base class. Ideally, you know, I should not… use these two packages directly. Unfortunately, I, I couldn't figure out, make it work with Android SDK.
Marc Pichler (Dynatrace) 00:19:05 Alright, yeah, I guess we can have a look at that during the review anyway. It's just something that stuck out to me, right away.
S.
Something that's a bit different than usual.
Alright, yep.
Luke (GuangHui) Zhang 00:19:22 Yep, I look forward to working with the community to make this contribution. Feel free to reach out to me on Slack.
Marc Pichler (Dynatrace) 00:19:35 Alright, yeah, thank you.
I will definitely have a look, then we can go from there.
Luke (GuangHui) Zhang 00:19:45 Thank you.
Marc Pichler (Dynatrace) 00:19:49 Alright, any questions for Luke?
Not there, I guess we can move on.
Everybody's favorite.
part of the meeting, which is triage.
Let's get started with the core repo, There's still this one here, I guess that mostly needs documentation, so I will, put the P2 label on here, and documentation is already assigned to me, so I will pick it up.
To document, which versions are supported and which ones, Which ones aren't, and also which bundles are supported.
Seems that… There's actually an issue in the browser repo about bundle support.
Oh, and there's this, exports field, which is required.
Seems like that's the first pass, but…
David Luna Bistuer 00:21:13 Yeah, I guess tomorrow we'll… sorry, Mark, I guess tomorrow we'll have a discussion about this table. This is kind of the first contribution on that… on that ticket.
From a note.
And I guess we'll be very trivial with the rest of the SIC.
Trent Mick 00:21:31 Was that required that Mark has highlighted there? Basically, the browser SIG saying, yeah.
To… for us to support a bundler, it has to support exports?
David Luna Bistuer 00:21:43 Yeah, that's kind of the idea. So first, they want to kind of work in this idea of having a list of what features they want to Yeah. Support.
Trent Mick 00:21:52 Be able to lend.
David Luna Bistuer 00:21:53 from that…
Trent Mick 00:21:54 Yeah. Yeah.
David Luna Bistuer 00:21:56 And then from there…
Trent Mick 00:21:56 Right, so that basically means… okay, so that basically… sorry, I'm gonna speak over here. That basically means that Webpack 4 is not something we need to support then, right?
And then we could just point people to that workaround that… that, jared.
David Luna Bistuer 00:22:10 Exactly. I think that, I guess tomorrow we'll want to talk about that, and then if that's the idea, I guess we should write some documentation for, you know, for.
Trent Mick 00:22:22 Beh.
David Luna Bistuer 00:22:23 If there is a possible workaround for them.
From the excluded, bundles.
Trent Mick 00:22:28 Everyone loves writing docs.
Marc Pichler (Dynatrace) 00:22:37 Yeah, I will definitely keep following this, thing here, if there's anything that we need to change in the repositories to, accommodate more, bundlas, that's also something that we can, I guess, look into. The exports thing, I think, is the largest issue right now, which isn't supported in some versions of bundles and, Cop.
So yeah, thanks for, raising this here in the, processing as well. Very much appreciated.
Alright, That was it for the poor repo, I think.
Yes, and then we can move on to… One trip, which has zero new bugs, which is nice.
Just checking here, if there's anything… It immediately sticks out as a puck, but Wasn't categorized as such, but it looks like we are okay on this one.
Yep, and then we can move on to PR triage. I forgot to say, if anybody has any topics you would like to discuss while we're doing triage, please just let me know, and we can go back to the agenda and talk about the topic that you would like to discuss.
Otherwise, we will go through with, PR triage session.
This one… I guess there's nothing… nothing new on that side. Oh, no.
Then there's the page view instrumentation, and I think we had a second instrumentation… Which was Browser Navigation opened last week.
So I guess that's… that's what we're going to look at first, I suppose.
Looks good on all us, There's an example for two, so… yeah.
bunch of code to review, though, so I will put… Target cross and labor on here.
There's a few conflicts…
Marten Hennoch 00:25:47 Do we know what's the… what's the browser CX idea about the browser code? Will it live in… Node repo, doesn't really make sense. We have, like, doesn't seem there is nobody to review those, besides Martin.
So what's the plan going forward?
Trent Mick 00:26:05 Yeah, we've been kind of treading water on those ones to see… for a while, at least, to see if the browser seg was gonna, like.
definitively decide.
one way or the other, what they wanted to do with some of the in-play instrumentations. At least that was my read. I think David might know better. But didn't, Didn't Martin… the other Martin, Martin Kuba, close… a different instrumentation PR in this repo, and open a similar or related one in the browser repo recently, so, like, I wonder if… Over time, they'll work through all of these ones.
Marc Pichler (Dynatrace) 00:26:43 I'm not aware… I'm not aware of any…
Trent Mick 00:26:46 There's one that moved recently.
Marten Hennoch 00:26:52 I mean, if we… if we approve those PRs, then… and somebody starts using them, then we… it's hard to get rid of those.
Trent Mick 00:27:00 Dennis. Yes.
Marc Pichler (Dynatrace) 00:27:02 Yeah.
I guess likely we would still keep using the same NPM, the same NPM scope, for both of them.
So the telemetry one.
So, there's some flexibility, at least, to move between repos with the packages.
But yeah, ideally having them in the place that they're gonna live long-term is… Probably better.
I'm also not true what the current,
Trent Mick 00:27:38 So Martin had a comment.
Martin had a comment in the… browser Slack on Friday, saying, I've moved all issues for adding new browser instructions from contribib to the browser repo.
Marc Pichler (Dynatrace) 00:27:49 So, is this…
Trent Mick 00:27:51 Is this just one that… Just fell off the list.
Martin had reviewed this in the past, but…
Marc Pichler (Dynatrace) 00:28:01 I guess it, so the comment there was mostly around triage permissions, I guess, because, we haven't sorted out any, permissions or rollers between the processing and the, JS repos yet.
that's something that we still have to look into.
Yep.
Personally, I'm not opposed to… Either of the two approaches, like, having it in the, JS repo, or having it in the browser repo, I'm, actually okay with both.
Trent Mick 00:28:36 Yep.
Marc Pichler (Dynatrace) 00:28:39 So, whatever the browser sig decides, that they want to do, I would just follow, Follow li- follow the lead on this one.
As they, know which requirements they have, and what works best for them.
Yo.
So, I guess that's the long way around of saying we don't know yet where they're gonna live, but we will figure it out in time.
Right.
Excuse me. So… Next one is… I think that one was…
Trent Mick 00:29:46 I promised to look last week, and I haven't yet.
Marten Hennoch 00:29:48 Sim is on a vacation anyway, so… He will be back next week.
Trent Mick 00:29:54 Okay, and I'll be away for part of next week, so it'll… hopefully I can get there this week. Look at it. Oh, no, David, you're already looking, right?
Marten Hennoch 00:30:03 Yeah, he has had, like, comments.
Trent Mick 00:30:05 Oh, that was in September.
David Luna Bistuer 00:30:06 Yeah.
Trent Mick 00:30:07 Yes.
Marc Pichler (Dynatrace) 00:30:10 Alright, yeah, then, let's keep this open, and then… once there's been some activity, we can have a look at this one. There's another processor… Yeah, There's one comment, but no activity since then, and… the changes requested are for component owners, which I guess this one is still missing, so… Nothing to do for this one.
Huh.
then this PR… I have approved, and we can actually merge this one.
Alright, then the next one is… something that I think Jamie had started looking into, we haven't had any… activity here yet, but I… did have a sync with Jamie on this one.
Last week… And there's a few things that we first need to figure out, how we're gonna merge things together. I did a review of How we handle environment variables in the core repo, and how to… precedence, usually.
works there.
And this one is doing something that's a bit different to what we do in the core repo, which is, uses the auto-node-disabled instrumentations as, like, the absolute priority, and if there's a programmatic config.
then… This one overrides that.
Which… It's usually not the way around that we go. We usually have the programmatic config be the absolute priority, and then have Things override that.
But other alternate SDKs do different things, and it's not specified, which way around to go. So… yeah.
Still trying to come up with a definitive guidance for this one.
Yeah, but it's being worked on, so… -Oh.
Trent Mick 00:32:51 Do you know if the spec has an opinion on the… Alright, I know, it gets really confusing with declarative config and stuff coming too, but…
Marc Pichler (Dynatrace) 00:32:59 Yeah, I think with the declarative config, at least it won't be, So the declarative config will only take environment variables when You actually put them in the file, to get substituted.
Which simplifies everything a bit.
Trent Mick 00:33:20 Though with the added confusion that declarative config is not yet handled, tackled, any… configure… it doesn't… the schema, and I'm not sure if it's been discussed, but the schema doesn't have anything for deciding whether instrumentation should be enabled or disabled, so exactly the example we're talking about here is not covered by… anyway, yeah.
Marc Pichler (Dynatrace) 00:33:45 Yeah, I guess when we get there, we would also follow a similar thing, where we would just not, read the environment variable at all.
In that case, having the, config the code-provided config override environment variables would be in our favor, because then we could just pass in whatever generated config we have, and that will for sure override it. Whereas if we now go the other way around, where, the… The environment wherever it takes the highest precedence, and we later have to do it, we will have to, introduce some option to turn that off.
Boom.
Yeah.
when looking at the what would Java-do thing, where Java usually does the right thing, they… they actually allow overriding, with the environment variables. I guess the idea there is that, somebody who Who configures things.
with some options somewhere, they… they just want to change the behavior and, like, override something, so… that's why they went this route. I did some digging, and I found… fewer threats, on the Java.
repos, where they were talking about this. It's exactly the opposite decision that we made back then, for environment variables.
Yeah.
Trent Mick 00:35:28 Good.
Marc Pichler (Dynatrace) 00:35:32 It is, tricky.
Interesting.
I guess, while we're talking about it, do you have any preferences?
Trent Mick 00:35:44 Which pipe?
I find it… well… I don't want to pigeon myself right now. I know in our… in our… at work, our… Free hotel agents.
Explicitly said that environment variables Win are a higher priority over a built-in set, but I think it gets a little bit… tricky. If someone's written bootstrap code that specifically passes in a value, then I don't know, yeah, like… I don't know if that code should have to be responsible for, like, the leading environment variables so that they don't come and override kind of thing, but I don't know.
With OTEL, it gets a bit more tricky, because, like, is the SDK… A thing for… Companies to build distros.
So that they can use the built-in functionality, but then users… Which might set things programmatically, but then still want users to be able to override with environment variables or not.
So it's… it's a little bit harder to decide, I think.
Marc Pichler (Dynatrace) 00:36:53 Hmm.
Yeah, I can definitely see, the… The value in both, both approaches.
Like, one, having the environment variables, override the… Configging code, and also the other way around.
Not sure if there's a right or wrong way in this sense, but if we can ever, remove the… environment variable config from the actual SDK packages, and have them be separate.
I guess, that would be ideal, because then… we can… Have whoever uses the things, choose which way they want to go, and not dictate by… Dictate to the user.
what's gonna happen by, having it built into, let's say, the export or whatnot.
Trent Mick 00:37:59 Yep.
Yeah, I agree, that sounds good.
every time I spend some time trying to get to a starting point to look at Morelia's configuration work, or any of the PRs around there, I've… I still haven't yet gotten to the point where I have, like, this grand vision of… How config should be handled with the various packages.
So yeah, I don't know. I don't have an opinion yet.
Marc Pichler (Dynatrace) 00:38:28 Alright.
David Luna Bistuer 00:38:34 Don't bother for those.
Sort of the SM1.
Marc Pichler (Dynatrace) 00:38:38 That's a reward.
David Luna Bistuer 00:38:39 I'm gonna close it.
Marc Pichler (Dynatrace) 00:38:40 Deese for now.
Alright, next one is… dependency update… We haven't merged this one, and it's been sitting for a while.
Usually, we don't look at the dependency updates, but I guess… While we're looking at this.
Seems like it builds, and… I'm not sure what, It looks like it bumps here.
Trent Mick 00:39:18 I'm not sure if it matters, but it bumps node min requirements to higher than our… base, minor versions of 18 and 20. I don't know if that hurts.
I mean, this is only going to be used for tests, I think, right?
Marc Pichler (Dynatrace) 00:39:32 Yeah, I think it's only gonna be used for tests, and I'm not sure which version the browser tests run at right now.
This one here.
David Luna Bistuer 00:39:51 I recall correctly.
Trent Mick 00:39:53 22…
David Luna Bistuer 00:39:55 22nd, yeah.
Marc Pichler (Dynatrace) 00:39:57 Okay, then I guess we should be fine merging this.
If there's a problem, I would just… Revert this one. That's fairly straightforward anyway.
I'll approve it, and then I'll merge it in when I… Get to, merchant PRs at some point.
Right.
This one here is probably…
Trent Mick 00:40:42 closed session.
Marc Pichler (Dynatrace) 00:40:42 Alright.
Trent Mick 00:40:43 It is, yeah, I'll close that in a second.
Marc Pichler (Dynatrace) 00:40:46 Thank you.
Oh… And the next one is… Stabersonv.
Thing?
Don't record anymore. Did I want to type up something here, or… It must.
Trent Mick 00:41:10 I think we need to come back to this one. I think instrumentation and QPlib might be… the hardest one for us to decide what to do. The… the… I guess the outstanding question I have for messaging stuff is… Well, one… I'm confused. So, the messaging… SEMCOM is not yet stabilized, so I think we decided, discussing this one last time, that we don't want to… merge this as is, because we shouldn't be exposing the opt-in environment variable for people to say, I'm opting into the stable, but it's not stable yet, so it could change on them.
Yet, they do have the first warning block there as suggesting that implementers should start providing opt-in environment variables. What does that mean?
Marc Pichler (Dynatrace) 00:41:59 Hmm.
So, I will write up an action item for myself, because I'm… In the same office as… show off from the messaging SIG.
I would just ask him.
That would be great.
Trent Mick 00:42:20 Yeah.
What we should be doing.
Marc Pichler (Dynatrace) 00:42:25 I think he was also very active in this messaging, some conf stuff.
So, he should have quite a bit of context.
Oh, no.
And then…
Trent Mick 00:42:41 Then, for MQPLib, if I remember correctly, we talked about using the HTTP Token in the opt-in environment variable for the net dot.
things. MQPLib… the current instrumentation uses some net dot ones, which maybe should change the network dot, but now if you go look at the current SEMCOM for messaging.
it uses some of the same NetDot things that the HTTP stable spec does, but for different Purposes.
And so then I got confused again on that one, so… I don't know. But if you can ask about what the stability story is, that would be… That'd be a good start, I think.
Marc Pichler (Dynatrace) 00:43:26 Yes, I will assign myself, Here, so that I don't forget about it.
And, yeah, then we can… Continue on with this one.
Alright.
The next one is… Building SQS context propagation… Some discussion here… There was some…
Trent Mick 00:44:25 I'd also been asked to comment on that one, but I haven't looked.
Marc Pichler (Dynatrace) 00:44:57 I guess this one… Just seems to have…
Luke (GuangHui) Zhang 00:45:02 Yeah, I can help a little bit on this, because Jonathan seat is just very close to me. Feel free to Slack me, and I'm happy to… Helps the communication?
Marc Pichler (Dynatrace) 00:45:15 Thank you. I think the communication here is mostly… Between Jonathan and… this person… I might need some… input from us, or SEMCOMF as well, so there's actually quite a few moving parts.
I seem to remember there being some SAMConf issue, that was opened about this… Where… SIMConf wasn't updated yet for… lambda spec, or something.
But this… Probably won't be able to find it here.
Yeah, no, probably won't be able to find this out on the car, need some further digging. But, thank you, Luke, for, offering.
To get the communication started again, I just need to read into, what, question I would actually ask, before.
-Oh.
Before being able to continue here.
Alright, then… Let's move on to the next one for now. This one… I think has now a different… It has a chain of 3 PRs, if I recall correctly.
So, I will… Close this…
Trent Mick 00:47:48 Oh, is that one no longer relevant?
Marc Pichler (Dynatrace) 00:47:51 Yeah, I think there's now a new PR, because the person that opened this one, was interning at… Company, and… No.
this one is the successor PR to that one.
Because they won't have time to drive this… Anymore, since the internship ended.
So, I were… Close this in favor of that one.
And this one here is probably still… Valuable as a, reference.
So, I will keep this one open for now.
So, once the actual instrumentation code is added to the package.
We can use this one as a reference of what the full picture is.
And there is one PR for instrumentation I already saw.
Or description.
Trent Mick 00:49:21 My memory, if this one is set, the idea looks good, it just needs review.
Marc Pichler (Dynatrace) 00:49:30 Alright, yeah, I probably won't be able to… Continue with anything here on the cart, but… Okay.
Seems good there. And this one here… Just closed.
Then we have… this PR… Which hoists our dev dependencies to root. I'm not sure if we have discussed this one.
E4, this seems to be… One more comment, if node 18 support is needed.
Yeah, I think just dropping Node.js 18 support… Like, that wouldn't be something that we would want to do.
I'm actually wondering why… I won't drop it.
Trent Mick 00:51:17 I don't know what specifically we're talking about. I had been discussing this with Jared a little bit.
You mean on this comment about…
Marc Pichler (Dynatrace) 00:51:31 Good.
Trent Mick 00:51:31 We… we already get… we already get unsupported engine warnings for some… some of the things, so I don't… Unless he has other… reasons for thinking that's… sorry, he needs to worry about Node 18 support. I don't think those two warnings indicate that we have a problem on this PR.
Marc Pichler (Dynatrace) 00:51:49 Hmm.
Trent Mick 00:51:49 Yeah, so…
Marc Pichler (Dynatrace) 00:51:51 Yeah, there's, I've also seen that there's quite a few warnings about that.
I think most of it is dev dependencies, but there's also a few packages that, R.
instrumented that are causing, warnings to be locked on in-store.
Freedom.
Trent Mick 00:52:20 Oh, I think that was actually… there was a conscious decision. I pushed… But that, I think, saying that.
So, the argument is, we support back to Node 18, where it makes sense But… That doesn't mean that our default testing should have… of… a module under test should have to stick at some Godawful old version.
Because we have test all versions for that, so…
Marc Pichler (Dynatrace) 00:52:53 Yeah, I think that makes sense.
There's quite a few here. I'm pretty sure I have also merged… merged a few Renovate PRs that have updated stuff.
Trent Mick 00:53:07 Okay.
But yeah, I'm.
Marc Pichler (Dynatrace) 00:53:09 As long as…
Trent Mick 00:53:10 Time packages there, so…
Marc Pichler (Dynatrace) 00:53:13 Yeah, I think it's mostly just this Azure thing.
Which I… don't recall exactly anymore where it's used. Probably the Azure, resource detector or something like that.
But as long as it's not significantly more than what we have on main right now, I think that should be… should be fine here. So… Jared doesn't need to…
Trent Mick 00:53:46 Don't worry about that, yeah. I can follow up on this one at some point, but yeah.
Alright, well, I'll add a comment about this one right now, but yeah.
Marc Pichler (Dynatrace) 00:53:54 I think we're generally in agreement, though, that we want to hoist all the def dependencies, right?
I'm in favor of doing that, since we likely can't npm install in the actual package anymore anyway.
We might as well hoist them, and get some… deduplication going.
Trent Mick 00:54:19 Yeah, I'm fine… fine with it. I mean, I'm… I don't have a strong opinion either way, but it sounds fine.
Marc Pichler (Dynatrace) 00:54:29 Right.
If anybody is opposed, please just comment on the PR.
Alright.
Then we can move on.
Oh, the next one, which is Instrumentation GraphQL.
This adds the option to have all the spans be like this instead of this.
David Luna Bistuer 00:55:21 You can assign this one to me, Mark.
I rarely see a review with a previous, yeah.
I'm this contributor, and Aaron Oveckney.
And I usually… well, he's not responding, so… I'll take a bit.
Marc Pichler (Dynatrace) 00:55:42 Thank you for looking into this one, GraphQL.
is not my strong suit. So, yeah.
Thanks for having a look at that.
Excellent.
And the next one is a fix for… X-ray propagator… There were comments… Jonathan didn't move yet.
I'm gonna check real quick if there's anything… all of the ordinary here in the diff, and approve the workflow run, so…
Luke (GuangHui) Zhang 00:56:42 Can I… sorry, sorry, bothering you, can I request it to be… become a AWS component owner?
So that'll give me my, I can contribute to this component, because I'm working with these things.
A lot.
Marc Pichler (Dynatrace) 00:56:57 But, yeah.
Yeah, if you want to become a component owner, please feel free to just, open an issue.
Here? Or a PR, or a PR…
Trent Mick 00:57:09 Oh, there you go, cool. I didn't know that.
Marc Pichler (Dynatrace) 00:57:11 There's a component ownership request, and… That just makes sure that, you're a member of the org, and, yeah, just gets a few things out of the way, because once we add you through a PR, as a component owner, we usually also give you triage permissions on the contract repo, and for that, all these things need to be fulfilled.
But, yeah, that would be the way to go. If you just open an issue, I will likely pick that one up, and then guide you through the process.
Luke (GuangHui) Zhang 00:57:47 We'll do that. Thank you.
Marc Pichler (Dynatrace) 00:57:48 Yeah, thank you for offering to become a component owner as well. The AWS components, they get a lot of, traffic, so having more people is better in that case, for sure.
Luke (GuangHui) Zhang 00:58:00 Sure.
Marc Pichler (Dynatrace) 00:58:07 Right. Keep producing.
Where we… were last time, so this was this PR here.
Yeah, looks like that was actually addressed fairly recently.
through this push, I suppose. So, we can leave this.
Here for now, and then… circle back to it at the later date. And… Dependency PR. We'll just leave it running for now.
Then this is a bug fix PR for instrumentation radius.
I didn't review this one… I actually triage this, this, issue here.
The problem here was that the… Anything that's started, like… So, with this pipeline or multi-thing, didn't have the proper… mode set, I think it should be prefixed by… more to your pipeline.
And that wasn't the case, so what they're doing here is they add that to the… So… We'll just spends here… And… That was something that hadn't been instrumented yet.
So it seems that this here is just doing it for the Redis instrumentation, and then… It will create a second one.
So… This one here actually seems to be fairly simple.
I'll have a look at this one, flying.
But I will assign myself here.
So then I don't forget about it. Yeah, it looks fairly simple, so… Shouldn't be too much of an issue to… Get this marched.
And then this one here is for an unmaintained component. We talked about this last week, I guess.
Awesome.
Marten Hennoch 01:01:15 Just click Merge.
died.
Marc Pichler (Dynatrace) 01:01:20 I can… I can just enable all the match, but I can…
Marten Hennoch 01:01:24 You can click update, at least.
Updiction.
Marc Pichler (Dynatrace) 01:01:29 I, I will, I will do that.
Marten Hennoch 01:01:31 It's something, hold on.
Marc Pichler (Dynatrace) 01:01:32 Yeah.
Yeah, we'll get back to this one.
Marten Hennoch 01:01:46 I'll try to go to TGS GitHub and find someone to review.
Also.
Trent Mick 01:01:56 I sit and take a look, but I'm slow.
Marten Hennoch 01:01:58 And you will also leave next week.
Trent Mick 01:02:03 Indeed.
Marten Hennoch 01:02:05 Leave, he said. He will be away.
Trent Mick 01:02:07 Next, yep, yep, yep.
Marc Pichler (Dynatrace) 01:02:20 Still need to get that one.
Reviewed here, and then we can move on to the… Next one, which is… Test our versions in parallel.
I guess we had talked about this one before, is… this is this… pitch, or… Histor versions where… if I recall correctly, it just… allows you to… Two things in parallel, and it might also serve this situation where… It leaves it in a state that might have a different package installed.
I have to take a look at that one.
It seems fairly promising, but if I recall correctly, there was also a Tesla versions PR.
That was trying to upstream this one.
Looks like no movement on that.
ideally, I'd like to, avoid… Vendoring this component, or, like, having this patch and have it applied here.
on… But I'll have a look at FPR at some point, and And we can…
Trent Mick 01:04:33 Continue the discussion there.
Marc Pichler (Dynatrace) 01:04:35 Renovate bot PR, we can also… Skip that one.
This one we had a look at earlier.
There's nothing to do for this one yet, and .
Trent Mick 01:05:10 Yeah, no, that's on me to finish. Some draft.
Marc Pichler (Dynatrace) 01:05:15 We'll skip that one. Release PR, we'll also skip that one.
Boom.
I don't know, we have another AWS… thing here, I had commented on that one.
this… so what this basically does is it just changes the dependency here to a caret version. I'm actually… okay with this one, though I feel like the more permanent fix would be actually to copy the actual type to the package here. Usually what we recommend is in the guidelines, to Use this, types package, As the first thing here, but the problem with this types package is that it actually defines global types, which causes conflicts.
So, option 2 would be to copy the relevant type declarations, if they're simple and short.
It's not exactly that, but it's close enough, I would say, to actually copy this one, and then circumvent the problems with the global type definition here.
But… I will actually approve this one, because I'm fine either way.
And… Bing.
I'll wait for Jonathan to also have a look at this, and… And go from there.
And it looks like we are actually out of time. So… Yeah.
That is it for today.
Thank you, everybody, for joining.
N4.
sticking with us through the triage session. I know it's difficult sometimes.
Yeah, thank you everybody, and see you next week.
Hector Hernandez 01:07:53 Thank you very much.
Trent Mick 01:07:53 Thanks, Mark.
David Luna Bistuer 01:07:54 Zip.
Trent Mick 01:07:54 Thanks.
David Luna Bistuer 01:07:55 But…
Marten Hennoch 01:07:55 Bye.
Marc Pichler (Dynatrace) 01:07:56 Wait.
