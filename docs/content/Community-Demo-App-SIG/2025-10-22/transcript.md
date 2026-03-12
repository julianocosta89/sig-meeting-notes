SIG: Community Demo App SIG
Date: 2025-10-22
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 02:46 Hello, hello!
**Pierre Tessier** 02:49 Giuliano.
Hey, Joss.
**Juliano Costa | Datadog** 02:52 Alright, thanks.
**Pierre Tessier** 02:54 They're good. Even better.
I know.
**Juliano Costa | Datadog** 02:58 Some people I'm stepping down from manager to IEC, and all of a sudden I'm doing an IC role. It's kind of weird.
**Pierre Tessier** 03:06 I still have to hire my replacement, but yeah.
So… .
**Juliano Costa | Datadog** 03:15 Well, hopefully you can focus on things that you like to do.
**Pierre Tessier** 03:19 Yeah, yeah, I actually did that yesterday. I, Using collectors and, collectors and feeding into collectors.
We have some customers who have been asking for just… can we flow data into a team for them? Into an account for them? So… We decided to take our standard demo data flow and flow it all through an additional collector, and then in that collector, we just stand up additional exporters, and it's easy for anybody to add.
A new export to it.
So we called… we created a new collector, we called it FanO.
And the fan-out collectors really only has OTLP receivers, and… as many OTLV exporters as you want to put on there, and the exporters are just going to different accounts, all it is. It's all the same data.
**Juliano Costa | Datadog** 04:10 Okay.
**Pierre Tessier** 04:11 You know.
album.
A lack of having a sample app out of the box that you could just leverage in the tool, like, we have a playground thing, but this is really to solve kind of a larger company initiative, so it was… It was… it was good to use OpenTelemetry's core technologies to do… to solve a real-world problem.
One way to say it.
**Juliano Costa | Datadog** 04:36 Awesome.
12 seconds.
Well, yeah, I'm happy to see the demo being used.
So…
**Pierre Tessier** 04:43 Yeah, yeah.
A lot more.
I like somewhere, you go look at some other, even adjacent company's demonstration, and their, like, checkout service, or, you know, you see all these names, they're like, I know what that is.
**Juliano Costa | Datadog** 05:01 Yeah, I… I reckon that name, yeah.
**Pierre Tessier** 05:05 Oh, God.
**Juliano Costa | Datadog** 05:05 I was at KCD Varsal, two weeks ago, and, well, I shared the pictures on the, on the channel, but, Dalton, Dorowitz.
shared the… the architecture on the keynote, and Andre from Elastic also shared, the demo in his demo, while he was presenting, So yeah, I was happy about it, so… In my presentation, I didn't use the demo, but they used, so yeah.
I mean, yeah.
Rom-com.
**Pierre Tessier** 05:46 Of course the hotel demos use that prom. Why wouldn't it be?
OpenTellertree now exports natively to Prometheus, for that matter.
It's better, right?
**Juliano Costa | Datadog** 05:59 So, Derek, I don't think we have met before, so hi.
Welcome to the SIG meeting.
**Derek Mitchell** 06:10 Thank you. Nice to meet you.
**Juliano Costa | Datadog** 06:13 Cool. So, we have a couple of things in the agenda, so… Let's try to get going, otherwise we won't be able to go over everything.
So the first thing that I would like to discuss… is this PR from Lukash, from Splunk, actually.
If I'm not mistaken.
**Derek Mitchell** 06:42 That's correct, Ann.
**Pierre Tessier** 06:43 I mean, there's a…
**Juliano Costa | Datadog** 06:44 Cool, yup. So, he… he's proposing Adding a couple of different databases, and whenever running the demo, we could switch, or… Swapped, the one that we start.
We currently have the Postgres, and he added MySQL and MongoDB.
I like the concept.
I don't like the… the… the implementation, because currently, he relies a lot on Docker. So, like.
In Helm, we could do something similar to that, but with the Kubernetes manifests, it would be, like, a little bit tricky. I know that whenever running Kubernetes, deploying three different pods for 3 different databases wouldn't be a problem, but still, two databases would be useless, because the service just chooses one, and then connects it Connects to this one.
And we configure that via environment variable. With Helm, we can say, hey, I want to use this one, and then it would just install that one. And in Docker, I think he implemented logic to actually just deploy this one.
The thing is, we had the PR from Henrik some time ago.
That had… that had DAPR within it.
And with Dapr, we could do this… switch, because, Dopper is something that stays in between the service and the database, and then the service talks with Dopper, and Dapr talks with the database.
The application doesn't need to know which database is topping.
So that would be a nice solution, because then, like, the application… Code doesn't change.
Basically, it is the same, like, what OTEL did with all the vendors. Dopper does with all the databases.
We didn't get… Henrik Piara through, because Dapper wasn't following… well, it is still not following the semantic conventions for databases.
So… Like, if we… get that, then we lose all the db.whatever spans that we have that we know that are stable and useful.
So, yeah, over here it is… So, that's why I wanted to discuss with.
**Pierre Tessier** 09:28 Yeah, and I'm looking at this PR, I don't hate the Docker Compose.
way that he's doing things. We would be able to achieve something similar in Helm.
So I don't hate that. I think that's probably the only way to do it anyways. I do not like… the big, long, if this, then this branches based on Mongo, MySQL, or Postgres.
encode. And this is the part that Dopper would solve for us.
**Juliano Costa | Datadog** 10:01 Yep.
**Pierre Tessier** 10:01 Specifically.
We know when Dapper plans on having proper support for semantic conventions.
**Juliano Costa | Datadog** 10:09 I… I met one of the maintainers of Dapper, and, he's, he said that it would be awesome if someone from Hotel had, like, a… some… calls with maintainers from the upper to, kind of, or actually just go and control.
**Pierre Tessier** 10:27 It's…
**Juliano Costa | Datadog** 10:28 this, so…
**Pierre Tessier** 10:28 Wouldn't that be Henrique?
**Juliano Costa | Datadog** 10:30 Can we just ask that? Yeah, or, Kasper from Dash Zero, he's also in contact with, Mauricio Salaboi.
Okay.
**Pierre Tessier** 10:43 So we… I think we need to reach out. I would love for us to… I don't like this code, and I agree with you.
I would prefer the code be… a implementation-style thing, and then we let another layer take care of all of it for us, and it would bring in another CNCF project at the right state. I think the other problem with the initial PR that Henrik wrote is that he was doing it for all the services, and this here would only touch the accounting service, which I think is.
**Juliano Costa | Datadog** 11:11 Yeah, it does.
**Pierre Tessier** 11:12 You know what I mean? It keeps it more kind of compartmentalized a little bit.
**Juliano Costa | Datadog** 11:16 Yep. That would be awesome.
Cyril has a good question here. So, why do we maintain Kubernetes and Helm chart? I think… our initial idea was because not everyone uses Helm.
But I would say that, yeah, Helm is well established as of today. Like, we could… and that would be, like, a maintenance burden, free, because then now we release the demo, and then we push something to Helm, and then we come back to the demo and update the KHS manifest. So if we drop the KHS manifest, we are just like, hey, if you want the KHS manifest, run, make, generate a KHS manifest, and you can deploy. But we do not maintain it.
on the demo.
I like that.
**Pierre Tessier** 12:09 Why don't we… Just give them a make command.
**Juliano Costa | Datadog** 12:15 Yeah, yeah, we already have one.
**Pierre Tessier** 12:17 We already have the make command in there that we use. We would just tell them, you have to run it, and then you can deploy it.
**Juliano Costa | Datadog** 12:23 The thing is that the make command executes Helm, so if the have held me styled, and, like.
**Pierre Tessier** 12:33 Oh, well… You see, the difference is that some people are not allowed to use Helm to deploy to Kubernetes, but they can still have Helm locally to generate things.
Right? Like, it could be part of your local toolchain, but you're not allowed to use it to deploy to your Kubernetes infra, for whatever.
**Juliano Costa | Datadog** 12:53 reason.
**Pierre Tessier** 12:53 They don't allow that.
Right? They might be using another mechanism where they have to push a YAML file over, and that YAML file gets brought in and does its thing.
So we could keep all the constructs in Helm to do all the branching and everything else.
**Juliano Costa | Datadog** 13:10 Sorry. Sorry, coming in?
**Derek Mitchell** 13:12 Sorry, sorry to cut you off, I'm just saying, I've seen that in customer environments where no problems installing Helm locally.
It's just, you know, pushing it to production, that's the issue.
**Juliano Costa | Datadog** 13:25 Awesome. Well, I guess we could do that. Another approach, that is also, I think, doable, I've never tried it myself, but I think it's doable. We create a Docker image with Helm, and just a shared volume.
the person runs make, generate K8s, then the manifest files will be generated in this shared folder, and the person doesn't need to have Helm installed.
**Jonathan Munz** 13:56 That's.
**Pierre Tessier** 13:57 I mean, that's not a bad idea.
**Jonathan Munz** 13:59 Juliano… Can you generate the APK for the React Native example?
**Juliano Costa | Datadog** 14:04 Did you do that?
Yep. Okay.
**Pierre Tessier** 14:09 I… I like that idea a lot more, because then it doesn't have… it has zero dependencies outside of Docker Compose, which we already force as a dependency.
And make, I guess, which we also kind of force.
Yeah, we should do that, we should update our docs accordingly as well.
And it would shorten our release cycle.
And make our releases a little cleaner, as well.
**Juliano Costa | Datadog** 14:38 Absolutely.
**Pierre Tessier** 14:39 having to do two releases every time I release anything.
**Juliano Costa | Datadog** 14:42 Yeah, so I need to come back to Lukash. I actually reached out to him directly on Slack, and he said that he wouldn't be able to make it, so I said that I would return to him.
So… should we agree… so should I come back to him and say, hey, we actually decided to… to… wait for Dapper, or, like… would you be willing to change the PR to use Dopper, and then we go to Dopper and say, hey, can we have that, following semantic conventions, or whatever?
**Pierre Tessier** 15:28 Maybe I'm just unaware of what the differences are. What is wrong with the telemetry that Dapper is emitting today? Is it just… it's not using the right attribute names, or is it something else?
**Juliano Costa | Datadog** 15:39 Yeah, I think the database, database attributes are not there. So, like, we have… They're not there. Yeah. To be honest, I wasn't able to run Henrik's PR, so I don't know what telemetry we get out of it.
But we… we can…
**Pierre Tessier** 16:01 I want to explore going down the DAPR route.
And if the problem is attribute key names are not matching, we could use the collector to rename some things today.
as a temporary fix, while we force and work with the Dapper community to update their stuff. We've had this pattern already before for Next.js instrumentation, which is broken, so I think it's okay as long as we agree that, hey, it's a temp fix, put the comments where they belong within the collector manifest, or the collector's config, to make sure that we're clear on that one.
And then we can work. Now, but if the problem is, is they're just not emitting the telemetry at all, that's a bigger, wider problem.
So I think I need to understand more greater what is the problem with the telemetry that DAPR is emitting today.
**Juliano Costa | Datadog** 16:53 We… well, I don't think it's hard to… to… to play around a little bit, and I can maybe reach out to… to Casper, and ask him if he already has something, because I know that he worked with that already,
**Pierre Tessier** 17:15 That PR is a great… is a great candidate for dapperizing.
better.
**Juliano Costa | Datadog** 17:19 Yep.
**Pierre Tessier** 17:20 Right? I think let's… let's get dapper. I think that's what we were waiting for. We're waiting for a good use case to make it where it makes a lot of sense, and this is it, right here. Let's use it for why it's there. It's there to make it easy for you to switch, your DBs behind the scene.
While keeping your calls feeling native, and I think this will allow us to do what we want to do.
And so if anybody from the Dapper community has interest in getting part of the OpenTelemetry demo, hopefully they could maybe participate in helping that PR along.
And… You know, we still have those standing questions on what does the telemetry look like.
fix it in a collector, let's… let's do that, let's move forward, and then we will follow, fast follow with getting Dapper to release with good telemetry instead.
What language is DAPA written in?
**Juliano Costa | Datadog** 18:09 You're asking too much, that bird question. I'm sorry.
**Pierre Tessier** 18:12 Okay, I should go… I should go join a DAP or SIG, is probably what I'm thinking I'm hearing right now.
**Juliano Costa | Datadog** 18:16 Yeah, I, I… Okay, let me see. I'm just opening Dapper here, I… Yeah, it's cool.
97.1% of the code is gone, so…
**Pierre Tessier** 18:29 No problem. Let's go.
**Juliano Costa | Datadog** 18:32 Cool.
**Pierre Tessier** 18:33 Let's make this a thing, let's make this a thing that we do, then. I think it's a… and the path we should move forward with, is doing that, so maybe we could ask the author?
To bring down that path.
**Juliano Costa | Datadog** 18:43 Cool.
Okay, second, second PR, second topic that I want to discuss is, really exciting, actually, and Derek's here to kind of, Make… make his point.
It is a GenAI service.
And he implemented a custom, or a service, Kind of, product review.
thingy, and… yeah. Derek, do you wanna…
**Derek Mitchell** 19:19 Yeah.
**Juliano Costa | Datadog** 19:19 Stay, stay stage, yeah.
**Derek Mitchell** 19:21 Yeah, thank you. Yeah, so the idea here was to introduce, a service and functionality where we could demonstrate OpenTelemetry support for Gen AI.
So the approach that I took was to, basically implement a mock LLM. I didn't want to add a dependency on, like, GPUs, which are, you know, not always easy to find, or, like, commercial LLMs, because you don't want, like, now to have a cost associated with running the demo.
So I decided to mock an LLM service. It follows OpenAI's, like, Chat Completion API.
Which is becoming, like, fairly standard. Like, almost all the LLMs support that, that format.
other than Anthropic and Google, sort of, notably stick to their own format.
But anyway, so there's a mock LLM service, and then there's a new product reviews service that calls it.
And the idea there is to add the concept of product reviews to the product detail page.
And the AI is used to effectively summarize the product reviews.
So each product has just 5 reviews, and the AI is used to, summarize those reviews.
And then finally, there's a MySQL database, which is used to store the product reviews.
And I did that so that we could do, like, a tool call.
So that when the product review service calls the LLM, The LLM says, hey, I need more information, I can call this tool to get the project reviews from the database, which it does.
And then it can actually return the summary.
I don't have it running right now, but there is a screenshot, in the PR.
Kind of showing how the, The product reviews appear, and as well as the summary.
**Juliano Costa | Datadog** 21:22 What I… the first thing that I said to Derek, just to put everyone on the same page, is that we got a PR from, What's his name?
Arrow, from Google.
Some time ago, 2158, Where he came to the… to the SIG meeting to discuss this idea, and we decided that we didn't want to rely on any, like, Gen AI vendor?
So, he said that he would implement in a way that we could simply choose either Gemini, or OpenAI, or whatever the other one is, provide a key, and the service would actually call it.
So, here is the first difference. The implementation from Aaron would call the… the… GenAI. The thing here is that this would cost the user that is running, I think, right? I don't think we can, call OpenAPI without, via API without paying, can we?
**Pierre Tessier** 22:39 I don't believe so, no. You need an API key.
**Derek Mitchell** 22:41 You know?
**Pierre Tessier** 22:42 There'll be some token usage there.
**Juliano Costa | Datadog** 22:44 Yeah, so the mock-up would be a nice idea to that.
And we could demonstrate the semantic conventions for Gen AI that are actually stable.
Yeah, but .
**Pierre Tessier** 22:55 I wonder if there's a way… Or, because inevitably, somebody's gonna say.
I want to test this without the mock service. I want to actually hit OpenAI with my token, knowing full well I'm going to spend a few dollars to test this out.
And I wonder if there's a way for us to provide them an option where if they provide us a key.
Then, instead of doing the mock call, we actually call OpenAI instead, directly. Is that a possibility we could do with this?
While having the whole… the whole interaction traced, still?
So that, to me, like, adding LLM observability is definitely something we hear a lot about across the board. And I think it's great to do what the Moxer is, because it allows it to stay self-contained and be free.
But ultimately, there will be somebody out there who's going to raise their hand almost immediately and say, I need this to work in real world.
Like, I want to make an actual OpenAI call.
Yeah, and I'm okay with that Anthropic as well. I'm okay if, like, OpenAI, that's what we did, because we wrote to the OpenAI API, and until Anthropic supports it, it is what it is.
Although I feel like, doesn't Langchain solve for that?
**Derek Mitchell** 24:08 Sort of. I mean, with LaneChain, you still need to say, I want to use, like, LaneChain OpenAI, or LaneChain Anthropics, so you need to pull in the right package.
So, I mean, the nice thing about OpenAI is that with Langchain, or with just OpenAI, you can also use open source LLMs. So, like, we have a demo with Mistral, but we use the OpenAI langchain OpenAI to communicate with it, or just the OpenAI SDK. Either one is fine.
Yeah, Anthropic and Gemini require, like, Different packages, different, different code.
But for sure, we could easily just swap in a real LLM, as long as it's OpenAI compatible.
And all the rest of the code would just work.
**Pierre Tessier** 24:57 I think we should do that.
**Juliano Costa | Datadog** 25:00 Well, so…
**Pierre Tessier** 25:01 And it would solve for…
**Juliano Costa | Datadog** 25:04 So the… the main point here for the, for the meeting is, should we then move in with, or move on with this one from Derek, and then do a follow-up PR with, adding this configuration to kind of allow Switching?
**Pierre Tessier** 25:24 Yeah.
**Juliano Costa | Datadog** 25:24 I would rather do a separate PR, because this one is already big. We actually need to clean up a couple of stuff, but yeah.
**Pierre Tessier** 25:32 Yeah, we could make it a separate PR to allow you to… when you leverage a mock database, or a mock database, a mock LLM versus OpenAI.
That could be a fast follow, for sure, but I think that needs to be the path we do with this capability.
**Juliano Costa | Datadog** 25:53 Awesome.
**Pierre Tessier** 25:54 The telemetry generated from this, do they follow the semantic conventions for LLM?
**Derek Mitchell** 26:02 Yeah, I've looked at the traces, everything, everything looks good. It's instrumented right now. So the product review service is instrumented with the OpenTelemetry, OpenAI, VTU instrumentation.
So, everything looks good. The interesting note, I think, is that I did not instrument the LLM.
Because normally you wouldn't do that, right? So, I mean.
**Pierre Tessier** 26:23 No, no, no, no, you want to instrument the interactions with the LLM, not the LLM itself. That's a whole different beast. I don't want to get into that yet.
**Derek Mitchell** 26:31 Yeah.
**Juliano Costa | Datadog** 26:34 I love the yet, but yeah.
**Pierre Tessier** 26:39 You know, one day, we'll have, like, DNCF LLM, and somebody's gonna ask us to implement it.
Julie, I know, like, one day, we're gonna need to come in with, you know.
12 gigs of RAM and, like, 4 virtual CPUs just to run the demo. It's coming.
**Juliano Costa | Datadog** 26:59 Cool. You know.
I'll… okay, so, Derek, the only thing that I… that I want to ask on the PR is if you could drop the K8… demo YAML changes, because this file is currently, auto-generated with the make comment.
**Derek Mitchell** 27:22 Oh, okay. And it's based on the Helm…
**Pierre Tessier** 27:26 Yep.
**Juliano Costa | Datadog** 27:27 of the Helm, updates, so…
**Pierre Tessier** 27:31 you know, us removing this from the demo and making this all documentation will… the number of times we have to go to PR and ask people to undo that changes.
**Juliano Costa | Datadog** 27:39 slightly annoying.
**Derek Mitchell** 27:42 Okay, and then I guess I need to update the helm chart as well.
Would you…
**Juliano Costa | Datadog** 27:46 Yeah, I.
**Pierre Tessier** 27:49 The Helm chart would be a separate PR on a Helm… on a Helm charts repo.
**Juliano Costa | Datadog** 27:52 Yep. And, that will only take effect, whenever we decide to… to release, but I think that addition is a nice addition, and we should cut a release, because If we wait, like, 8 months as we waited the last time, that… yeah, it was a mess. I don't know if you follow all the releases that I… that I.
**Pierre Tessier** 28:18 I did.
**Juliano Costa | Datadog** 28:18 But yeah, sorry.
**Pierre Tessier** 28:21 I always like… would love for us to have a cool new feature that we can release.
coinciding with a major CNCF conference, like the one happening, I think, in 3 weeks. I know this is asking for a lot, but can we maybe get this LM thing in there? I… the Dapper one might be a little bit more of a stretch as well, but if we could do those both, I will see to it we have a push of getting these things done on the Helm side.
So we could do a full release.
like, the weekend before. I know I'm asking for a lot.
But it would be great if we could get this out before Observability Day.
**Juliano Costa | Datadog** 29:00 What I can promise, Derek, is that I will take a look at the… at the PR latest tomorrow, so… I can…
**Pierre Tessier** 29:08 Okay.
**Juliano Costa | Datadog** 29:11 Well, we can get.
**Pierre Tessier** 29:12 Yeah.
**Juliano Costa | Datadog** 29:13 Merged soon. But the…
**Pierre Tessier** 29:18 Is asking to get this all done.
**Juliano Costa | Datadog** 29:19 Patient.
**Pierre Tessier** 29:20 Is asking to get this released by, like, say, November 7th too much to ask for?
**Juliano Costa | Datadog** 29:27 Yeah.
**Pierre Tessier** 29:29 two weeks. I know it's very narrow, probably is too much.
**Juliano Costa | Datadog** 29:32 Yeah, no, next week, Well, I don't know about you guys, but I'm kind of traveling the next two weeks, so, yeah.
I won't be available.
**Pierre Tessier** 29:47 I could definitely help with all the help stuff, Derek, okay?
I think if we can get this working.
end-to-end telemetry, working through all the Docker stuff, I could definitely make the Helm stuff work.
the database swapping stuff, I have less confidence in, because that… it's got the unknown dependency on Dapper.
That we still have to solve for.
**Juliano Costa | Datadog** 30:13 I think implementing it it's not, that… that much of an effort, to be honest. Dapper is pretty… simple, and I… if I'm not mistaken, Henrik actually already has that.
**Pierre Tessier** 30:27 We should just look at Hedrik's PR paper, and it's probably… Okay. I will have cycles of spend on this now, Julie, I know, because my role changed.
Awesome. So I will… I will… I will take on this as a challenge to make sure that we could at least get this LLM stuff shipped. I think it's important.
AI is all the rage, and I think it would be great if we could come out and say, hey, the Opatometry now has the LLM support, or the OpenTeometry demo now has LLM support, and I think that would be a good thing to do.
**Juliano Costa | Datadog** 30:56 Awesome.
**Pierre Tessier** 30:57 And it makes… you know, there's a lot of excitement around it. Let's capitalize on that excitement.
**Juliano Costa | Datadog** 31:04 Oh, the thing that I mentioned, I just pasted here the link, right under the PR from Derek.
The… the PR from… Oh, Jesus, I pissed on the wrong place, sorry.
So, in the prize thingy, I just pasted the link to the… yeah, from here.
Okay, so… I think we can swap the order here to have, as we are… with cereal, so I've got Cyril here in the call, so… and I think we will not be able to… Talk about everything.
There's this issue that's real open regarding… Swapping out the… other services to use HTTP protobuf instead of, gRPC.
**Pierre Tessier** 32:06 We didn't do it before because not all services… not all SDKs supported when we did the initial effort. I think they all support HTTP protobuf now, right?
**Juliano Costa | Datadog** 32:16 Yes, and the other thing is that when we started this sync, gRPC was the default.
**Pierre Tessier** 32:23 I know, I know.
**Juliano Costa | Datadog** 32:25 So…
**Pierre Tessier** 32:25 I'll repeat my statement again, GRPC was a mistake.
**Cyrille Le Clerc** 32:31 No runting.
**Pierre Tessier** 32:34 No, no ranting allowed.
Can we… can we get a list of, here's the services that do this, and just look at it? Let's set up a multitask issue, and we'll just hammer it out?
And get them all converted over.
Let's just do that. Let's get it, let's get an issue set up. This service, this, like, all the services that need to get moved over.
list it out, and then we'll… as we solve in PRs, we'll check off that task.
And then we can resolve for this. We should get everything onto what is the currently recommended approach from OpenTelemetry, which is HTTP protobuf anyways.
And it'll allow Serial to do these other future PRs that we wanted to do.
actually work.
Because the… Auto-instementation environment variables only support one Of the two. You have to specify which one.
**Cyrille Le Clerc** 33:33 I have an update on this. I gave up in some ways, because… I gave up, not on hotel operator, but hotel operator to inject configuration in the SDKs.
Because Helm charts, I couldn't find in Helm charts a solution to… Wait for hotel operator to be up, configured, on Zen.
After this up, Trigger the initialization of the demo services.
**Pierre Tessier** 34:07 What if we make this… What if our instructions change, then, instead?
**Cyrille Le Clerc** 34:15 Install the operator first.
**Pierre Tessier** 34:17 wait for it to be installed, and now install the demo. Can we do that way?
**Cyrille Le Clerc** 34:22 Then it looks to me like two consecutive Elm charts to install, to be debated.
**Pierre Tessier** 34:29 Yeah.
Yeah, I think that's okay. Install this helm chart, get the operator up and running. Now install this helm chart, get the demo running.
**Cyrille Le Clerc** 34:37 That's an idea.
We can work on it.
**Pierre Tessier** 34:41 Because I know what you're talking about. Help doesn't have a facility for… to wait. It doesn't… it doesn't have that concept.
But if we have a dependency and it takes more than, you know, we need the operator to be initialized and working before it all works.
I think that's a valid way, and we could just document this.
We could put it in the README for the Helm charts, itself.
And put it in the official documentation.
On docs atopentelementary.io.
**Cyrille Le Clerc** 35:12 As soon as we adopt the hotel operator for some things, like managing hotel collectors, it will be pretty easy to go through the steps you described.
The big effort is to go tell operators, and for the config of the SDKs, it's pretty easy.
So we can do this incrementally.
**Pierre Tessier** 35:37 Okay.
I still like to… like, people ask for this.
our challenges before, where we couldn't inject the actual SDKs, but injecting configuration makes a lot of sense, and it's the next best thing, so I think we should… Find a way to do this.
**Cyrille Le Clerc** 35:53 without putting… the vendors who integrate with the hotel demo uncomfortable with, unplanned, incompatibilities, I guess, so maybe, yeah, being incremental to give them visibility will be good as well.
**Juliano Costa | Datadog** 36:14 To be fair, I think a lot of vendors that we have listed are not, aligned with the new updates from, the Helm chart? So, from the… from the demo.
So, yeah. I mean, we can, of course, always, like, raise all the breaking changes that we are doing, but I don't know if everyone is… This won't be a breaking change, though.
**Pierre Tessier** 36:42 Right? Because it's still going to operate without… it's still going to work either way.
This would just be a way for us to say, hey, this is how the operator does this injection.
**Juliano Costa | Datadog** 36:51 Versus using environment variables, right? And we would just have a mode when you install the Helm chart that I'm getting installed operator style.
**Pierre Tessier** 36:59 And I think it would make for a great blog post and a good chunk of documentation on what is happening and why it's happening.
Just get… can't wait till we do configuration files. It's coming next.
Configv2 is getting approved, man. I'm seeing it in release candidate mode right now.
**Juliano Costa | Datadog** 37:19 Is that… is that the blog post that they released?
**Pierre Tessier** 37:24 No, it's not released yet, but it's, like, RC1 I've seen in there.
**Juliano Costa | Datadog** 37:27 Yeah, no, but they released a blog post explaining the config.
And to me, it was, like, a mess. I think nobody actually…
**Pierre Tessier** 37:37 Thank you.
**Juliano Costa | Datadog** 37:37 the developer experience.
**Pierre Tessier** 37:39 Thanks, thanks for joining.
**Juliano Costa | Datadog** 37:42 like, the fire was so complex, and, like, Jesus Christ, yeah.
**Pierre Tessier** 37:49 It's still in experimental stage. It's an RC, like, the format for the file is an RC1 right now.
So, I believe that's gonna be the format.
**Juliano Costa | Datadog** 38:03 I don't disagree with what you're saying, as…
**Pierre Tessier** 38:08 I feel like every SDK now has to have a config file as complicated as the collector's. Probably.
That's what it's starting to feel like. The good news is, though, is beyond using language-specific things, the file will be portable from SDK to SDK.
**Juliano Costa | Datadog** 38:28 Yeah, that's true. But that… this portability, I think Alex, from Honeycomb, Alex Bolton, was sharing two coup codes ago with the V1, so… and the file was… Pretty straightforward, was great.
Like, I loved it, I loved his presentation, I, like.
Hey, this is awesome, thanks! And then, yesterday, I, I I got the new blog post, and I read through, and I was like.
**Pierre Tessier** 38:57 God.
**Juliano Costa | Datadog** 38:58 What the hell?
They read it to you.
**Pierre Tessier** 39:02 On the same note, I was configuring, the self-telemetry for the collector.
and realizing how complicated that was, where I just really wanted to just give my own exporter to it, and it's like, you can't. You have to redefine the entire exporter through it. It was just like, I already defined my exporter, can't you just use… it felt… and what I ended up doing is I just… I had it instead export to itself's own OTLP endpoint.
**Juliano Costa | Datadog** 39:27 Yeah, but.
**Pierre Tessier** 39:27 I feel like that should be an easy button.
**Juliano Costa | Datadog** 39:30 That's not, the recommended approach, so that's the thing.
Because then you kind of, you'll have an inception, you know? So, yeah, but anyways, it's just, like, the way that they decided to go, so… Huh.
**Pierre Tessier** 39:49 Juliana, we will continue to fight for developer experience. Just, let's just remember that.
**Juliano Costa | Datadog** 39:54 I'm part of the developer experience, SEEK, so, like.
Yeah, there are a lot of stuff to discuss, actually, so…
**Pierre Tessier** 40:06 I, I, I… Good meeting. Let's get this LLM thing shipped.
for KubeCon. Let's make that a goal, and his secondary goal will be getting the database Mongo MySQL thing shipped as well.
Okay, and all these little other things taken care of.
**Juliano Costa | Datadog** 40:23 So, what… what actually… well, yeah, okay. Well, because what I was about to say is that with direct service, we get, MySQL.
**Pierre Tessier** 40:34 So then we have Postgres and MySQL.
**Juliano Costa | Datadog** 40:36 So it's just a matter of, having… the mobile… They should have shared it.
**Pierre Tessier** 40:43 They should… they should share… Should we share a DB in this case?
Or do we want to deploy two DBs?
**Derek Mitchell** 40:53 Yeah, my, I mean, my logic was that Postgres, at least, was dedicated for accounting service, at least in how it was named.
And I thought it would be beneficial to have another type of database, so I went with MySQL.
Not knowing that Lukash was submitting the PR4 database, which… Yeah, so that was my logic.
**Juliano Costa | Datadog** 41:15 Okay.
Yeah, the thing is that I think if we actually use the LLM, then the database won't run, right?
Yeah, it will still run.
**Derek Mitchell** 41:26 It will, it will still run.
**Pierre Tessier** 41:27 10 minutes out.
The initial intent was for actually the Postgres database to not be just for accounting.
And it would be a shared database across. That's why it was just called Postgres.
And not called Postgres Accounting, like what we did with Redis, where we called it Redis cart.
**Juliano Costa | Datadog** 41:56 Valkycard.
**Pierre Tessier** 41:58 Whatever, you know what I mean.
**Juliano Costa | Datadog** 42:01 But yeah, okay, but I think those… Well, Derek, do you think we, you could swap the database part and use the same one that we already have?
**Derek Mitchell** 42:21 Yeah, that's fine, I'm not doing anything, you know, groundbreaking, it's just a simple, simple table.
**Juliano Costa | Datadog** 42:27 And it's mainly just to do the tool lookup.
**Derek Mitchell** 42:30 to say, you know, hey, I call the LLM first, say, hey, can you summarize these project reviews? And I have these tools.
Then the LLM says, hey, I want to do a tool call.
To get the product reviews from the database.
**Pierre Tessier** 42:43 So…
**Derek Mitchell** 42:44 So yeah, I can… I can swap in Postgres.
**Pierre Tessier** 42:47 Yeah, I think what we should probably do is probably create… make sure this is schemaed properly within Postgres. I think right now we're all just dumping into the public schema, and we should probably have two schemas, one for accounting.
one for the LLM.
**Juliano Costa | Datadog** 43:03 Now you, you asked too much of my database knowledge, yeah.
**Pierre Tessier** 43:08 Hmm, sorry.
I can help with this. It's not… it's not overly.
**Juliano Costa | Datadog** 43:14 Okay.
**Pierre Tessier** 43:14 located.
Yeah, yeah. It's mostly, like, right now, we're just straight up whatever, like, the standard public schema is what we're doing. We would just change schema to be accounting, and we'd make sure the user that we're using for everything has permissions on the accounting schema.
Right? We could put everything in public and just make sure all our tables are named differently.
I just feel like that's not following proper design of how people do things in the real world.
**Juliano Costa | Datadog** 43:42 Yep.
Well, but we have an application that has 16 different programming languages, and that's definitely not how people do things in real world.
**Pierre Tessier** 43:54 I don't know, I've worked with a couple financial institutions.
Alright, we're way over time, I appreciate everything.
**Juliano Costa | Datadog** 44:02 Appreciate it. I'm happy…
**Pierre Tessier** 44:03 making more progress, and I will be… I'm also happy I'm gonna get to get much more plugged in Given my role changed here at Honeycomb, To do more of these things, so… I will miss you in Atlanta, Juliano, but I do believe I will… I'm going to the one in Europe next spring.
**Juliano Costa | Datadog** 44:21 Awesome, yeah. Oh, well, there will be, Hotel Unplugged, co-located at Fosden. I don't know if you can make that one.
**Pierre Tessier** 44:30 We'll see about that. We'll see how it works.
**Juliano Costa | Datadog** 44:32 It's just one day. Well, I think KubeCon is easier to get, because then you come for the whole week, and there are plenty of stuff happening.
But anyways, yeah.
Appreciate it, guys.
**Derek Mitchell** 44:44 Thanks for your support.
**Juliano Costa | Datadog** 44:45 Thank you.
**Derek Mitchell** 44:46 Nice to meet you.
**Pierre Tessier** 44:47 Rachel.
**Juliano Costa | Datadog** 44:48 Thanks, Eric.
**Derek Mitchell** 44:49 Thank you.
