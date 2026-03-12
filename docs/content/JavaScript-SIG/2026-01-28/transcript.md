SIG: JavaScript SIG
Date: 2026-01-28
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Andrei Borza (Sentry) 00:00:47 Hello?
Raphaël Thériault 00:00:49 Hello.
Trent Mick 00:01:21 June…
Marc Pichler (Dynatrace) 00:01:52 Alright, let's wait a little bit longer to see if, The paper also drying, and we can get started.
Alright.
It's 2 minutes past the hour, I guess we can get started.
For now, the first one is Trent about the SEMCOMF roadmap.
Trent Mick 00:02:42 Yep, just an FYI.
Marc Pichler (Dynatrace) 00:02:43 for people.
Trent Mick 00:02:44 I saw they'd posted that in a number of channels, if you have.
strong opinions?
About what you should get focused on for SEMCOMs this year. Now's the time.
Marc Pichler (Dynatrace) 00:02:56 Nice. Thanks for bringing that up.
Right.
Any… questions or comments, or anything that you think we as a Sikh should drive there, In that space.
If not, then… I guess we could move on to the next one, which is my topic, mostly a question about what you think, we should do in the OTRP exporters, and… Also, in the, signers processes.
Last week we had this issue, that we went… Through during the triage session, Essentially, what happened was there was this change here.
Which ensures that, there's a retry on network errors. So, for example, if you're trying to export a collector, and that one's not available yet because it's still starting, then it… the exporter will essentially retry, and we didn't do that before.
That has the effect now that, with auto-instrumentation. So, for example, if you're trying to shut down the app, it will block the termination by about 5 seconds.
Because it's trying to, like, still export, then figures out it can't do that, because it runs into the retry limit, and then it exits.
So… First, my first impression about this was that that's a bug, and we should… see to fix this somehow.
But I then did check the behavior for Java.
And in Java, it, like, the behavior is the same, essentially. Takes about 10 seconds to shut down.
And that's mostly the exporter retry.
I did, however, create a draft PR that is here.
that… cancels retries on shutdown, to get more or less the old shutdown behavior back, and that's fairly complex, because it needs changes, in the exporters and all the processes, To make it happen, because we don't… want to await the export anymore. We want to, like, start the export, and then essentially, core force flush on that exporter.
So, as you can see, the change is fairly big.
so, that leaves us, kind of, with two options.
the first one is we could close this as one fix and keep the status quo, because… That's likely also how it is in other language implementations.
Or we could go ahead and, try to make the PR that I, put in draft here happen.
It does come with some… Changes in the processes, though, that could affect other exporters, which may or may not be what we want.
So I'm just trying to figure out what your opinion on this is.
If you have any.
Trent Mick 00:06:48 I think, hell yes, make it faster.
A 10-second delay at the end of shutdown sucks. I think we'll always bring up questions.
And probably wasn't at all the intent of the retry stuff.
Did you… sorry, I… I mean… Just seeing us now, and trying to read and listen at the same time.
You had that thing saying, no, this is based on my interpretation of two parts of the spec. Are there things that you think this change goes against?
Wording in the spec, or do you think it's kind of… Up in the air.
Marc Pichler (Dynatrace) 00:07:23 I think… I think I'm interpreting a lot, So, I'm looking at the text there, and it's, Like, this one is for the exporter, and here it says that force flush, should become… Like… The export of any, Readable log records in this example, it has received prior to the call to force flush, should be completed as soon as possible.
preferably before returning from this method. And then… In the OTLP spec, it says to do the retries, but it doesn't specify what to do on force flush.
So, since it's unspecified, I feel like we could do whatever we want there, and the… Requirement level for the retries is a should.
so… I guess forced flush is a good reason to… Not adhere to that.
So we would… Since it's not a must, we can… Have some flexibility there.
And then there's also the processor spec, which… is a bit more clear in that sense. Because it says here, Should try to call the export as export with all the log records.
And then invoke force flush on it. Doesn't say we need to await it or anything like that, which is essentially what my PR is doing.
It does co- Export, and then doesn't await the export, but immediately invokes for a flush.
And in case there are more patches, it invokes export and false flush.
Multiple times.
Because that was just the easiest way to do it.
Trent Mick 00:09:28 Right. Okay.
I mean, I'm for trying to do it. I guess then the next question is the complexity.
And whether that's worth it, but…
Marc Pichler (Dynatrace) 00:09:39 Yeah.
Trent Mick 00:09:39 I mean, you have it working already, though, right?
Marc Pichler (Dynatrace) 00:09:42 Yeah, it's already working, and I… Needed to make some changes to the tests to actually get it there.
Because the tests are mostly… Let's see here… Where'd be…
Trent Mick 00:09:56 tests relying on the export being done when force flush returns, or something, or…
Marc Pichler (Dynatrace) 00:10:02 Yeah, so the tests were mostly relying on timing. They relied on, like, once on the mid-discord or on end in the span processor, that the… Export would be scheduled immediately.
so… The export would be scheduled immediately on Emit synchronously, and then would reserve asynchronously in the background.
And with my changes here, the way that I did it is kind of required to await the resource before that.
And then do the export.
And because of that extra weight.
It takes a bit longer for… It takes one.
Trent Mick 00:10:55 Heck, yeah. Got it.
Marc Pichler (Dynatrace) 00:10:56 One more await, and then… Yeah, the whole test needs to be changed, but it still does the same thing, essentially, it just… Uses this tick async to break the event loop.
Trent Mick 00:11:07 Okay.
Marc Pichler (Dynatrace) 00:11:10 Yeah, that's the… the gist of it here. And the actual change to the batch processes is also fairly large, because then I need to keep track of the Export operations, and there's some… Some caveats there, where sometimes we want to wait that the export is completely completed, and sometimes we just want to wait that it's scheduled for export.
Since we need to await the resource.
Which wasn't done in… I think a forced flush scenario?
That's now already fixed. I think that was also a bug there.
But yeah.
Trent Mick 00:12:00 And then the same thing for the other batch.
Marc Pichler (Dynatrace) 00:12:03 Yeah, exactly. The implementations, just vary on the names.
It's actually all the same code. I copied a bunch of stuff back and forth. I still need to go through the comments to make sure I haven't copied the log exporter into… The batch spend processor.
The commons, at least, but… Essentially, it works the same there. It just has this huge extra… Ping to make sure that, We can figure out once the export has actually been scattered, and then, basically we get to force flush right after it.
if I had to redo it, like, the whole export pipeline, I would have, export force flush or something like that, because that would simplify stuff a little bit more.
Or have something where I can pass log records to the force flush method to say force flush these.
Because once that's happening, we already know that that's what we want to do, and there might be one export in progress, but we just force flush it without any blog records.
That'll simplify stuff a bit, but yeah.
Trent Mick 00:13:20 Okay.
Marc Pichler (Dynatrace) 00:13:24 So, I guess if there's… If nobody is against, doing this cancel-retry thing.
I would break the PR up into multiple PRs.
Because the changes are fairly self-contained.
I can… Do the, changes for each SDK in separate PRs.
And then we do the exporter change, and we should be all good.
Trent Mick 00:13:57 That can be.
Sounds good to me. Yeah. I mean, it's not crazy high priority, but yeah.
Marc Pichler (Dynatrace) 00:14:03 Yeah, I already, split that up into multiple commits, so I would just take them one by one, and open PRs for that, so it should be fairly simple.
Alright.
Any questions or comments about this?
If there aren't any, then I guess we can move on to the next topic.
Which is, Carlos, who is offline today.
On the other resource attribute PR… This is the environment variable parsing stuff that we talked about a few times already.
Please discuss if you have an opinion On this thing here.
It looks like, essentially, this changes that… we should fail fast, which means discarding the entire empire value in case of an error, as opposed to what we do now, which is, Go through half of it, and once we encounter the error, just drop the rest that's in.
DMFAR.
And then there's also another thing that says, anything outside the baggage octet.
Should be percent encoded rather than must, so the diff looks like this here.
Trent Mick 00:15:56 It looks like Carlo's table from the issue that was linked to the spec change.
JS was the only language checking for unencoded shares.
Everything else was, I guess, just letting stuff go through.
Okay, cool.
Marc Pichler (Dynatrace) 00:16:22 I guess… don't have an exact opinion on it. Dropping everything, Might be a bit problematic if we want to do it soon, but we can do it with 3.0 if necessary.
Trent Mick 00:16:40 Is that a breaking change?
I mean…
Marc Pichler (Dynatrace) 00:16:45 It's closer to breaking… I suppose. Yeah.
Trent Mick 00:16:49 everything's supported.
Marc Pichler (Dynatrace) 00:16:50 Depends on you.
Trent Mick 00:16:51 shaking.
Marc Pichler (Dynatrace) 00:16:52 Yeah.
Not having the resources there suddenly might be, Something that people would see and, be confused about, though then there's also a question of, like, how often does that actually happen in the wild?
I would assume that if you put a resource in the environment variable, you would also rely on it somewhere.
Trent Mick 00:17:17 So that must changing to a should, I think, means that the JS implementation can not bother being strict about Failing if a double quote, or a semicolon, or… What was the other one? Or used, and if that's the case, then… I can't even think of an example where… There's a failure.
I guess if you have a key value that doesn't have an equal in it, sign in it, then maybe that's a failure and the whole thing blows up.
So I guess that would be maybe a surprise. If someone had foo equals bar, comma, Spam.
that now breaks and it didn't before, I'm not sure. So, I guess we'll see what the JS implementation is, but certainly the spec is a lot more relaxed here, so… Yeah.
Marc Pichler (Dynatrace) 00:18:13 Yeah, I guess I misunderstood then on the initial read here.
But yeah, as long as… Whatever the output is, is… usually… and less strict than what we do, I think it shouldn't be a breaking change, then.
Because we just get more data, so it should be fine.
Trent Mick 00:18:36 Yep.
And we can sort that out on the JS.
implementation, I assume… Carlos or Jack will follow up on after the spec's updated.
Marc Pichler (Dynatrace) 00:18:50 Sounds good.
Alright, any additional… Questions, comments, concerns about this?
If not, then we can move on to Marilla's topic, which is… A bug that was reported.
Marylia Gutierrez 00:19:13 Yeah, it just is a quick thing that… we have the service instance ID that it can be passed through the hotel resources, but we also have a detector for that one. It's just, like, if you don't have anything, just put it at random. But apparently that was the case when you said both things, it was giving the priority to the random one, instead of the custom one from the… hotel resources. So this one is just, yeah, adding a bunch of tests.
To catch this case, but the fix itself is just… Yeah, check if the… we have already on the resource attributes, and use that one. Otherwise, use the random.
Raphaël Thériault 00:19:54 Mmm…
Marylia Gutierrez 00:19:55 Kind of just, like, looking at this, wouldn't a better fix be to reorder them in the SDK?
Raphaël Thériault 00:20:01 Or, like, wherever they're declared so that the priority is in the proper order.
Marylia Gutierrez 00:20:09 So, I was looking at both solutions, and I try to basically say… If this one is kind of, like, detecting, maybe we want to contain the detection in one place, which is, like, or the detector that is just a random, or detecting if that is set on an environment variable.
So this way, you don't have to think about Oh, I do the detector, get a random, but I also need to check the environments and do it there, so I decided just to put everything in one place.
Trent Mick 00:20:50 Yeah, I'm not sure.
Marylia Gutierrez 00:20:52 I can go with it, because the similar case is, like, the service name that we do this, then we do then on the package SDK nodes, and then when we do another check, like, we set up the values, and then we check if there is a config for service name, and then we set that again.
That could be the other way to do it.
Trent Mick 00:21:14 Are there… are there other examples? Like, service.name's obviously a weird one, because it also has things.
Marylia Gutierrez 00:21:18 Yeah.
Trent Mick 00:21:18 what config option, are there not other ones? No.
I don't know the answer to this question. So when there's the OTIL resource detectors environment variable, where you can give a comma-separated list of which resource detectors to use.
Does the order given there get… used? Or should we then consider having, if envis specified, should we put that always at the end, because it's the one that should win?
Marylia Gutierrez 00:21:50 Oh, but the envy's not looking at service in Society, I think.
Is it? Oh, let me see.
Trent Mick 00:21:57 The ENV one is, I think, the one that picks up hotel resource attributes, isn't it? Yeah. It might not be. Yeah, it is. Is it? Okay.
Raphaël Thériault 00:22:05 Yeah, and then, like, if we do decide to put it in the service instance ID detector, there's probably, like, the person decoding stuff that should also be present here.
Trent Mick 00:22:18 Ari, I'm not sure what you're saying.
Raphaël Thériault 00:22:20 Oh, I'm saying, like, if we do decide to like, have specific logic in here to detect the service instance ID key value in the… ultra resource attributes, environment variable. It didn't need to also do the person decoding and all of that stuff.
Trent Mick 00:22:37 Yeah, it would.
Nice.
Which, I guess is an argument for putting it… leaving it in the end of the detector, maybe, and then making the… Yeah.
It's an argument for what you're saying, is the potential alternative solution is to just ensure ordering Of the N1 being last. If we do that, though, then we also have to discuss how we order them, if… The resource detectors being used are coming from the hotel resource.
Detectors, environment variable.
Marylia Gutierrez 00:23:13 I'm doing the test right now, I'm just changing the order and see what happens.
And removing my changes, just to see.
Trent Mick 00:23:32 Was it your test here that had the ordering of things, or was it an existing SDK?
I guess we have a default order in the SDK, right?
Marylia Gutierrez 00:23:42 Yeah, so the ordering I'm changing on the file… So is on the package OpenTelemetry Resources the same thing? Is the… I already lost it.
No, never mind. It's on the OpenTelemeter SDK node.
There is, utils file, that is the getResourceDetectors from environment, and that one has the list of all the things, so I'm just… SDK node… Source?
Trent Mick 00:24:17 I just sent the link, if you want.
Marylia Gutierrez 00:24:26 Yeah, that one. So now I'm changing the line 79 to be, I guess, the last one.
Trent Mick 00:24:32 Move that down to the last, yeah. Yeah.
Marc Pichler (Dynatrace) 00:24:55 default here.
So if it's unset, it will also use the nth detector first.
But the order in which they are applied is.
Marylia Gutierrez 00:25:32 Yeah, just changing the order didn't fix the issue.
At least on that file.
Marc Pichler (Dynatrace) 00:25:42 Might be this, detect resources thing that also has kind of an impact in… How things are merged together.
Marylia Gutierrez 00:25:51 Yeah.
Marc Pichler (Dynatrace) 00:25:54 I found that the way that we, like, the ordering that we apply on the detectors, and also… the way that we apply code-provided resources can be a bit wonky. I think it doesn't follow exactly the rule that we follow in the rest of the SDK, where if you provide something in code, it overrides whatever happened in the environment variables.
so… I'm wondering if this would be a good… Time to also change this.
Have it RP inline.
Like, the default settings, and the way that things are merged together, and the way that things are merged together with the code provided.
resource.
Things are… Oh, didn't I actually realize that this detect resources thing was in… resource package.
If that one is the problem, then, We can't change this easily, because we're… Change the output for everybody who's using that.
I will, also have a look at that PR here.
to see if there's anything that we could do. Ideally, if, like, reordering stuff works, That would be great.
Because then, It also wouldn't change any… change for anybody who's relying on that behavior if they're just, you know.
Taking the resource detectors and… Thank you.
Actually putting them in that order on purpose.
Though it's also a question of, like, how many people are those?
Didn't run into that.
Marylia Gutierrez 00:28:11 Yeah, because, yeah, changing just the art on that file cannot fix the issue.
Marc Pichler (Dynatrace) 00:28:25 Oh, that was in… In the thing that was linked now in the chat, right?
Marylia Gutierrez 00:28:34 Yes.
Marc Pichler (Dynatrace) 00:28:50 Yeah, I guess I couldn't… Take some time to look into this in more detail.
Trent Mick 00:28:58 We discussed this before. It rings a bell.
Marc Pichler (Dynatrace) 00:29:01 It does, yeah. I'm getting major deja vu.
Trent Mick 00:29:09 Yeah.
Marc Pichler (Dynatrace) 00:29:19 world. There's… No more questions. I guess, let's just have a look into that async.
And see if there's another way to do it.
Marylia Gutierrez 00:29:37 Okay.
Marc Pichler (Dynatrace) 00:29:40 Right?
I guess we could move on to bug triage, or if you… if anybody has any topics, please feel free to just, write them down here, and then we can go back to that.
As is tradition.
Alright.
backtriage, GraphQL… Some problem with custom reservers.
I seem to remember that, apollo… Was either not instrumented or something like that, and that's why, didn't show up.
Or did something with the, Default reserve things that cause trouble for users.
They actually do have a reproducer repo, which is nice.
Looks like there's something in between.
That's missing here.
In case this looks like P2.
Because telemetry is not there, that's supposed to be there.
I don't have any initial idea of what could be wrong here.
Hadn't looked into the GraphQL instrumentation in a while.
Let's leave this here for now. Might also ping the component owner for it, but I guess he is not responsive.
What do you mean?
Alright.
Let's move on to the next one.
So we're back in package propagation.
Oh, this is using… through Indigen ExpressHTTP.
Oh.
That's an interesting… Set up here… Next handlers are executed without package.
And we have some, situation where we also lost context there.
Because if that's not here, then ours, so… It takes chunky here.
I'm also not sure, if propagation getActivePaggage is a thing. I haven't looked into that one for a while.
Trent Mick 00:34:50 It is.
Marc Pichler (Dynatrace) 00:34:51 Indeed, yeah.
Thus, get baggage on the context API.
Baggage gets… baggage key from… Add here… I don't know what we mean.
Yeah, I'm having trouble figuring out if that's an instrumentation problem, or if it's a bug somewhere else. I guess let's just check in the instrumentation first, and we can… move this as necessary to the core repo if needed. This would be… RCP2, maybe.
Not exactly sure what the… Impact would be if a package wasn't here.
Yeah.
Let's leave this like that for now, and then we can move on to the next one, which is, instrumentation.
H. Mitoperpoolers cause… DP client connection count be recorded incorrectly.
One of our services has two connection pools.
But one of them goes negative, which is probably not… red value for it. If I recall correctly, the way that we need to handle, the up-down counters in… in database instrumentations can be a bit finicky, so I wonder if just… If the usage is just added or subtracted from the wrong one.
And that's why it ends up in a negative value in the end.
Trent Mick 00:37:42 Yeah.
I don't know.
Little name is being used to know. So, which counter is this? Connection count.
Marc Pichler (Dynatrace) 00:38:01 Oops.
Trent Mick 00:38:03 In slow.
Oops.
go there… The pool name is being passed through.
Marc Pichler (Dynatrace) 00:38:47 Oh, update counter does… this here… The poor name.
Trent Mick 00:38:57 Actions.
Marc Pichler (Dynatrace) 00:39:05 So I guess it could be that, But they are actually… Named differently.
So as long as the pool name is okay, then… Should also be fine.
Unless the way that we, Attach the extra data onto the pool here.
is incorrect, somehow.
Go to usage update counter… Market, our name might be incorrect. I guess we won't figure out exactly what's going on here, but… If the data is wrong, then it… It's likely because something wrong is written into it.
And maybe the pools just pollute each other.
I'm not sure if there's a test for using multiple different pools.
Trent Mick 00:40:51 No, I doubt it.
Anyway, that sounds like a good book to follow up on.
Marc Pichler (Dynatrace) 00:40:59 Yes.
Alright.
And these two I was meaning to look into, but I haven't had the time yet.
So I was working on the other… Dark with the shutdown stuff.
Looks like this one still needs author response, and the other one… Still no, additional info, but we also didn't ask for it, or write this, I'll add this to my notes again.
I'll try to follow up on this. I need to take some time at some point to actually get a proper Lambda testing setup ready, so that I can play around with it. I don't have anything here.
Alright… So this was Contrip.
Looks like no new topics… In the meantime, so let's go ahead to… to… our triage.
It's go to… Core repo first, because…
Marylia Gutierrez 00:42:35 Just an update is the test that I was doing that I was like, oh, it's too filling when I changed the order. My test, I had created an order, like, putting environment first answer, so it was not really testing the actual case, so I just… fix the test, and just changed the order, and that fixed the problem, so I updated the PR.
Trent Mick 00:42:55 So, last one wins, is that right?
Marylia Gutierrez 00:42:56 Yeah.
Trent Mick 00:42:58 Okay.
Marylia Gutierrez 00:42:59 So I did… when… when you don't set the order, you just leave, like, use auto-intermentation or whatever, so I'm putting the environment variable always last. If somebody passes the order, it's whatever order they put, so it's not something that I can control.
Trent Mick 00:43:16 So I guess… Yeah, two options on the environment variable for specifying resource detectors. One is we explicitly always put NVLAST, so we reorder what they give us.
Which is maybe… Not a great idea, or we at least had a comment in the README for the docs on that thing, saying order matters here for a couple cases, and give the specific case, because I think it's useful to have a specific.
Marylia Gutierrez 00:43:40 Yeah, gonna update them to read me here, but yeah.
Trent Mick 00:43:42 Yeah, I think our README examples are showing end views first, we should change the examples to put end last, because we probably want it last, yeah.
Oh, sorry, on that, another side thing, I wonder if at some point we'll want, like, this is not exactly related, but… so our resource detector for Service Instance ID is a, quote, experimental one called Service Instance.
Marylia Gutierrez 00:44:05 But…
Trent Mick 00:44:06 Declarative config has, at least the kitchen sink examples, have an example of… and this is under… here, let me… Share the links so you can put it up.
Can you bring that?
Okay.
Marc Pichler (Dynatrace) 00:44:23 Yeah, one second.
Kitchen sink, there we go.
Trent Mick 00:44:28 Okay, line 39, and this is under detection development, so this is all, like, early days central config. But they have some proposed, kind of, I guess, well-known names for detectors.
Which I wonder if at some point we'll want to change to change. So… I don't know if anything's implied here. Does this imply that the service detector would also handle service instance ID? Because it would handle service.star?
post and process already happen to match the names that we're using in our environment variable. The other ones don't, so… Anyway, something to think about.
Download. We can move on. That's all I want to say.
Marylia Gutierrez 00:45:06 Thanks.
Marc Pichler (Dynatrace) 00:45:11 Alright, thanks for looking into it again. I think the reorder, stuff… is… A good way to go about it.
And…
Marylia Gutierrez 00:45:24 Yeah, I'm just gonna update the read me now, and you should be good to go then.
Marc Pichler (Dynatrace) 00:45:28 Possibly.
Trent Mick 00:45:28 You're gonna take out the handling of the environment variable directly in the service instance ID detector, right?
Marylia Gutierrez 00:45:34 Yeah, I already did it, the PR is…
Trent Mick 00:45:36 Oh, I see.
Marylia Gutierrez 00:45:37 already updated, so yeah. The only thing that PR is doing is adding the task for this case that didn't exist, and then changing the order. That's the only thing. Now, the readme that I'm gonna do.
Trent Mick 00:45:47 Cool.
Marc Pichler (Dynatrace) 00:45:50 Thank you.
Right.
Let's skip over this one, and this one will be, actionable once we… Get everything in the… SDK and API logs GA, milestone ready.
I did update the, focus topics issue with that, and I guess declarative config we can still add, don't have a text for that yet.
Alright, then this one here, this I initially had opened to, serve a bunch of issues which come from the use of, Protopuff.js.
I will actually go ahead and open a PR to do the custom protopuff serialization. I've been… Chipping away on that, in the background.
appropriate, I just need to, make it… I will break it apart into serializing and deserializing for logs first, and then… We'll open a few PRs.
Tool.
make that happen. I'll close this one.
Because it would be obsolete once I, Once I open the other PR.
Then… We have the entity prototype, which… Does not have anything, actionable right now.
the advisory attributes… This is for the metrics API, and they were running… so, essentially, what the advisory attributes parameter is, is that, It just gives you a… Allow list.
But… you can define when you create an instrument, so… Essentially, what this does is you say, I want to have these attributes only on here, and then only these are kept and the rest is discarded.
But the tests here are failing, because the precedence is not… Right, it seems.
It's been a while since these tests have run.
But… We need to make sure that the order in which things are applied is correct.
I… Put another comment here, pinging the person.
And see if they come back.
here, and… If they still want to work on it.
Doesn't know.
Trent Mick 00:49:30 Environmental part of the metrics spec?
Marc Pichler (Dynatrace) 00:49:34 it was experimental at the time that they opened the PR, yes. I'm not sure what the current state of it is?
Trent Mick 00:49:42 That's fine, yeah.
Marc Pichler (Dynatrace) 00:49:44 I guess we could just check real quick.
Should be fairly easy to find.
Advisory parameters, attributes.
Yeah, it's still in development.
Though I wonder if… For TypeScript, at least, we should have something… like this already.
if I recall correctly, the metrics API, it… Gives users a way to, Create an instrument with a type.
And then only the attributes from the type were actually be applied. So you can define a type, and then type checking will check if you pass the correct data to it.
it's not all the way there. It's, like, I don't know, 60%.
the way, but let's just see if the person still wants to continue work on it or not.
Right.
And here we have, exporting the Shima functions with… Stay label on it.
From… last week.
I guess stillbot will get to this one, if… There's no change. I'm not, against exporting these, but I just think that we should.
not provide many different ways of doing this, so I think we should deprecate the… We should deprecate the protected wrap and unwrap on the instrumentation-based class.
And eventually remove it, so that people can use, the wrap and unwrap directly.
I also think we shouldn't.
probably have the shimmer name and just export wrap, unwrap, mass rep, and mass unwrap from instrumentation directly as utilities.
Trent Mick 00:52:31 And I want to drop unwrapped completely.
Marc Pichler (Dynatrace) 00:52:34 Yes.
Trent Mick 00:52:35 Bye.
Marc Pichler (Dynatrace) 00:52:35 That's a bigger discussion. That was part of the thing I was…
Trent Mick 00:52:39 When we were chatting earlier, I was talking about new instrumentation thing is.
Having this concept of instrumentations have a setup, if you selected them, and then enable-disabled, but enable, disable has nothing to do with unwrapping, because that's a pipe dream.
Marc Pichler (Dynatrace) 00:52:52 Yeah, unwrapping… it doesn't even work right now if you use import in the middle, I think.
or at least…
Trent Mick 00:53:01 Oh, does it not? Because something something proxies is in there, I haven't looked at that. I was hoping we could drop all that support, but probably still need it.
Marc Pichler (Dynatrace) 00:53:10 Yeah, I think with input in the middle, you can stack stuff on top of each other, and then the thing that you're trying to unwrap is not… might not be the thing anymore that you wrapped before.
Trent Mick 00:53:24 Yep. I seem to remember something like that.
Marc Pichler (Dynatrace) 00:53:27 -Oh.
Trent Mick 00:53:28 Well, that can happen without the import in the middle, too, with the require in the middle, too. If someone else is using a different shimmer that uses a different… key to identify whether it's been wrapped, so, like, I… I don't know this, but a strong guess is that Datadogs version of Shimmer probably uses a Datadog-specific symbol on the thing to say, yeah, we're wrapped and unwrapped. So if you have two agents, I've seen this not often, but occasionally in support requests at work, that people happen to have two agents enabled.
At the same time, which, like, hilarity ensues, but unwrapped just won't work in that case.
So yeah, anyways.
Good times.
Marc Pichler (Dynatrace) 00:54:18 So…
Trent Mick 00:54:23 That's no way.
Marc Pichler (Dynatrace) 00:54:23 one.
Trent Mick 00:54:24 What we want to do.
Marc Pichler (Dynatrace) 00:54:26 Yeah, so for this one here.
I guess we could start working somewhat towards that future, and just deprecate the ones That we know we want to export from the top level.
Trent Mick 00:54:39 So if we export… do we export the ones that have the proxy support in them? The ones that are only on the node?
implement… instrumentation base.
Because those are the ones that were added. So when import in the middle support was added.
custom implementations of wrap, unwrap, mass wrap, mass unwrap were done that… Oh.
Supported checking if the thing being wrapped was a proxy and doing something different.
I don't really know more details than that.
And that was… because it was imported in the middle, it was added to the node-specific implementation. So if you go into source platform node.
Instrumentation.ts.
Go look for underwrap or something. Yeah, right there. It's line 74.
This is extending what Wrap does with the proxy stuff, so if we were to export something… which one are we talking about?
So I'm not sure what the answer would be.
Marc Pichler (Dynatrace) 00:55:51 Yeah, that's a good question.
Trent Mick 00:55:53 Also, that wrap automatically does unwrapping, bugs me, but whatever. Maybe that's what the shimmer… wrap stuff does, or maybe that was kind of unnecessary because of the added proxy support, I don't know.
you know, as I said, I went into new graphing, so… Or unwrapping, so I'm not sure what I would want to export here.
I don't know.
Marc Pichler (Dynatrace) 00:56:20 Yeah, I guess if we were to deprecate these here, We would have to have some sort of… These two.
I guess now I confused myself even more than I was already.
That's interesting, I will look into this a bit more. I don't have a good answer for what to do here.
4, but… if I recall correctly, this Shima implementation that we had, Edit here… I'm not sure if it does an unwrap or a rep.
Already?
Trent Mick 00:57:17 I don't know.
Marc Pichler (Dynatrace) 00:57:30 No, it doesn't. Seems like that's just, It is not unwrapped, so it'll…
Trent Mick 00:57:42 It'll wrap again, I think.
Marc Pichler (Dynatrace) 00:57:51 Which I guess makes sense.
Trent Mick 00:57:56 But that means only the node… only the node ones.
When you call… This.unwrap will… or this.wrap will be doing an unwrap for you, Autumn.
Which… which is usually… wasted work.
Because I think most of the instrumentation implementations will… Unwrap first, but maybe it's not always the case.
Oh, huh, actually, no, that's an init, not an enable. Nevermind.
Instrumentations had it enabled twice as it stands right now, which is… Sometimes causes some surprises.
That's on the node side, but I've seen the bugs on the browser side, that's where the discussions were, like, for example, on the PR for… adding instrumentation console that I think… you looked at recently, teamwork, but… yeah, anyway. Okay. It's exciting times. And David, you're nodding your head. Is that because you noticed that when… for your… Let's change how instrumentations work, PR.
As well, or…
David Luna Bistuer 00:59:04 No, we can talk with… It's a big topic.
Trent Mick 00:59:09 Yep.
it ends up blowing up. So sorry, again, Mark, I'm not helping. I don't have an easy answer for the unwrap, nor the exporting shimmer.
Marc Pichler (Dynatrace) 00:59:24 I guess, We wouldn't have any, trying to find the right word. We're not against, exporting the… Utility functions, right?
Trent Mick 00:59:46 I guess I was gonna come down the other way, and saying, like, one person has asked for it, and…
Marc Pichler (Dynatrace) 00:59:51 Hmm.
Trent Mick 00:59:53 It was just for a type reason.
And… they're not probably desperate for it. I mean, I feel bad just basically ignoring letting things go stale, because I've never looked at this one. But if we're… At all seriously considering Significant enough changes to the instrumentation.
API.
That we would even consider not unwrapping. Why would we go export these things right now?
Also, there's the technical question of whether the… this un… Exported versions would be just the raw shimmer ones, or the ones that have this proxy support that we're using, so… I wouldn't be ready to approve this one right now.
Marc Pichler (Dynatrace) 01:00:40 Yeah, that makes sense.
I will type up a response for this, trying to summarize.
What we talked about now.
And, and let's see where that goes.
Trent Mick 01:01:10 Thanks.
Marc Pichler (Dynatrace) 01:01:11 I'm not sure why I even ended up at… the idea that I want to have this exported, I'm usually Against exporting everything.
Alright.
Trent Mick 01:01:26 We're out of time.
Marc Pichler (Dynatrace) 01:01:30 Alright then, thank you everybody for joining.
Have a great week, and see you next week.
Bye.
