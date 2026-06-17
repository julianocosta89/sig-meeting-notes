SIG: Ruby SIG
Date: 2026-06-16
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:41 Hey, everybody.
**Hannah Ramadan** 00:45 Hey guys.
**Kayla Reopelle** 00:54 Right, there's a link to the meeting notes.
I don't think we've heard anything from people one way or the other about joining today, so this might be all of us. Oh, okay, there's Matt. Welcome, Matt.
**Matt Wear** 01:26 Hello, thanks.
**Hannah Ramadan** 01:28 Hey, Matt.
**Kayla Reopelle** 01:39 Okay, cool. I will… Share my screen… So… I had a really hard time sleeping, and I overslept through the spec sick today. I hopped on for a minute, and then realized I wasn't quite awake yet. So, Matt, I see that you were there today. Is there anything that you could share with us about what was discussed?
**Matt Wear** 02:10 Yes.
Yeah, there's a… there's a policy OTEP, I don't know if anybody has seen that, but, Yeah, when I was first looking at this, I was really thinking about it in terms of the collector, because I think that's what it's… Definitely… It's, like, an initial use case.
But the idea is that you can kind of send down some configuration from, like, a remote location, and then, The thing that receives it would apply it.
And, generally, I think this is what you want to do if you're managing, like, a large fleet of collectors, but I think what I was starting to understand when people were talking about this is it also, applies to SDKs, potentially.
So yeah, I think this is definitely interesting, and I think, it's something that, That people are going to want one way or another, but there's just a call to kind of, look at this OTAP, read it, provide some feedback, and hopefully, ultimately, approve it.
I think it's been open for a little while, but the author is just kind of doing the rounds, I guess, and trying to get this, Ultimately approved.
**Kayla Reopelle** 03:26 Nice. Thanks.
Anything else you had to call out?
**Matt Wear** 03:36 I don't know that we need to go down this can of worms for the key attribute… key value and unit thing.
I think the ones that are most relevant are, there's this context… context scoped attributes OTEP. I don't… I know, like, This idea has been around for a long time. I think I've brought it up in past meetings, but I think there's actually been an OTEP around it since I've been around last.
And… Yeah, I think, ultimately.
This allows you, kind of at a context level, to add attributes to your context, and then they should cascade onto.
**Kayla Reopelle** 04:29 Hmm.
**Matt Wear** 04:29 Traces, logs, and metrics, rather than having to add them all individually.
And, I think we do need to kind of look at, like, how we would actually implement this and make it work, but I do think it's a really good idea, and probably will be… quite, quite helpful in the long run for us.
**Kayla Reopelle** 04:51 Nice.
Yeah, that does seem really helpful, to just have something added to all of those signals.
**Matt Wear** 05:01 Yeah, and I think, you know, OpenTelemetry kind of started with tracing, and then… added metrics and then added logs, so I feel like… If we would have known.
If we would have had all three from the beginning, we probably would have had this from the beginning, I guess.
**Kayla Reopelle** 05:18 It was kind of…
**Matt Wear** 05:19 After, as you kind of added the signals, and then had to add all the attributes to each of the signals, you kind of realized you needed this.
So just that one, and then, there… Is the proposal to expand span processor?
And… Yeah, so there's 3 more methods that… Would be added to it.
I think, yeah, you know, from a technical perspective, sure, we can add these methods. I'm just trying to figure out, like, what really the use cases are, and And yeah, I just feel like spam processor does not actually do anything that anybody wants it to do, which is unfortunate, and I'm just wondering if this… I just need to reason through this and see if it actually fixes anything, but I'm not sure that.
**Kayla Reopelle** 06:22 Yeah.
Interesting.
It does seem like a lot of… Callbacks to have available.
**Matt Wear** 06:39 Yeah, so, yeah, I guess that's it, and.
**Kayla Reopelle** 06:43 Okay.
Great, thank you.
**Matt Wear** 06:52 I don't know.
**Kayla Reopelle** 06:55 Yeah, I'll try to read through those.
Some of them I know, have been in discussion for a while, like the policies and the context attributes, so I'm sure they're getting to a… Close.
Conclusion.
Okay, moving into CORE… Schwan, you want to talk about this PR?
**Xuan Cao** 07:16 Yeah, So, for the character confirmation, this week, this week I made a video review, and, for the last two or three weeks, I have, upped the discussion with Mr. James, He gives some very good allies.
But still, there's a long discussion about, the extension.
For the, SDK… SDK?
I stand by mate.
view that, Ruby Cannot, well… I could… I can't say cannot have, but it's very hard to have a… extension.
Similar to, Java and the PHP.
Because of how the, how the language designed.
And I stand by my review that it should be a little similar to the goal, So, yeah, basically, I applied some of his advice, which is really good, and then… I kind of want to just ignore some… his request.
Especially, especially he wanted to, To make some change, in the, the SDK.
And I don't want to introduce any, destructive, change to the SDK. I want them separate.
So, yeah, that's basically it for this PR, and it is ready for review.
So, People are welcome to take a look.
**Kayla Reopelle** 09:01 Nice, sounds good.
Yeah, I'll take a look at the… Feedback, too, and see, Kind of think through those things. It looks like most of the conversations were resolved. Is there anything… That you want other people to chime in on, or do you feel like, you know, they're pretty well taken care of?
**Xuan Cao** 09:24 So, most of the comments are about why not, how to extend, if, if, if users have, like, their customized, like, for example, processor or, exporters. Most of the comments related to that, and I think one of the, probably shouldn't, shouldn't resolve the… that… Black com- comments.
Boom.
I don't know which one it is, but anyway, yeah, You can, people can take a look on what we did, discussed. Yeah.
**Kayla Reopelle** 10:02 Sounds good.
Thank you for putting that together. I'm excited to read it.
And then… I don't see any other points on core, but… We should have just had a release for the metrics.
SDK and exporter with the cardinality limits.
so, those will be out in the world, available for use.
Yeah. They were released successfully.
So, any… other PRs that folks are aware of. Oops, that's the wrong column.
That should be prioritized this week.
Be nice to wrap these up. I know there were more comments on them.
And I think there's kind of a link in with this PR now.
And I haven't fully digested.
Yeah, what still needs to be done there?
And then I think we're still waiting on… TLA on this one.
Okay, on the issue side… We did have a comment this week on… Profiling?
And just, like, a request to… check in on our profiling process. I do not know… Where that was exactly, though.
I can find it and post it in the channel, too, if people are interested.
But it does sound like profiling is moving along, and they're looking for some… Implementations.
Anything that folks want to look at together here before we move on to contribute?
**Matt Wear** 12:16 I was just gonna ask briefly, I see there's a handful of PRs to, to update our COPS? Is that… is that something that we're actively, kind of, hoping to do, and… and generally in favor of?
**Kayla Reopelle** 12:30 That's a great question. It wasn't something that was on my mind at all. There was a pull request that was first opened by Arielle, and then kind of taken up by James Thompson-Tomo.
to, bring the RuboCop up to date.
I guess, like, I did ask, because in that PR, some performance cops had been disabled, and so I asked for those to be enabled, and then the rest of them, I think, were kind of… Newer follow-ups, so… it's… it's complicated, because it's not something that I particularly see as a priority, but we do have a community member who seems actively excited about making those kinds of improvements, so try to pay attention to them, or I try to pay attention to them.
**Matt Wear** 13:27 Alright, yeah, that's fine. I feel like… Yeah, if somebody is enthusiastic about this, and wants to do the work, and has done the work, then, yeah, I'm fine with it, so I'll go ahead and get some eyes on those.
dead.
Boom.
Yeah, I… I do think that we have way more priority things, but, you know.
**Kayla Reopelle** 13:50 Yeah.
**Matt Wear** 13:51 Like… This is open source, and people can pick and choose what they actually want to work on, so…
**Kayla Reopelle** 13:59 Yep.
Yep, I think we're on the same page there.
Yeah.
Oh, kind of thinking about… Right, or I guess I'll add this later on.
We can discuss it later.
Okay.
**Matt Wear** 14:18 Yeah, I would like to talk about renovate, so we can do that later.
**Kayla Reopelle** 14:22 Great.
Yeah, because I guess it applies to both repos, so we can… we can get to that one together.
Alright, let's… that was CORE, we already looked at that one, We can just pop briefly into Contrib before we get to burning questions.
The Active Job Continuation Step PR is, gonna be released after this meeting.
I did…
**Matt Wear** 14:53 I remember I took an action item to kind of look over, like, Messaging attributes, and how they.
**Kayla Reopelle** 14:58 I'm working.
**Matt Wear** 14:59 Between, you know, different.
**Kayla Reopelle** 15:01 Right, yes.
**Matt Wear** 15:03 And, yeah, I noticed that there's, like, actually an issue, There's an issue reference, where we're actually talking about this, and there's a conversation kind of going on, and… Yeah, what I did find is that, like, like, Python is probably the most similar. They have, like, Celery and, like, Remelade. I think those are both kind of, like, job processing frameworks, and… Oof.
**Kayla Reopelle** 15:34 What was the second one?
for celebrating.
**Matt Wear** 15:38 delayed.
**Kayla Reopelle** 15:39 Okay.
**Matt Wear** 15:41 But… Yeah, what I found is that for the most part, I think the only semantic convention that I found them using was, like, the messaging ID convention, and then everything else was just, like, in, like, a Celery namespace, or a Remolate namespace.
**Kayla Reopelle** 16:01 So…
**Matt Wear** 16:01 I feel like we're… Yeah, kind of what we're doing in OpenTelemetry Ruby, is… we're probably… an oddball, I guess. To state it one way, but ultimately, like, We seem to be defining a lot of, like, custom attributes in the messaging namespace.
And that's definitely something that I haven't seen anybody else doing, and I see the spec kind of, Frowning upon that, because… Ultimately, whatever is, Whatever namespace is owned by semantic conventions.
well, I don't think there's a huge risk of this, like, they could add an attribute, you know?
Of the same name.
And, like, then we would have a conflict. So they kind of owned… like, generally, I think they own the namespaces, you know, that are from semantic conventions, and anything that we're adding should go under, like, a different namespace, so… maybe we've been, like, too hesitant in the past to use our own namespaces, but from what I found looking around in the other repos, it seems like that's pretty widely done for things that do not map, kind of, directly.
**Kayla Reopelle** 17:26 Got it. That's great to know. Thank you.
I added some notes on, the SIG meeting notes, but I'm wondering if you would be, open to… Like, adding a comment on this issue with your findings.
**Matt Wear** 17:46 Yeah, yeah, I think… Yeah, I think I definitely have to do that. I'm dreading it, but I will do it.
**Kayla Reopelle** 17:53 Okay. Well, thank you. Thank you for taking it on.
I think that's really helpful. Yeah, the, with continuations, I think that just since we're only… we're adding a new feature, I don't think we need to break the whole pattern, for this particular PR. I would rather do something more… balanced, like, with an environment variable or config switch to move to these new attributes, since it seems like we do need to change things up, so it didn't, Makes sense to me to hold off until these were ready before we got the continuations functionality up to the community.
**Matt Wear** 18:33 Yeah, no, I think that's fine. I think there's, like, a whole… There's a whole cleanup, task that has to happen, and that's kind of what is being discussed in this issue, so whatever needs to be done can be done there. I don't… there was… there was no reason to hold up, that… that other PR, but that was the one that, We were looking at, when I at least agreed to look at things.
**Kayla Reopelle** 18:55 Yeah, yep.
Nice.
Okay, excellent. Thank you for… for looking into that and following up with it.
**Matt Wear** 19:04 Yeah, and then, I think just the last thing is, when we have these conversations in the future, I think that's… We should probably somehow… know that this is the rule. You know, like, if… like, don't add new attributes under a, Semantic convention namespace. Those are reserved for semantic conventions, and then if we have something that doesn't fit, it kind of should be in our own namespace.
And, And we probably have quite a bit more liberty than we, than we knew we had in that area, if… Unless everybody else is doing things wrong.
But yeah, that's all I have to say.
**Kayla Reopelle** 19:54 Great. Well, and this does kind of coincide, too, with having access to, Our own semantic conventions.
Namespaces for documentation. So maybe we try to couple that more clearly with Provided we're going to be using, if we use the Ruby or Rails.
Namespace, maybe we try to document things there.
as well.
Great. Okay, let's take a look over here.
Alright.
PR for semantic commits. Sean, is there anything you wanted to chat about on this one?
**Xuan Cao** 20:58 Yeah, I'm not familiar, it's just, renovate, so every time I have an issue, I have to open the PR tool.
person fix that, I asked AI how to fix it, so…
**Kayla Reopelle** 21:09 Okay.
**Xuan Cao** 21:11 Yes.
**Kayla Reopelle** 21:12 Cool.
Yeah, I'm kind of surprised it didn't come up in the… Other… like, a config that you copy over, but, I mean, down to approve that.
I'll, I don't know much about Renovate either, so I'll read a little bit about it before I approve it.
**Xuan Cao** 21:34 Yeah, every time I change the name to comply with the semantic, commit message, and then this generator just, updated it again without this,
**Kayla Reopelle** 21:49 submitting.
**Xuan Cao** 21:50 So, I was kind of annoying, so I'm sure you know why I didn't have that anyway, so… I don't know, I asked AF, but I have no idea.
**Kayla Reopelle** 21:59 Weird.
Interesting, yeah.
That sounds really annoying. Well, I hope this will fix it.
And then, did you get a chance to try the release yet? Or is that.
**Xuan Cao** 22:17 Not really… I wanted to… to test on the operator first, to make sure everything works fine, and then I… I, how I'll create those, raise.
Okay.
**Kayla Reopelle** 22:30 Awesome, thank you.
I guess we need to make a new, column.
For auto instrumentation.
But I can do that later.
Alright, renovate. Yeah, so… a few meetings ago.
I mentioned an interest in kind of, like, reducing the frequency that we have renovate, run, and open up new, PRs for us. Last week, I surveyed the other repositories in OpenTelemetry that use Renovate, and it does seem like our schedule is fairly standard.
Most repositories have, like, a once-a-week kind of check-in.
what I would rather move to is a monthly check-in. I… I think that… It's… it's just a lot of noise, kind of, compared to what What our capacity is day-to-day, and is kind of distracting overall, so… I feel like we had that longer cadence before. I mean, we didn't even really have dependable on and core for a long time.
And so, even… I wanted to just check with everyone, because it is kind of breaking with OpenTelemetry. I don't think there was a single… Repo that had that infrequent of a check-in.
I didn't want to just go ahead and open that up, and you know, I'm curious about what you all think for… other frequencies, or other ways to manage it, if you like the frequency.
Just kind of a check-in for the group here about how we think Renovate is doing.
**Matt Wear** 24:43 I'm fine with monthlies.
Unless anybody, like, opposes it, I think we can try it.
And…
**Kayla Reopelle** 24:52 Hmm.
**Matt Wear** 24:53 Boom.
If there's any feedback that is not enough, or if you want it more frequently, then we can address it then.
**Kayla Reopelle** 25:01 Okay.
**Hannah Ramadan** 25:08 Yeah, I agree with Matt on that as well. I think it's okay if it, like, breaks from what other repos are doing, it's probably what just feels best for us.
And we can always revert if it's not something we want.
**Kayla Reopelle** 25:20 So true, yeah.
Yeah, I think we just added Renovate because we wanted a way to automate the semantic conventions pull requests, so that that way we could leverage our rig task, and it would just automatically open a PR for us whenever we had a new Whenever a new Semantic Conventions version was released.
And we have that now, and that's… that's nice.
But I think there was a lot of other… it kind of triggered a cascade of other contributions that, I'm not sure if I quite like… Okay, cool.
Any other thoughts, though, on Renovate? I know, Matt, you said you had some… Points you wanted to chat about with it, too.
**Matt Wear** 26:12 Well, I was just checking what our policy was generally, because I was trying to just go through and see if… I could get the Renovate, PRs green, and just merge them, and get them out of the… Out of the queue, just because they, they seem like, Easy wins, and just… the n… A little more clear what, what actually needs attention, but… But yes, some of them seem to… seemed to stay red, and I was… it's like…
**Kayla Reopelle** 26:47 Hmm.
**Matt Wear** 26:49 And part of me… and some of them, I think maybe they need to be, they need to be rebased, and I saw there was a check mark to rebase, and I think I clicked that, and I didn't really notice it doing anything.
There used to be the button to merge in main.
**Kayla Reopelle** 27:05 Yeah.
I think that… that is a thing that's been on… The button to merge into main… is something that I think we can add back now. I can take that as a to-do this week.
there was a change made by the OpenTelemetry admin repo that kind of caused us to lose that functionality, but, There's since been a pattern to figure out how to get it back, so… There've been a couple of times where I've been interested in it.
As well, so I can get that back.
Well.
**Matt Wear** 27:44 I feel like I've seen it on the other repos, so they must have added it back themselves.
**Kayla Reopelle** 27:50 Yes.
Yeah, that's how we got it back on Contrib.
Yeah, I noticed that the rebase can sometimes take a really long time. I… Don't think I've ever seen it not work entirely.
But I think sometimes it's been an hour. I just… I don't really know how Renovate works behind the scenes on that.
**Matt Wear** 28:13 Got it.
It's not.
It's not as easy as a button.
**Kayla Reopelle** 28:19 Yeah, it's like I add it to the queue kind of a thing.
Which I guess is another question, too, since I'm looking at merging… the Merge Main button.
contrib has been using merge queues for a while. It seems like they're working pretty well.
Is that a feature?
Folks are interested in for the core repo, too.
Okay, I'm seeing some mutes. I'm not sure.
**Hannah Ramadan** 29:09 I mean, I'm not really out there merging queue stuff, so, I think if that's something that's working for people who are, then yeah.
**Kayla Reopelle** 29:19 Matt, have you used the merge queue on other repos?
**Matt Wear** 29:26 I'm fine with if you want to add it, because that will, that should help with… Not having to merge, bane in on, on every, And every PR, as you're merging them, is that the.
**Kayla Reopelle** 29:43 benefit that.
**Matt Wear** 29:44 you'll get.
**Kayla Reopelle** 29:46 Yeah, and then I think it will rerun the tests after it merges into main, and if the tests fail, then I think it… puts it.
Back as, like, a… Approved but unmerged PR.
But maybe that's only for required workflows?
I know sometimes it kicks it… itself back out.
**Matt Wear** 30:15 Yeah, I'm fine with adding it, and I haven't personally used it before, from the merging side, but… Boom.
I'm sure I'll figure it out, and I'll ask questions if… if I'm confused.
**Kayla Reopelle** 30:33 Okay.
Sounds good.
Cool. Any other, like… CI, or… Working… Kinds of questions to chat about today?
**Xuan Cao** 31:05 Oh, I'll have one, but I'll keep it very short. So I have a, I have a PR for the, like, In, Ruby country.
it's for the, OpenAI,
**Kayla Reopelle** 31:23 Oh, goodness. Yeah.
**Xuan Cao** 31:25 So… so this one, I'm not very eager to move… to ask people to remove it, or move it, The reason I wanted to bring out those, I know, I really wanted to… I agree with most about the library to… to have this, to have this open entry plugin, so we don't need to maintain them or update them every.
**Kayla Reopelle** 31:50 Wait.
**Xuan Cao** 31:51 There's a sense that, not every other major languages have this LLM implementations. They… they're… it's very useful to… To track the token usage.
**Kayla Reopelle** 32:09 to the…
**Xuan Cao** 32:10 the message. I know Ruby is not the popular language for running your, and stuff like that.
I'm just trying to get some ideas to, how people think about, instrumentations.
If you look at this, I think some people, mentioned this PR If you look very down… Oil.
**Kayla Reopelle** 32:42 Oh, I guess I have a pending review. I didn't realize.
**Xuan Cao** 32:44 Oh, sorry, I needed a…
**Kayla Reopelle** 32:46 Oh, but this one.
**Xuan Cao** 32:47 This guy, so… So, Ruby RM is, like, Yeah, this one. This is exactly the thing, people, if people want to contribute from their own organization, which is totally fine. Reduces the burden.
And now they wanted to move, move to the, country. I'm afraid that I make a wrong example to people.
A cookie.
**Kayla Reopelle** 33:18 Give…
**Xuan Cao** 33:18 If it's professional, we want to maintain. No, no, no, we don't want to maintain it.
**Kayla Reopelle** 33:22 Yay.
**Xuan Cao** 33:23 Now, just a quick idea how people think about this, .
**Kayla Reopelle** 33:28 Okay.
**Xuan Cao** 33:29 Yeah. Given that all other languages have this… at least have these implementations, and that they use it very extensively.
And given that Ruby is not the popular language for there, and… If we kind of… And it is a big topic.
So, you know, that's my, my, question.
**Kayla Reopelle** 34:02 Yeah, that's a good, it's a good question.
So were you saying that the other languages, their open AI instrumentation.
is native and not in Contrib, or… Are theirs also in their contribute repos?
**Xuan Cao** 34:28 In their country repo, at least for the Python. Okay. As, as most of the… institution for the… Including, the launch chain.
I'm not sure about the Node.js.
**Kayla Reopelle** 34:48 Okay.
Yeah, I… I don't know. I think, I could comment on the… the Ruby LLM, repo, because I think… I would be hesitant to… have us… I mean, or we can wait until they actually open the PR, I guess is the other… Option, and then have the conversation there.
I do think AI instrumentation is really interesting for… Figuring out patterns to support, because it involves… Like, events, logs, as well as traces.
And I would like to… Just see us move towards being more confident about having multiple signals inside of our instrumentation, and… The mechanisms for, kind of, turning those on and off.
But it is nice to not have so many things to need to maintain and kind of… Being aware of and confident in how they work.
I haven't looked at the official OpenAI gem much. The… I've added instrumentation in the past to the Ruby OpenAI kind of third-party gem.
But, yeah, and I know that token counts can be really valuable.
And I think more people… even though Ruby isn't the premier language for AI, I think more people are using Ruby for AI than… I think… But, Yeah, I think I'd have to read through the comments more before I feel like I'd have a full opinion.
And admittedly, I don't remember when I started to talk with you, but it might have been before those comments happened, so… I, I'll try to finish it as well for… Other reasons, so that that way, You know, that loop is at least closed.
**Xuan Cao** 37:11 Yeah, thanks. And also, we already have this, ancho intro, topic, Jim. Even though it doesn't do instrumentation, it does some kind of publications.
**Kayla Reopelle** 37:25 Oh, yay.
**Xuan Cao** 37:26 It's just… I don't know, the reason for that, Jim, but… I think… I think it's very, very interesting to have this kind of…
**Kayla Reopelle** 37:36 Yeah, what I remember about this one is that it was kind of a Shopify… Combo, because they were interested in having their context propagated through their anthropic calls, but it's not a full-fledged instrumentation.
That's what I remember about when it was created.
But I imagine… Eventually, it would be good to actually have all of the… Like, traces and… events and things like that that the Semitic conventions expect.
**Xuan Cao** 38:23 Yeah, and also, if people are still using Rails.
And then they want to have, like, some chatbots.
Aye.
That they, they, they, they have to use… they have to use this kind of, And then if you want to do institution, then you have to use this kind of a… Instant fishing, so…
**Kayla Reopelle** 38:49 Yup.
Yeah.
Hmm.
Okay, well, I guess, are there any… outside of me finishing my pull request and reading things through, are there any to-dos that we want to take on this topic?
Okay, cool.
Well, I think that's it, unless anyone wants to bring anything else up today.
Awesome. Alright, thanks everyone for your engagement.
It's great to have you all here, and have a great week. If you need anything, you can chat on Slack, and… Or on GitHub, so… I'll see you all next week.
**Matt Wear** 40:08 Cool.
**Hannah Ramadan** 40:09 Thank you.
**Xuan Cao** 40:09 Thank you.
**Kayla Reopelle** 40:11 I…
