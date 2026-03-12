SIG: Community Demo App SIG
Date: 2025-07-16
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/KKU79UXB5_JnWer8piWRSvo1JMkthNZciGDDyHu-phnfYKrTEijz6A4VgOJKdioX.rbwOzfGtZ3cAWR3M
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 02:06 You know, renew.
**Alessio** 02:09 Okay.
**Juliano Costa | Datadog** 02:10 I need to open that. Otherwise I don't have camera.
How's it going.
**Alessio** 02:18 It's going. Well, actually, how's it going for you?
**Juliano Costa | Datadog** 02:22 Yeah. Well, busy week kid got sick. So it's.
**Alessio** 02:26 Oh!
**Juliano Costa | Datadog** 02:27 We don't. We don't have a support network here. So it's just my wife and I juggling around.
**Alessio** 02:36 Where do you live like? Where are you based.
**Juliano Costa | Datadog** 02:39 We are based in Austria.
**Alessio** 02:41 Okay, yeah, that can be challenging. You don't have like grand grandfathers and stuff like that.
**Juliano Costa | Datadog** 02:49 Yeah, I know, yeah.
**Alessio** 02:56 It can be.
**Juliano Costa | Datadog** 02:57 Hey! Brother!
**Alessio** 02:57 Very challenging, hey?
**Juliano Costa | Datadog** 02:59 Yeah, a bit.
But well, yeah, so thankfully, he's getting better. So.
**Alessio** 03:06 Yeah. Also, I think you work remotely right?
**Juliano Costa | Datadog** 03:09 Yep.
**Alessio** 03:10 Okay, that can be a big helper on the personal side and a big slowdown on the work side. Actually.
**Juliano Costa | Datadog** 03:20 Yeah. Well, when when he's at home, it's tricky to to work. But yeah, yeah, it's fine. Yeah, hopefully.
**Alessio** 03:32 Yeah.
**Juliano Costa | Datadog** 03:33 But by Monday he is back to the daycare, and I.
**Alessio** 03:37 That's that's fine! That's fine!
**Juliano Costa | Datadog** 03:48 Jonathan, am I missing something on? I think I I reviewed your pr on the open telemetry, I/O. But did it get merged.
**Jonathan Munz** 04:03 I think so. Yeah.
**Juliano Costa | Datadog** 04:04 Okay. Perfect.
**Jonathan Munz** 04:04 I just had a comment on the issue, because I don't have the permission to close the original issue. But I think the Docs Pr. And the demo repo pr both got merged.
**Juliano Costa | Datadog** 04:14 Awesome. Yeah, the the demo I I know, but I wasn't keeping track on the on the i 0 1 think one sec. Let me just add shouldn't. Look here, the agenda.
I have one thing that I want to discuss. Well, I would love to hear everyone's opinion.
There is a Pr. From well, Pr. 2340 enhanced Prometheus integration and Rafana Apm dashboard.
where the guy Cyril, I think if I'm pronounce pronouncing correctly his name. Shared added a kind of a Apm view on the It's working it. It's not beautiful, but yeah, I'm it. It is, it is what it is. 1 1 thing that bothers me and I I shared that feedback with him is that he has 2 to kind of tables at the beginning. One is for HP. Red metrics, and the other one is for Jrpc. Red metrics, and you you can choose in a dropdown the service that you want to to view.
and if this service emits or communicates through Http, you get the Http red metrics, and if not. There. The Htp metrics are empty. Kind of no data.
So me personally, I don't like having this kind of broken experience. Looks like the dashboard is broken, and it's missing data. But it's not actually, it's just that this data is not available for this service.
But I feel that this may bring some questions from from users. So I would love to hear your opinion. And and then like to me, it looks fine. I just yeah.
**Roger Coll** 06:43 Why, having these 2 separate, let's say red diverse for the Rtc. And Scp way. Not just one. And and that's it. And if it's empty. Just don't show it up.
I don't know if it's possible. This in Grafana.
if a metric it's it's null , just skip it, but.
**Juliano Costa | Datadog** 07:09 I think he mentioned that this will be available on Revenue 12.
I don't know which version Griffin is, but yeah, but it's not available at the moment.
and one thing is that he could. He said that he could aggregate Http and Rpc. Jpc. Red metrics and show them kind of combine.
but I don't know. I told him that I I prefer them split. But yeah, I'm kind of yeah, because they they're not quite the same right?
I mean, there are red metrics, but they are to different protocols. And or does that matter or not?
**Roger Coll** 08:00 But I guess you can always use labels right or in the you know, when it says, p. 99, p. 90, just a label saying that protocol? Right?
That's it.
Then.
Yeah, maybe for Http and services that have both it. You're very convoluted.
Nice words. But yeah, don't have any other solution for the no data graphs.
**Juliano Costa | Datadog** 08:40 Yeah. Hi, I think it will be hard to get dashboards. Hmm, wait.
It will be difficult to have dashboards that do not have if we merge Grpc and HP. It will be difficult to have dashboards empty, because we would have either one or the other right, unless, for instance, you get I don't know Flag D, or the services that are not actual part of the demo I mean Flag D is part of the demo, but I don't think we generate red metrics out of it.
Or are we, Gene? I I think we are actually generating red metrics from the spend metrics processor. So it's tricky because I don't use the demo with Grafana. I use the demo with better dog, and I know how Badadog works. I don't know how Grafana works. So.
**Roger Coll** 09:43 Yeah, same for me. And in elastic, the or the kiwana, the fall dice. For there isn't this differentiation between Grpc and Http everything, and throughput the latency. And if you want to get the details of each one of the the one that failed.
you will have that on the attributes. So.
**Juliano Costa | Datadog** 10:08 And even that's actually true, even for datadog. We we have red metrics. We don't. We don't differentiate or Http, so that's a good thing. Oh, thank you.
Yeah. I'll actually raise that to him.
Awesome.
**Jonathan Munz** 10:27 You might have said this, but I was just curious in like the normal running of the demo, like sort of vanilla out of the box. Nothing is reported for Grpc recorded, you mean like, No, like, if you just.
this is like this is the data showing in this Grafana dashboard is coming from like of a vanilla run of the demo and clicking around and stuff. In doing that you wouldn't get any with the normal like. Make start. You wouldn't get any telemetry that is Grpc.
**Roger Coll** 11:04 No, I guess you get telemetry, but you don't get the dashboards.
I I think this Pr is just adding dashboards over the already available Grpc. Or Http. Telemetric.
**Jonathan Munz** 11:16 Right? Right? So I guess my question is because that changes how I feel about whether you would see no data or not. No data for the Grpc like, if if in the normal run of the demo of just clicking around, you would expect spans to be generated for Http and for Grpc. I think it's useful to see the no data for Grpc, because it points to something wrong in the demo setup versus. If if Grpc is only emitted in very specialized uses of the demo.
That would change. How I feel about that being displayed that way, I guess.
like in what circumstances of using the demo. Would you see telemetry for Grpc. I guess, would be the question.
**Roger Coll** 12:02 I guess it depends on the service right? There's some service that using Glpc and and some others that use Http, and not sure if some both, but maybe usually I don't know.
**Juliano Costa | Datadog** 12:15 I don't think we have. Well, I I I know that we have clients, for instance, I think, checkout has Jrpc calls, and also HP. Calls, but not server. So if you have, if you are a Jpc. Server, you're just Jpc, and if you're a Http server, or just. HP, so I know 2 services that are, I should be server now.
the the rust service like that is shipping because we are using actix web, which is a web framework for rust that has an instrumentation library and Php, because the Jrpc. Implementation for Php server side isn't kind of properly supported by the Jp. If you go to the Jrpc. Dot, I/O, you can't find the instructions. There are some like contributors forks somewhere, but we just opted to not use.
**Jonathan Munz** 13:20 I see.
**Juliano Costa | Datadog** 13:22 But other than that, we, we try to kind of focus on Jrpc. Everywhere.
**Jonathan Munz** 13:27 Okay?
Yeah. I mean, I think this, I think this is interesting, because I think my answer changes for the demo versus like as someone consuming my own data in my own Grafana dashboard. I probably would combine it and want to see just everything together. I think, for the special case of this being tied to the demo, and the fact that we are having services behave different ways for the purposes of showing the instrumentation differently across Http and Grpc. I would then almost lean towards showing them separately and and side by side, because that's more demonstrating the different types of telemetry coming from the demo, but that's just my opinion. But I agree that if I was building this myself for my own app monitoring.
I probably wouldn't like seeing the 2 separate sets of charts either, but.
**Juliano Costa | Datadog** 14:20 Awesome.
**Jonathan Munz** 14:21 But it is. Yeah, we're we're. We're in a bit of a special case, because it is, it is the demo. So yeah, I don't know.
**Juliano Costa | Datadog** 14:32 cool. Okay, so I'll I'll post this feedback to him. One thing that I have we have here in the agenda. I think it was you, Jonathan.
that edit.
**Jonathan Munz** 14:42 Yeah, this is just a quick question a coworker had for. And I've actually only ever run the demo locally. So I didn't actually know the answer to this, but he was curious if he could just avoid, because he just wanted to check a quick thing, and whether there was a hosted version of the demo somewhere that he could just ping. But I didn't know the answer.
**Juliano Costa | Datadog** 15:00 I know that some vendors have that running but usually you would navigate on their back end, because that's what they're using the the demo to to showcase.
**Shenoy Pratik** 15:14 Yeah, we do have a playground that's open.
**Juliano Costa | Datadog** 15:18 Yeah, so, yeah.
**Alessio** 15:21 Mean a hosted version of the demo. It's actually like on the don't. We have, like on the readme, a list of deployed Demos by company.
**Juliano Costa | Datadog** 15:31 Well, it's not deployed. But those are folks right.
**Alessio** 15:35 Oh, okay.
**Shenoy Pratik** 15:36 Take them and deploy it.
**Juliano Costa | Datadog** 15:39 Yeah, depend depending on the on the on the vendor. So, for instance, I know the the data, Doc, one, I wrote a doc explaining how to send the demo data to data, Doc. So then, I just pointed.
So people that want to use the demo with just follow those instructions. I think Banner Trace has something like that as well. I don't know what elastic has. Let me check.
**Roger Coll** 16:04 Yeah.
**Juliano Costa | Datadog** 16:05 Yeah.
**Roger Coll** 16:05 Same office and as open source. I just share the public deployment. But it's just let's say, Kibana, it's not. We don't expose the shopping, etc. But that's the demo behind. Yeah.
**Jonathan Munz** 16:19 Okay.
**Alessio** 16:20 Yeah.
**Jonathan Munz** 16:21 I can. I can share these links with that person. Yeah, cool. All right.
Thank you.
**Juliano Costa | Datadog** 16:29 No worries and da-da-da any.
Let me check here.
Well, we do not have any Prs open. Do we have any issues that are more like concerning.
If not, I would just try to to cut a release by this week, or maybe next week. I don't know how how I'm gonna how it's gonna be the rest of my week. With a sick kid I already shared with Alessio that but But if I can do this this week most probably next week I can. I can do, and maybe I can even schedule something with Roger. So we go together, Roger. So you also know the process of how how to do? I don't know if you have ever released something. But yeah, I think the process.
**Roger Coll** 17:39 Yeah, we can sing also for the Ham chart. Maybe we need some help there or.
**Juliano Costa | Datadog** 17:45 Home chart is a mess.
But yes, we need to. We need to do that as well. A couple of environment variables will will change.
So yeah, this is gonna be tricky. But yeah, we can. We can.
**Alessio** 18:00 Sounds good. Thank you.
**Juliano Costa | Datadog** 18:03 Cool.
**Shenoy Pratik** 18:03 Oh, let me know if you, if you need any help from my side as well, I can pitch in. Yeah.
**Juliano Costa | Datadog** 18:08 Yeah, I still need to add you as a approver. Sorry I I haven't.
**Shenoy Pratik** 18:12 And that's strange.
I also had questions around health. So I see there are 2 places where we have helm charts. Right? One is in the Demo report itself. And there's the other Kubernetes hotel chart somewhere.
Yeah. So to be updated with.
**Juliano Costa | Datadog** 18:32 So in the demo itself we have just the manifest files.
and the manifest files are generated from the from the helm. So we first.st So we 1st release a new version. Yeah, the release process is tricky. So we 1st release a new version and then we go to the helm repo and update the the helm version.
and once the helm version, once the the new helm Pr is merged, then we come back to the demo and run like, make. Generate Kubernetes manifest something like that. And then we have the whole kids manifest generated, based on the helm chart.
And then we just commit that it would be awesome to have some automation on this kind of I don't know checking if there was any pr merged on on the health chart and then opening a Pr automatically to us.
**Shenoy Pratik** 19:32 Check it.
**Juliano Costa | Datadog** 19:33 Because this is just manual work. And sometimes it happened that we bumped one environment variable on the helm chart, and then we forgot to run the make comment. So people started complaining. And then we said, Okay, yeah, it's missing this thing that we already released like 2 months ago. But yeah, nobody ran the comment. So yeah, it's from 2 error. That's what I what I'm trying to say.
**Shenoy Pratik** 19:57 Okay.
**Juliano Costa | Datadog** 20:04 Cool any anything else that you would like to share. Anyone would like to discuss.
**Alessio** 20:13 I just wanted to tell you that I started rewriting the flag Dui in Elixir, but like don't expect anything, because I have a huge dungeons and dragons campaign running, and they are like asking for a lot of stuff at the moment. So I hope I could devote some more time to that. But yeah.
**Juliano Costa | Datadog** 20:38 Awesome.
Yeah, no, don't worry. No, no pressure on that. Whenever we have, we have. And yeah.
I do. Miss Elixir airline in the demo. So.
**Alessio** 20:52 It's coming slowly.
**Juliano Costa | Datadog** 20:57 Yeah, I I me personally, I would love to have all the other all the other kind of supported languages. So when you go to the open telemetryio, you go to the, to the languages, and then there there is this other where I think they have Lua and.
**Alessio** 21:18 Yeah, we'll book on trip.
Stuff like, yeah.
**Juliano Costa | Datadog** 21:22 Other rep was that are not under the hotel umbrella, but they are hotel compliant, so I would love to have all of them in a demo. But yeah, then things like the discussion that we had in the chat.
**Alessio** 21:37 Yeah, exactly.
**Juliano Costa | Datadog** 21:38 Next week, like we just because.
**Alessio** 21:41 Yeah, the the about the footprint, you mean. Yeah, it's like we would have a lot of footprint. And yeah, we would have also the same discussion we had for elixir, like we to to find where where a specific language fits, for example. So it's but it's yeah. It would be nice, actually, anyway. Don't think.
**Juliano Costa | Datadog** 22:03 But yeah, no worries. And and as we got into this discussion, I want to ask Chennai, one thing.
currently, we are using a open search image that has one dot, one giga. Is there a kind of a smaller version? Because in the demo we are not actually using the the front end of opensearch. Right? We just.
**Shenoy Pratik** 22:30 Yeah.
Shouldn't.
**Juliano Costa | Datadog** 22:31 The back end.
**Shenoy Pratik** 22:31 The yeah. The docker currently just has backend itself that I use.
**Juliano Costa | Datadog** 22:36 Oh, it's.
**Shenoy Pratik** 22:36 So, but I can. I can think of a smaller version, but it needs to be built and run time where you have.
I'm not sure that even has a docker shipped out. There is something called as open Search core, which is shipped out without plugins, but in that case you will not have the SQL. And Ppl. Plugin, which is used by Grafana for querying to opensearch.
so I can take a look and see if we can make it smaller. But are you talking about the docker footprint, or the memory consumed by open search being smaller.
**Juliano Costa | Datadog** 23:12 Well, I think those 2 things would be great to improve, I think at the moment, if I do let me just check the so the open search one is one dot, 2 GB. So if we can reduce this, this would be awesome.
and honestly, I don't know how much we are allocating for the for the open search at the moment just opening here one sec.
**Shenoy Pratik** 23:55 Yeah, see? 1.1.
**Juliano Costa | Datadog** 23:56 One day.
**Shenoy Pratik** 23:57 Can remember.
**Juliano Costa | Datadog** 23:57 Point one, yeah, that that's a lot.
If if we can have something like smaller that would be awesome.
**Shenoy Pratik** 24:07 Okay. Yeah.
**Juliano Costa | Datadog** 24:08 Okay.
**Shenoy Pratik** 24:08 Me!
**Juliano Costa | Datadog** 24:09 Any any improvement that you can bring? On that regards that would be be great. And if you think about the the thing that you you said about building the building a custom image. We could do that. We just, we would just need to create a folder at the docker file and ship our own open search. Demo version.
**Shenoy Pratik** 24:36 Yeah, it would be similar to other services. Something like that custom image. Okay, let me take.
**Juliano Costa | Datadog** 24:43 That's awesome.
**Shenoy Pratik** 24:43 Contact. Yes, that's a good task.
**Juliano Costa | Datadog** 24:47 Cool, appreciate that.
**Roger Coll** 24:51 Yeah, also for the low generator. It's super heavy. I think it's 700 or 900 MB. Just the image.
And it's it's a pretty simple feature, right it should be, at least
**Juliano Costa | Datadog** 25:07 It is, but it's not I. I've done some research on that, because there is there is a error that the the low generator is generating. I don't know if how often you guys run the demo. But I I run a lot, and if you check the logs of the low. Gen. You will see that it has a weird error there, and I was checking for other other tools that could do the same. And there's none that actually do the the browser thingy.
So the the playwright.
the is, the is the tricky part of it. Because locust is basically we could replace locust with that.
**Roger Coll** 25:50 From you.
**Juliano Costa | Datadog** 25:51 And whatever but like a busy, busy box with girl, and that would solve our low gen problem. But the the click parting is, the is the tricky one, and I think there there is selenium, but the the image is even bigger, and it's like.
**Roger Coll** 26:12 Okay. Okay. Yeah.
No race, you know.
**Juliano Costa | Datadog** 26:16 Yeah. Well, if you hear about anything, just so.
**Roger Coll** 26:21 Yeah, we can send it. Okay, thanks. Thanks for the for the context.
**Juliano Costa | Datadog** 26:29 Yeah. And I I don't know. I I know that some observability vendors have synthetic tests, that it is kind of that you go and configure click paths to. So the user will open this page and then click here, click here, click here. So you kind of validate the availability of the page and the the flow that you want to test. But that also would be something.
tied to the to the vendor, and not we try to to keep everything open? Source so also, wouldn't we? An option for us?
Well, actually, I never! I never googled for synthetic open source synthetic testing.
I'll I'll do that. Breakout open status.
Hq.
cool. Yeah, I have homework. Thanks, Roger.
**Roger Coll** 27:58 And also take a look. I guess something.
Yeah, it will be difficult, at least, to have all the features that focus have. But yeah, we can take a look.
**Juliano Costa | Datadog** 28:13 Yeah, I think that the our main.
our main thing is the click path like the the actual the browser synthetic load, because the other.
the the curl to the to the endpoints to the Api of the front end is easy to to fix, easy to w get occur, or like.
**Roger Coll** 28:41 Yeah, yeah, yeah, that's not.
**Juliano Costa | Datadog** 28:50 Cool, awesome. So then have a great rest of day, everyone, and see you all in 2 weeks.
The 3rd good good luck with the the campaign unless you.
**Alessio** 29:06 Frankly, thanks, I'll need it.
Thanks.
**Roger Coll** 29:10 So.
**Juliano Costa | Datadog** 29:10 But.
