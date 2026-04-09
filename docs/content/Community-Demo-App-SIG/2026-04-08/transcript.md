SIG: Community Demo App SIG
Date: 2026-04-08
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:05 Hello, hello.
**antoninbruneau** 01:10 Hello!
**Pierre Tessier** 01:14 Hey!
Long time.
**Juliano Costa | Datadog** 01:18 Yeah. How you doing?
**Pierre Tessier** 01:21 Mud… Done being between jobs, and, you know… About a month into the new role now.
**Juliano Costa | Datadog** 01:28 Awesome. Yeah, now we need to update the main README with the R…
**Pierre Tessier** 01:33 Yeah…
**Juliano Costa | Datadog** 01:34 company name.
**Pierre Tessier** 01:35 I need to update my… there's a file somewhere, right? I gotta update?
That says, as a different company as well, so that the contribution's contributed right.
I should probably figure that out. I gotta figure out where that file is.
**Juliano Costa | Datadog** 01:51 I may be able to help you on that. Give me a second.
I have a chat with Army.
that… when I joined.
Dadog, I reached out to him, asking about exactly that.
Yep, there you go.
Uranus.
**Pierre Tessier** 02:31 Yep.
**Juliano Costa | Datadog** 02:32 I can also,
**Pierre Tessier** 02:33 Yeah, I, I… I'll write my PR later.
**Juliano Costa | Datadog** 02:39 Cool. So, there are a couple of things that I would love to discuss, and But I think one of them is that we are getting a lot of Things happening on the demo recently.
How do you all feel about moving the meeting back to weekly? Like, we can keep 30 minutes, it's fine, but, like… Because I feel that we are not discussing stuff for 2 weeks, and then we discuss the things, and then, like, two weeks passes, then we are back on discussing.
the thing again, and, like, I just want to get back to normal.
**Pierre Tessier** 03:26 Moving it forward.
I don't have an issue with that, and this time would work fine for me as well.
**Juliano Costa | Datadog** 03:42 Hello, Shanoy.
**Shenoy Pratik Gurudatt** 03:45 Hi. Hi, everyone. I joined late, sorry, I was late for discussion. I didn't get the last thing that you were talking about.
**Juliano Costa | Datadog** 03:52 No, you missed.
I was asking, Everyone, if everyone would be okay in moving the meeting to a weekly cadence.
**Shenoy Pratik Gurudatt** 04:07 Yes I want to do that as well.
**Juliano Costa | Datadog** 04:11 Cool.
Yeah, like, I know that… Last week, we… our last meeting, we were… well, I posted on… on Slack that we would skip, but I saw that the folks from IBM still joined.
And I think they presented something about the… or at least discussed something about the agendic Astronomy shop.
So, I don't… I don't have any insights on that.
**Shenoy Pratik Gurudatt** 04:43 Yeah, I can give you a gist about it. So they're trying to add MCP server… and their agentic UI interface to the demo.
And I think they also have a PR app.
I think Cyril and I went over their contribution.
And then gave some guidance that they had a single agentic Docker Compose, which had UI, MCP, everything all together. We asked them to split it out, just to see if other vendors could try to swap their elements, for example.
Yeah, that was the conversation last time. And they also have a GitHub issue showing the architecture and stuff.
On how they want to integrate this.
But after that, I didn't get time to check back on their PR.
I was planning to do an initial review.
Yeah, that's… that's the status about it.
**Juliano Costa | Datadog** 05:43 Awesome.
Okay.
So, just… just so I have everyone here, Anton in Citiel, would be… would both of you be fine on moving this meeting to weekly instead of bi-weekly?
Cool, okay, so I'll… I'll reach out to… Marilla, so she can, just, Perfect.
Don't tell?
I see that, Gerhard is here in Bohan as well, and I saw that you have added a couple of items in the agenda.
Chennai just gave us a nice overview on the current state. Would you both like to add something, or… it's just pending on our side, reviewing the PR?
**Rohan Arora** 06:51 Yeah, and then, you know, feel free to ask us any questions you guys may have through the PR or whatever have you, right? And we'll be more than happy to chime in, so…
**Juliano Costa | Datadog** 07:01 Awesome. Yeah, I have to be honest with you, I didn't have time, so, yeah, it's, I got back from KubeCon last week, and then last week I got sick, so yay, KubeCon, flew, so… This is the first week that I'm actually back to, to work, so…
**Rohan Arora** 07:25 Yeah.
Yeah, and actually, a couple of weeks back, I was at SRECon, and the… like, the SREs there are now talking about where, you know, I was talking to a senior SRE from a large pharmaceutical company, and they now have… 100-plus agents deployed in their environment, and they are actively thinking about, okay, what's the platform for me to start monitoring and observing these environments and whatever have you, right? So, I think all this effort is shepherding in that direction. Maybe the… Practitioners are not there this year, but they are getting there, and, you know, probably they'll be there by the end of the year. They'll be, like, asking for, hey, you know, has the open telemetry bit been streamlined, right? Or what's the way for them to experience, and whatever have you, so…
**Juliano Costa | Datadog** 08:24 Okay. Yeah, I need to check. I just saw the… I watched the recording from the call where you all presented to CDL. Well, actually, presented in the SIG, and.
**Rohan Arora** 08:38 Yeah.
**Juliano Costa | Datadog** 08:39 I rewatched the recording, but that's everything I know, and I haven't checked the PR yet, so I don't have any… any… Anything to add on that?
**Pierre Tessier** 08:57 So… I have to watch the recording still, but I'm reading the issue here. So this is a lot of things mixed into one. It's really four things in one, right?
this PR?
**Gerard** 09:20 So this PR, largely the initial one, if I recall correctly.
it's real… it's realistically adding about, 3 microservices, I believe, to, Olta Demo. I'm just double-checking to make sure I'm not, Speaking out of turn…
**Pierre Tessier** 09:39 Sorry, when I said four things, I meant the, from the issue.
Oh, okay. Yeah, uses 3 services to accomplish the four things. How is this different?
Or should we replace the recommendation AI?
With this, as well.
**Gerard** 10:05 At least from our perspective, I don't… So, I guess that also depends on how you guys are using the recommendation AI, If it's… From our perspective, this is just the mess… from our perspective, this is just… What we're adding is effectively making the demo microservices look similar to, or rather make them available through MCP calls so that you have this chat, bot with a, with an LLM.
Running to then, try to use the microservices like tools.
Instead, so, I guess, you guys would know Lisa better than me in terms of how your use of the AI in the… I think it's product recommendation.
**Pierre Tessier** 11:00 It's product reviews, I'm sorry, I misspoke there. But yeah, product reviews is.
**Gerard** 11:05 Yeah, so, however you guys are using it, if you feel like this is comparable and you want to… change it between that, that's fine. If you want to keep it all the same, that's also more than fine. I think I'd kick that back to more of what you guys want to do from an architectural, standpoint.
**Rohan Arora** 11:24 Yeah. But Pierre, last time when I'd taken a look at the product reviews, it seemed that it was basically just returning a static JSON, which was already present.
in the system. It wasn't making any LLM calls.
**Pierre Tessier** 11:39 If you pass in an OpenAPI key.
**Rohan Arora** 11:44 Huh.
**Pierre Tessier** 11:45 It will make an… an LLM call to OpenAPI. But by default, it just… I think there's a built-in LLM, which just returns that JSON, I think it was?
**Juliano Costa | Datadog** 11:56 A mock-up. So, yeah, yeah.
**Pierre Tessier** 11:58 Yeah, yeah, so that LLM gets bypassed if you specify an open API key to the product reviews service.
**Juliano Costa | Datadog** 12:08 So we can demonstrate that.
**Pierre Tessier** 12:10 Yeah, what I'm trying to get at here is… is just… I think it's fine, I'm just trying to make sure, like, now we're gonna have two different chat.
Interfaces in the demo.
One in the astronomy shop itself, and another one to kind of orchestrate the astronomy shop.
If that makes sense.
**Rohan Arora** 12:27 Yeah, yeah, and I completely agree, right? If it's doing that LM call, then we should… we should go back on our side and revisit and come back with a POV for the team to hear to consider, right? What… what does it mean to have that consolidated view, and what's the delta?
That we are bringing in here.
**Juliano Costa | Datadog** 12:45 One question that I have is, so… Are we currently using some… like, API call, or are we call… so, like, in this PR, are we adding anything that actually calls, whatever that I need to provide, tokens and pay to run the demo.
Because that's what we did with this mock-up on the… on the…
**Rohan Arora** 13:17 Yeah, so there are two lenses which we are taking to this. So in the first iteration, yes, the expectation is to have the API call, but then the second thing which the team is working on, and we didn't want it to bloat up this PR, was to have what we refer to as an LLM cache, so think about this as, you know, a key-value database which has a certain set of, you know, pre-generated responses and requests stored, and at that point, right, if let's say an LLM is not available, so just like how in the product review example, y'all defer to one JSON being returned, it would just be that it would go and try and do some matching based on those cached responses, and then retrieve from those cached responses.
So, if you believe that, you know, not having, let's say, access to an LLM, that should not be a prerequisite to enable, let's say, this part of the component entry, then we could try… you know, we could build that component in as a part of this PR as well.
**Juliano Costa | Datadog** 14:32 opinions. I know some folks that have the demo up and running for Sometime.
So, having something consuming tokens all the time is, I would say concerning.
**Pierre Tessier** 14:48 Yeah.
We'd have to be able to turn that off.
**Juliano Costa | Datadog** 14:53 Yes.
**Rohan Arora** 14:54 Nope.
**Pierre Tessier** 14:55 It has to be able to turn off, and it, like, almost… Like, I almost want it controllable through a feature flag. Like, it's always checking itself to turn itself back on.
**Rohan Arora** 15:03 If the.
**Pierre Tessier** 15:04 feature flag on, okay, now I'm gonna burn some tokens.
I also feel like we gotta really warn humans about this, because what I don't want is the demo to come up with a… Bill for somebody.
**Rohan Arora** 15:16 Yep, yep, yep, yep.
**Pierre Tessier** 15:20 You know, especially people on corporate accounts who just sling around their corporate auth tokens all over the place and not realizing it, and then something in the background is just chewing away at that.
There's risk there.
**Rohan Arora** 15:33 Yep, yep.
Okay, yeah, making note of that, so… so, and again, right, maybe, but by default, it would be like, hey, we have this L&M cache, and that's the cache it will hit, right? So that's not incurring any tokens or whatever have you, but then, you know, if there's an active token plugged in, then it can defer to… Using those.
**Pierre Tessier** 15:55 And now, for what to work, that's how we have it set up with product reviews as well. Like, if you specify your open API.
**Rohan Arora** 16:04 added.
**Pierre Tessier** 16:04 environment variable to it. It'll start… the load generator, when it does a product review request, which is a couple of them at least, will incur that… that cost.
So, it's a pattern that we've done before, which is, like, default has to be… not cost money. That's it.
**Rohan Arora** 16:22 Yep, yep, yep, yep, yep.
**Cyrille Le Clerc** 16:24 Maybe we can play with the feature flag service to, Help activating and deactivating, the stuff.
**Rohan Arora** 16:36 So that would be the FLACD component, Cyril, or is that when you say…
**Pierre Tessier** 16:40 Yeah, the flag geek component.
We would be able to define our own flag for this, and use whatever open feature makes it available for… for feature flagging here. And then we have a… a fairly simple UI, That allows you to update and change the feature flags.
**Rohan Arora** 17:02 Yeah, triplex, okay.
**Shenoy Pratik Gurudatt** 17:05 Don, correct me if I'm getting this wrong, but in the current state of the PR, it's only when users chat with the agent, only then the tokens get used, right?
Otherwise, even if the server is up and running, it's not going to incur any token.
**Rohan Arora** 17:22 But then we, you know, if you foresee a world, right, where your load generator now has the capability to start generating these chat interactions, then it will quickly trickle down into what Pierre is saying, right? Because.
**Shenoy Pratik Gurudatt** 17:33 Yeah.
**Rohan Arora** 17:34 your load generator will just fire off, it'll be creating these chat interactions, and then there'll be, like, a bill associated with it, right? So…
**Gerard** 17:41 Yeah, I mean…
**Rohan Arora** 17:42 Completely to that point.
**Gerard** 17:43 We talked about, at one point, making a slider between you know, load generator going to, you know, traditional microservice API calls, then, like, doing some, like, split between that one way or the other, but I could still see a world where you want to, make sure whether or not there's a token installed or not, because even if you start off with zero, should there be a bug or something else like that, then you would have a world where You know, the load generator may be incurring costs, so it's still all a good idea.
**Rohan Arora** 18:20 Yeah, and while we are brainstorming here, right, another component was what… and again, we shouldn't bloat this current PR into that, but just putting it out there, right? What if we had a component in there Which is, let's say, a smaller model which can be used for inferencing.
deployed as a part of the stack itself, right? So, for example, VLLM is a very popular inferencing server. You deploy VLLM as one of the components, as a part of hotel demo, and then, you know, your application, or one of the components in the application could be interacting with that small model.
So, yes, there'll be no cost incurred.
But then at that point, you know, this to me is, like, particularly with the way the LLMD platform and other places are going, is you'd have this inferencing server which is deployed in your enterprise environment.
Instead of you going outside of the environment to make these inference calls, right? So that's another lens which we can take, but again, you know, something which we should… think about a little whether, does it make our OpenTelemetry demo way too bloated?
Than we want it to be, so… but something… something for us to think about, maybe, in the coming months.
**Cyrille Le Clerc** 19:37 I like this idea to have, batteries included, LLM.
**Rohan Arora** 19:43 Yeah, so…
**Cyrille Le Clerc** 19:44 It should just… just be, another container.
**Rohan Arora** 19:48 Yep, it would just be another container in the environment, and, you know, basically, whenever it needs to make an LLM call, it will go hit the LLM call and then come back. It's just that we need to do some homework on which model is small enough.
So that it's not that people are waiting for half an hour to wait for the model itself to be downloaded and deployed, right? So, that's… that's the concern, but, how, like.
let's say if any of the, you know, the Microsoft small models, or the Gemini small models, which are supposed to be running on these Edge devices.
If they are decent enough for our example, then maybe that's something which we may want to consider.
**Shenoy Pratik Gurudatt** 20:28 Yeah, I tried, replacing the OpenAI integration, or at least adding small LLM to the recommendation one, but that doesn't do any React-style agentic flows. It will not give you… it is just good for question, answer, and… But anything where it comes with the agentic stuff, I think we need to do some more stuff. But that was 3 months ago, and things have changed very quickly. So, I think we have much better models now.
**Rohan Arora** 20:56 Yeah, but… but again, right, from the… so, while it might be good for, let's say, the React agents, like, we are… like, the team which Gerard and I are a part of, right, the partner team is building SRE agents, so for them, it makes sense to go ahead and have… be ensured that the React pattern or whatever works.
But in the context of the OpenTelemetry demo, where the objective is to you know, kind of see if we can trace out these interactions, or build some abstract analytics on the top of OpenTelemetry data collected.
does it need to be a model which can do React, right? Or does it need to be a model which can do auto-search and all those things? I think that's the fundamental question, right?
Yeah, I don't have… I don't know.
**Shenoy Pratik Gurudatt** 21:43 Without React, any agentic interfaces fail, that's what I've seen in my experience.
But, it won't be able to make your tool calls correctly. That as simple as that.
**Rohan Arora** 21:53 Yeah, yeah, that's true, yeah, that's true.
**Juliano Costa | Datadog** 22:10 I… I have… Another topic that I would like to discuss… But, I'm suffering from Google Docs here.
One sec, dude.
Okay.
so, we have, PR open, or… a couple of months already now, from, Marching Twice.
Regarding, adding a waiver to the demo. I already brought this, here in the… in the SIG meeting, once we discussed a bit.
Shanoi took a look, and thanks for that. But I actually want to… To discuss a bit, because we… so… This would be… this would add docs to the… to the demo, and, it's just now, an extra… URL slash telemetry that you… we have all the semantics from the demo, so all the custom attributes will be there.
This is nice, but then we are not actually using the full power of Weaver, which would be, like, code generation for… not only for dogs, but also for, classes and, files for other For defining the constants and stuff, where… the programming languages could just use the generated class from Weaver, and also the live check. But I think this is a start.
So… I'm… I will take a final look, and… And, I think, as Shanoy already, look, Shanoy, if you can also take a look, and, when we are… when we agree, we get this one first, because then, we can start Moving on to the next phases.
Because that would be the first one.
Go ahead, Cedar.
**Cyrille Le Clerc** 24:32 You said first step, Pierre, this is one of your colleagues, no?
Can you…
**Juliano Costa | Datadog** 24:38 Pr… PR changed.
**Cyrille Le Clerc** 24:40 Oh, you changed? Sorry. Yes.
So, yeah, no, how can we be sure that it's a next… there will be a next step?
**Juliano Costa | Datadog** 24:51 Well, we can't. That would be on us, I think.
**Pierre Tessier** 24:56 I'm… for what it's worth, I… I still stay quite a bit in touch with Martin.
On it. And he did say, like, do whatever you want with that PR.
There are, like what Giuliano said, there are a couple, phases to this. The first one is probably generating the docs.
I think generating code or the initial classes is another one.
I, for what it's worth, really want LiveCheck.
In here, because CI depended bot, and CI is a problem on the demo.
It's just a workload that we can… If we could get back to integration testing.
I would be much happier. I've even looked at, like, can we expose a Jaeger API somehow to do this, and write our own test harness? But, you know, ideally, Weaver does this for us, and then… Product.
**Juliano Costa | Datadog** 25:53 Yeah, I think… I think the problem is that Weaver cannot validate the connection between the spins. But then, for this, we can use a Jaeger… because… so, you said expose the Jager API, but actually, Jaeger, we can query the… the traces get a JSON from it already.
**Pierre Tessier** 26:14 Huh.
**Juliano Costa | Datadog** 26:16 I'm doing that in a rep already, so…
**Pierre Tessier** 26:18 Okay, well, we should… maybe that's what we need to do. Maybe we just write a small test harness, and we just do that instead.
**Juliano Costa | Datadog** 26:26 Which…
**Pierre Tessier** 26:27 Because I regret.
**Juliano Costa | Datadog** 26:27 Trace Fest, but, it's smaller.
**Pierre Tessier** 26:30 Yeah, I don't think we need to replay trace tests, but a test harness that can be leveraged in CI.
**Juliano Costa | Datadog** 26:35 that when we…
**Pierre Tessier** 26:35 The demo's way too large.
**Juliano Costa | Datadog** 26:39 I think that the main problem there is creating something that, like.
How we will define the tests.
which, that was what TraceTest did. Like, they had their YAML definition, where you said, hey, this service connects to this service, and… Whatever. So we need to define this somehow, and then… Well, with Claude, we just need time. But yeah, or not even too much time. We just need to ask him to come up with something.
Okay, so we have, next steps, planned.
By the way, I also have a chat open with Martin. He is super responsive. I just don't know when he will come back to the things, so sometimes I ping him, and he's like, hey, I'm in the middle of something.
I'll get back to you. And then two weeks passed, and he's like, hey, I've done this, then that, here it is. So, yeah, it's just that.
**Cyrille Le Clerc** 27:46 Or maybe a week.
**Juliano Costa | Datadog** 27:47 contributed I'm always.
**Cyrille Le Clerc** 27:50 should be optimistic.
And then ask the Weaver people if someone can help, if Mark is struggling to get that space.
**Juliano Costa | Datadog** 28:01 I'm a huge fan of Weaver, so yeah, I'm happy to see Weaver in the demo.
The problem is that everything that we are discussing is beautiful.
The problem is that, whenever we have Weaver, and then all the agentic things.
If we do not have a proper testing mechanism and something that will be able to spin up part of the demo, people will simply stop using because it's getting out of hand.
**Cyrille Le Clerc** 28:33 Yeah.
And we will be blocked to evolve onto.
Agreed.
**Juliano Costa | Datadog** 28:40 Yep.
So, I think we have also… okay, last thing that I will bring up, we have also a PR that… brings back the Docker profile things.
So this would replace all the Docker… Docker Composes that we have with two with… I think it's one Docker, one Compose file with two different profiles.
So the full and the minimal. So maybe we can, whenever we have that set, maybe we can think about adding the agentic one that would run the full together with it, and then consider.
The problem with that approach.
is that with Docker, we can do everything we want, different setups, different services, starting with different profiles, this is great. How we do that in Helm?
**Pierre Tessier** 29:43 What if we define a top-level construct?
That says, what mode you want to run in? Full or not full?
And then each mode, internally, inside the Helm chart.
We say this mode has these services, this mode has those services.
There's probably… but there are some service-level overrides, as well, that we have to be careful of.
Right? Because when you poke… there's, like, environment variables that we have to reset, so I think we could do it, but I'm thinking it's just a… it's a top-level thing. Which mode do you want to run the demo in, or profile, whatever we decide to call it.
**Juliano Costa | Datadog** 30:27 Cool.
**Cyrille Le Clerc** 30:29 Don't we have on hand chart already the availability to enable, disable many subcharts on many components with the enable-disabled?
**Pierre Tessier** 30:40 I, I think the… that's for the, In, like, the sub… like, the sub-charts, it's a hard enable, disable there.
But I mean more…
**Cyrille Le Clerc** 30:55 Contin on, you have more.
**Pierre Tessier** 30:57 Yeah, this is more, like, the actual components itself that are part of the demo. So the… not the observability components, which we subchart.
If that makes sense.
**Cyrille Le Clerc** 31:08 They also are, they have, enabled disabled flags, which I think are already used by vendors to, when they want to remove the batteries included. But, yeah, to be verified, but I think that.
**Pierre Tessier** 31:23 Yeah, I think it's a finite control one, I think we could create… an overriding flag that overrides it in other people, or something. We could… you know what I mean?
**Cyrille Le Clerc** 31:37 a JSON overall values, .yaml that we'll just, set.
A true-false on these, enabled flags, maybe.
I was thinking.
**Pierre Tessier** 31:48 You know, maybe that's a better solution, actually, Juliano. We just provide what a minimal YAML looks like.
And it just specifies each component with enabled false, and the few overrides you need.
So default is full, but we provide documentation on how to run it in a minimal mode.
or, like, it's really just an example YAML file, and you can modify that values file, right? So we say, hey, if you want to run minimal, here's a sample values file that runs it in minimal mode, it works.
you know, fewest things possible, tweak this to your content. If not, run it without a values.
Or, you know, run without any overrides. I think… I like that.
**Juliano Costa | Datadog** 32:40 I… I gotta jump to another call, but just to let everyone know, the SIG meeting is already, changed to weekly, so if you just update your, Canada, you should see the new thing there.
**Pierre Tessier** 32:59 Cool.
**Juliano Costa | Datadog** 32:59 Thanks, Farah.
**Rohan Arora** 33:00 Alright.
**Juliano Costa | Datadog** 33:01 everything, for all the discussions.
**Rohan Arora** 33:02 True.
**Juliano Costa | Datadog** 33:03 Let's see you next week.
**Rohan Arora** 33:05 Thank you, everyone. Bye.
